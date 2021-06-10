from setuptools import setup, find_packages
import pathlib

VERSION = '1.0'
HERE = pathlib.Path(__file__).parent
README = (HERE / 'readme.md').read_text()

# Setting up
setup(
    name='pykitsu',
    version=VERSION,
    author='MetaStag',
    author_email='thegreek132@gmail.com',
    url='https://github.com/MetaStag/Pykitsu',
    description='A simple api wrapper for the kitsu api written in python',
    long_description=README,
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
