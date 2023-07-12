# Lindex *[List Index]*
### by @some1and2
A `python` Library created to improve functionality of Nested Dictionaries in Python

# Usage::
```python
from Lindex import lindex
dictionary = {}
dictionary = lindex(dictionary)
```

# Functionality::

- Making a Lindex Dictionary
	```python
	dictionary = lindex(dictionary)
	```

- Ability to index Nested Dictionaries by using a list
	```python
	print(dictionary.RTN(*path))
	```

	if `path` is a list of indexes of the dictionary then this will return `dictionary[path[0]][path[1]][path[2]]...`


- Ability to change information from a Nested Dictionary through a list
	```python
	dictionary.set(*path, value)
	```
	if `path` is a list of indexes of the dictionary, then whatever value is at the end of `dictionary[path[0]][path[1]][path[2]]...` will be set to `value`

- Ability to add to a number from a Nested Dictionary indexed through a list
	```python
	dictionary.add(*path, value)
	```
	whatever value is at the end of `dictionary[path[0]][path[1]][path[2]]...` will be added added with `value`

- Ability to pretty print dictionaries
	```python
	dictionary.pprint()
	```

# Installation::
```python
pip install Lindex
```
---

**Documentation** *[Coming Soon]*