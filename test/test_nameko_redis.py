import eventlet
eventlet.monkey_patch()  # noqa (code before rest of imports)

from nameko.containers import ServiceContainer
from nameko.testing.services import entrypoint_hook, dummy
import pytest

from redis import StrictRedis
from nameko_redis import Redis, REDIS_URIS_KEY


TEST_KEY = 'nameko-test-value'


class ExampleService(object):
    name = "exampleservice"

    redis = Redis('server')

    @dummy
    def write(self, value):
        self.redis.set(TEST_KEY,  value)

    @dummy
    def read(self):
        return self.redis.get(TEST_KEY)


@pytest.fixture
def redis_db(request):
    url = 'redis://localhost/0'

    def redis_teardown():
        client = StrictRedis.from_url(url)
        client.delete(TEST_KEY)
    request.addfinalizer(redis_teardown)
    return url


def test_end_to_end(redis_db):
    config = {
        REDIS_URIS_KEY: {
            'server': redis_db
        }
    }

    container = ServiceContainer(ExampleService, config)
    container.start()

    # write through the service
    with entrypoint_hook(container, "write") as write:
        write("foobar")

    # verify changes written to redis
    client = StrictRedis.from_url(redis_db)
    assert client.get(TEST_KEY) == b'foobar'

    # read through the service
    with entrypoint_hook(container, "read") as read:
        assert read() == b"foobar"