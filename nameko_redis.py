from nameko.extensions import DependencyProvider
from redis import StrictRedis as _StrictRedis


REDIS_URIS_KEY = 'REDIS_URIS'


class Redis(DependencyProvider):

    def __init__(self, key, **options):
        self.key = key
        self.client = None
        self.options = {
            'decode_responses': True,
        }
        self.options.update(options)

    def setup(self):
        redis_uris = self.container.config[REDIS_URIS_KEY]
        self.redis_uri = redis_uris[self.key]

    def start(self):
        self.client = _StrictRedis.from_url(self.redis_uri, **self.options)

    def stop(self):
        self.client = None

    def kill(self):
        self.client = None

    def get_dependency(self, worker_ctx):
        return self.client
