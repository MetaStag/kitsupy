from setuptools import setup, find_packages
from os import path

VERSION = '1.1'
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

# Setting up
setup(
    name='kitsupy',
    version=VERSION,
    author='MetaStag',
    author_email='thegreek132@gmail.com',
    url='https://github.com/MetaStag/Pykitsu',
    description='A simple api wrapper for the kitsu api written in python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'api-wrapper', 'kitsu', 'anime'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
    ]
)
