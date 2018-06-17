'''
This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:

dog
cat
apple
apricot
fish
Return the list:

d
c
app
apr
f
'''
class Trie_Node:
	def __init__(self):
		self.isunique = True
		self.map = dict()

def insert(word,T):
	prev = T 
	for char in word:
		if char in prev.map:
			prev.isunique = False
			prev = prev.map[char]
		else:
			T = Trie_Node()
			prev.map[char] = T
			prev = T 
def print_trie(T):
	if len(T.map)>0:
		print(T.isunique, T.map.keys())
		for key in T.map.keys():
			print_trie(T.map[key])

def helper(word,T):
	unique_prefix = word[0]
	prev = T.map[word[0]]
	for i,char in enumerate(word[1:]):
		if i==0 and prev.isunique:
			return unique_prefix
		if prev.isunique:
			unique_prefix += char
			return unique_prefix
		else:
			unique_prefix += char
			prev = prev.map[char]
		
	return unique_prefix
def solve(arr):
	T = Trie_Node()
	for string in arr:
		insert(string,T)
	# print_trie(T)
	unique_prefixes = []
	for string in arr:
		unique_prefixes.append(helper(string,T))

	return unique_prefixes

if __name__=='__main__':
	arr = ['dog','cat','apple','apricot','fish','fissy','fixit','doggy']
	print(solve(arr))