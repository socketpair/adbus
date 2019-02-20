#!/usr/bin/python

import sys

from setuptools import Extension, setup, find_packages

__module__ = 'adbus'
__url__ = 'https://github.com/ccxtechnologies'

__version__ = None
exec(open(f'{__module__}/__version__.py').read())

if "--nosystemd" in sys.argv:
    sys.argv.remove("--nosystemd")

if "--cythonize" in sys.argv:
    sys.argv.remove("--cythonize")

setup(
    name=__module__,
    version=__version__,
    author='CCX Technologies',
    author_email='charles@ccxtechnologies.com',
    description='asyncio based dbus interface',
    long_description=open('README.rst', 'rt').read(),
    license='MIT',
    url=f'{__url__}/{__module__}',
    download_url=f'{__url__}/archive/v{__version__}.tar.gz',
    python_requires='>=3.7',
    packages=find_packages(exclude=["tests"]),
    setup_requires=[
        'setuptools>=18.0',  # Handles Cython extensions natively
        'cython>=0.25.2',
    ],
    ext_modules=[
        Extension(
            f"{__module__}.sdbus",
            sources=[f"{__module__}/sdbus.pyx"],
            libraries=["systemd"],
        )
    ],
)
