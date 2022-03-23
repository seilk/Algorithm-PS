import sys

In = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, In().split())


class Node:
	def __init__(self, key, data=None):
		self.key = key
		self.data = data
		self.children = {}


class Trie:
	def __init__(self):
		self.head = Node(None)

	def insert(self, word):
		cur_node = self.head
		for char in word:
			if char not in cur_node.children:
				cur_node.children[char] = Node(char)
			cur_node = cur_node.children[char]
		cur_node.data = word

	def search(self, word):
		cur_node = self.head
		for char in word:
			if char in cur_node.children:
				cur_node = cur_node.children[char]
			else:
				return False

		if cur_node.data:
			return True
		else:
			return False

	def start_with(self, prefix):
		cur_node = self.head

		for char in prefix:
			if char in cur_node.children:
				cur_node = cur_node.children[char]
			else:
				return None

		words = []
		next_node = []
		if cur_node.data: #app
			words.append(cur_node.data)
		next_node.extend(list(cur_node.children.values()))
		if len(next_node) == 0: return words

		cur_node = list(next_node)
		next_node = []
		while True:
			for node in cur_node:
				if node.data:
					words.append(node.data)
				next_node.extend(list(node.children.values()))
			if len(next_node) == 0: return words
			cur_node = list(next_node)
			next_node = []


if __name__ == "__main__":
	N, M = MIS()
	trie = Trie()
	for _ in range(N):
		trie.insert(In())

	ans = 0
	for _ in range(M):
		if trie.search(In()):
			ans += 1
	print(ans)