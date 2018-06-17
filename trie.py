# 162,
class Trie_Node:
	def __init__(self):
		self.isunique = True
		self.map = dict()


	def insert(self,word,T):
		prev = T 
		for char in word:
			if char in prev.map:
				prev.isunique = False
				prev = prev.map[char]
			else:
				T = Trie_Node()
				prev.map[char] = T
				prev = T 

	def iscontains(self,prefix,T):
		prev = T
		isunique = False
		for i,char in enumerate(prefix):
			if char in prev.map:
				if i==len(prefix)-1:
					isunique = prev.isunique
				prev = prev.map[char]
			else:
				return False,False
		return True,isunique

	def print_trie(self,T):
		if len(T.map)>0:
			print(T.isunique, T.map.keys())
			for key in T.map.keys():
				print_trie(T.map[key])


if __name__=='__main__':
	arr = ['dog','cat','apple','apricot','fish','fissy','fixit','doggy']
	T = Trie_Node()
	for word in arr:
		T.insert(word,T)
	print(T.iscontains('app',T))
	print(T.print_trie(T))