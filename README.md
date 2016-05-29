# nameko-redis
Redis dependency for nameko services

## Installation
```
pip install nameko-redis
```

## Usage
```python
from nameko.rpc import rpc
from nameko_redis import Redis


class MyService(object):
    name = "my_service"

    redis = Redis('development')

    @rpc
    def hello(self, name):
        self.redis.set("foo", name)
        return "Hello, {}!".format(name)

    @rpc
    def bye(self):
        name = self.redis.get("foo")
        return "Bye, {}!".format(name)
```
To specify redis connection string you will need a config
```yaml
AMQP_URI: 'amqp://guest:guest@localhost'
REDIS_URIS:
 development: 'redis://localhost:6379/0'
```
