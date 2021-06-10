# Pykitsu

Pykitsu is a simple api wrapper for the [kitsu](https://kitsu.io/explore/anime) api written in python. It should work without any problems on any reasonably recent version of python.

### Installation
Pykitsu can be installed from pypi
```bash
$ pip install pykitsu
```

### Dependencies
This module requires only one external module, `requests`, which should be installed by-default with python. In case it's not, you can install it with pip:
```bash
$ pip install requests
```

### Example
```py
>>> import pykitsu # import the module
>>> pykitsu.search('anime', 'bakemonogatari')
{'count': 2, '3919': 'Bakemonogatari', '4800': 'Bakemonogatari Recap'}
>>> # A dictionary is returned, from where we can get the id of the anime
>>> pykitsu.get_info('anime', 3919) # Taking the id from the above dictionary
{'createdAt': '2013-02-20T17:00:18.998Z', 'updatedAt': '2021-06-10T06:00:15.132Z', 'slug': 'bakemonogatari', 'synopsis': '#long description', 'coverImageTopOffset': 20, 'titles': {'en': 'Bakemonogatari', 'en_jp': 'Bakemonogatari', 'ja_jp': '化物語'}, 'canonicalTitle': 'Bakemonogatari', 'abbreviatedTitles': ['Ghostory']}
>>> # Note that a lot more data is returned in the dictionary, but for the sake of keeping it simple, the dictionary has been truncated here
```

### Docs
The documentation can be found [here](https://github.com/MetaStag/Pykitsu/wiki)

### License
This project can been licensed under the [MIT](https://github.com/MetaStag/Pykitsu/blob/main/LICENSE) license.
