import sys
from setuptools import setup


install_requires = [
    'asyncio',
    'asyncpg',
    'aiohttp',
    'aiohttp-utils',
    'cchardet',
    'uvloop',
]

PY_VER = sys.version_info

if PY_VER < (3, 5):
    raise RuntimeError("aio-demo doesn't suppport Python earlier than 3.5")


classifiers = (
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Operating System :: POSIX',
    'Environment :: Web Environment',
    'Development Status :: 4 - Beta',
)

setup(
    name='aoidemo',
    version='1.0.0',
    description=('Simple REST demo using aiohttp.'),
    classifiers=classifiers,
    platforms=['POSIX'],
    author='Lucas Roesler',
    author_email='roesler.lucas@gmail.com',
    license='BSD',
    packages=['aiodemo', ],
    install_requires=install_requires,
)
