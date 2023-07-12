#!/usr/bin/env python3

class lindex(dict):
	def __init__(self, dictionary: dict = {}, StringIndexes: bool = False, debug: bool = False):
		"""
		init class for lindex
		Args:
			dictionary:
				The dictionary being converted to a lindex dictionary
			StringIndexes:
				Converts all keys to strings (don't use if you are using lists)
			debug:
				Shows all debug messages from lindex
		"""
		super().__init__(dictionary)
		self.StringIndexes = StringIndexes
		self.debug = debug

	# Pretty Prints Dictionary
	def pprint(self, EmptyString: str = "    ") -> bool:
		def PrintSubsection(dictionary: dict, EmptyString: str, SpaceAmnt: int = 0):
			if type(dictionary) == type(self) or type(dictionary) == dict:
				return "\n".join( EmptyString * SpaceAmnt + f"{entry}: {type(entry)}\n" + PrintSubsection(dictionary[entry], EmptyString, SpaceAmnt + 1) for entry in dictionary )
			else:
				return EmptyString * SpaceAmnt + str(dictionary)
		print(PrintSubsection(self, EmptyString))
		return

	# Add `value` to self[arg[0]][arg[1]][arg2]...
	def add(self, *args) -> bool:

		value = args[-1]
		args = args[:-1]

		OldValue = self.RTN(*args)

		try:
			self.set(*args, OldValue + value)
			return True
		except TypeError as e:
			print(f"TypeError: {e}\nIgnoring Exception on `add`")
			return False

	# Sets self[arg[0]][arg[1]][arg2]... to value
	def set(self, *args) -> bool:
		if self.StringIndexes:
			args = tuple(str(i) for i in args)

		value = args[-1]
		args = args[:-1]

		def Carve(PointsDict: dict, Indexes: tuple, FinalState, States: list = []) -> list:
			States.append(PointsDict)
			if len(Indexes) == 0:
				States[-1] = FinalState
				return States
			try:
				if type(PointsDict) in [dict, lindex]:
					if Indexes[0] not in PointsDict.keys():
						PointsDict[Indexes[0]] = {}
				if type(PointsDict) == list:
					if type(Indexes[0]) != int or not(0 <= Indexes[0] < len(PointsDict)):
						PointsDict[Indexes[0]] = {}
			# If the index already exists as an entry, PointsDict will be set to the end value instead of a dictionary
			# To prevent errors occuring because of this, the previous `if` statment uses the `.keys()` function to check for keys instead of just using `in` directly on the `PointsDict`
			# The error then moves to become an `AttributeError` when a final value is being used as an index. 
			except AttributeError:
				PointsDict = {Indexes[0]: {}}
				States[-1] = {States[-1]: {}}
			return Carve(PointsDict[Indexes[0]], Indexes[1:], FinalState, States)

		def Write(Indexes: tuple, States: list) -> dict:
			for i in range(len(States) - 1):
				States[-i-2][Indexes[-i-1]] = States[-i-1]
			return States[0]
		self = super().__init__(Write(args, Carve(self, args, value)))
		return True

	# Returns self[arg[0]][arg[1]][arg2]...
	def RTN(self, *args):
		def Carve(dictionary: dict, Indexes: tuple):
			if len(Indexes) == 0:
				return dictionary


			if type(dictionary) in [dictionary, type(self)]:
				if Indexes[0] not in dictionary:
					raise KeyError(f"\"{Indexes[0]}\" is not a Valid Dictionary Key - {dictionary}[{Indexes[0]}]")
			if type(dictionary) == list:
				if type(Indexes[0]) != int or not (0 <= Indexes[0] < len(dictionary) ):
					raise KeyError(f"Index out of range - {dictionary}[{Indexes[0]}]")
			try:
				return Carve(dictionary[Indexes[0]], Indexes[1:])
			except TypeError as e: # This is only a type error because the dictionary is not being set to a dictionary, in reality the problem is with the `Keys` supplied
				if self.debug:
					print(f"KeyError: `*path` Includes Final Value\nIgnoring Exception on `RTN`")
		try:
			if self.StringIndexes:
				args = tuple(str(i) for i in args)
			return Carve(self, args)
		except KeyError as e:
			if self.debug:
				print(f"KeyError: {e}\nIgnoring Exception on `RTN`")

if __name__ == "__main__":
	...
