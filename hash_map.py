class HashMap:
	def __init__(self):
		self.mod_val = 100
		self.hashtable = [[] for i in range(self.mod_val)]
		self.keys = list()

	def hashfunc(self, key):
		count = 0
		for i in key:
			count += ord(i)
		return count % self.mod_val

	def __setitem__(self, key, val):
		loc = self.hashfunc(key)
		if not len(self.hashtable[loc]):
			self.hashtable[loc].append((key,val))
			return
		for i, j in enumerate(self.hashtable[loc]):
			if len(j) == 2 and j[0] == key:
				self.hashtable[loc][i] = (key, val)
			else:
				self.hashtable[loc].append((key, val))

		if key not in self.keys:
			self.keys.append(key)




	def __getitem__(self, key):
		getval = None
		loc = self.hashfunc(key)
		for i,j in enumerate(self.hashtable[loc]):
			if j[0] == key:
				getval = self.hashtable[loc][i][1]
		return getval

	# def __repr__(self):
	# 	string = "{ "
	# 	for kiss in self.keys:
	# 		val = self.hashtable[self.hashfunc(kiss)]
	# 		string += f"{kiss} : {val}"
	# 		string += " "
	# 		# print((kiss, val), end=" ")
	# 	string += "}"
	# 	return string


obj = HashMap()
# print(obj.hashfunc("Dec 29"))
obj['Jun 2'] = 129
obj['Jun 5'] = 330

for key in obj.keys:
	print(key, obj.hashtable[obj.hashfunc(key)])
print(obj['Jun 2'])
print(obj['Jun 5'])

# print(obj.hashtable)