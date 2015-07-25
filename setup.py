from distutils.core import setup

setup(
    name='nameko-redis',
    version='0.0.1',
    url='https://github.com/etataurov/nameko-redis/tree/master',
    license='Apache License, Version 2.0',
    author='etataurov',
    author_email='tatauroff@gmail.com',
    py_modules=['nameko_redis'],
    install_requires=[
        "nameko>=2.0.0",
        "redis"
    ],
    description='Redis dependency for nameko services'
)
