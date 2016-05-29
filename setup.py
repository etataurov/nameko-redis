from setuptools import setup

setup(
    name='nameko-redis',
    version='1.0.0',
    url='https://github.com/etataurov/nameko-redis/',
    license='Apache License, Version 2.0',
    author='etataurov',
    author_email='tatauroff@gmail.com',
    py_modules=['nameko_redis'],
    install_requires=[
        "nameko>=2.0.0",
        "redis"
    ],
    description='Redis dependency for nameko services',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
