from nameko.extensions import DependencyProvider

from redis import StrictRedis as _StrictRedis

REDIS_URIS_KEY = 'REDIS_URIS'


class Redis(DependencyProvider):
    def __init__(self):
        self.client = None

    def setup(self):
        service_name = self.container.service_name
        redis_uris = self.container.config[REDIS_URIS_KEY]
        self.redis_uri = redis_uris[service_name]

    def start(self):
        self.client = _StrictRedis.from_url(self.redis_uri)

    def stop(self):
        self.client = None

    def kill(self):
        self.client = None

    def get_dependency(self, worker_ctx):
        return self.client
