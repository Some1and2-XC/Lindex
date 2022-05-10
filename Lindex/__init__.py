#!/usr/bin/env python3

class lindex(dict):

	# Pretty Print Dictionary
	def pprint(self, EmptyString: str = "    ") -> bool:
		def PrintSubsection(dictionary: dict, EmptyString: str, SpaceAmnt: int = 0):
			if type(dictionary) == type(self) or type(dictionary) == dict:
				return "\n".join( EmptyString * SpaceAmnt + f"{entry}:\n" + PrintSubsection(dictionary[entry], EmptyString, SpaceAmnt + 1) for entry in dictionary )
			else:
				return EmptyString * SpaceAmnt + str(dictionary)
		print(PrintSubsection(self, EmptyString))
		return

	# Add num to self[arg[0]][arg[1]][arg2]...
	def add(self, *args, num: int = None) -> bool:
		if num is None:
			num = args[-1]
			args = args[:-1]
		OldNum = self.RTN(*args)
		if (type(OldNum) == int or type(OldNum) == float) and (type(num) == int or type(num) == float) :
			self.set(*args, num = num + OldNum)
			return
		else:
			assert False
			return

	# Sets self[arg[0]][arg[1]][arg2]... to num
	def set(self, *args, num = None) -> bool:
		if num is None:
			num = args[-1]
			args = args[:-1]
		def Carve(PointsDict: dict, Indexes: tuple, FinalState, States: list = []) -> list:
			States.append(PointsDict)
			if len(Indexes) == 0:
				States[-1] = FinalState
				return States
			if Indexes[0] not in PointsDict:
				PointsDict[Indexes[0]] = {}
			return Carve(PointsDict[Indexes[0]], Indexes[1:], FinalState, States)

		def Write(Indexes: tuple, States: list) -> dict:
			for i in range(len(States) - 1):
				States[-i-2][Indexes[-i-1]] = States[-i-1]
			return States[0]
		self = super().__init__(Write(args, Carve(self, args, num)))
		return

	# Returns self[arg[0]][arg[1]][arg2]...
	def RTN(self, *args):
		def Carve(dictionary: dict, Indexes: tuple):
			if len(Indexes) == 0:
				return dictionary
			if Indexes[0] not in dictionary:
				assert False
				return
			return Carve(dictionary[Indexes[0]], Indexes[1:])
		return Carve(self, args)
