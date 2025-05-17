from setuptools import setup, find_packages

setup(
    name='iplookup',
    version='1.0',
    description='CLI tool to get IP address information',
    author='Sojan',
    packages=find_packages(),
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'iplookup=iplookup.cli:main',
        ],
    },
)
