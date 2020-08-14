import re
import setuptools
from setuptools.command.test import test as TestCommand

extras_require = {
    'tests': [
        'pytest',
        'pytest-cov',
        'mock',
        'iso8601',
    ],
}

packages = setuptools.find_packages('.', exclude=('tests', 'tests.*'))

setuptools.setup(
    name='pilo',
    version=(
        re
        .compile(r".*__version__ = '(.*?)'", re.S)
        .match(open('pilo/__init__.py').read())
        .group(1)
    ),
    url='https://github.com/bninja/pilo/',
    license=open('LICENSE').read(),
    author='egon',
    author_email='egon@gb.com',
    description='Yet another form parser.',
    long_description=open('README.rst').read(),
    packages=packages,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    extras_require=extras_require,
    tests_require=extras_require['tests'],
    install_requires=[],
    setup_requires=['pytest-runner'],
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
