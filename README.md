--lindex-- (list index)
by @some1and2
Lindex is a Library created to improve functionality of Nested Dictionaries in Python
Some Added functionality includes:

	 - Being able to index Nested Dictionaries by using a list
		ex:
			print(lindex(dictionary).RTN(*path))
		if `path` is a list of indexes of the dictionary then this will return `dictionary[path[0]][path[1]][path[2]]...`

	 - Being able to change information from a Nested Dictionary through a list
		ex:
			dictionary = lindex(dictionary)
			dictionary.set(*path, num)
		Again if `path` is a list of indexes of the dictionary, then whatever value is at the end of 
		`dictionary[path[0]][path[1]][path[2]]...` will be set to `num`

	 - Being able to add to a number from a Nested Dictionary indexed through a list
		ex:
			dictionary = lindex(dictionary)
			dictionary.add(*path, num)
		whatever value is at the end of `dictionary[path[0]][path[1]][path[2]]...`
		will be added added with `num`
	 - Being able to pretty print dictionaries
		ex:
			lindex(dictionary).pprint()