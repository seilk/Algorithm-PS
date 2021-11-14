import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()


nodes = int(input())
graph = dict()
for i in range(nodes):
    node, left, right = input().split()
    if left == ".":
        left = None
    if right == ".":
        right = None
    graph[node] = [left, right]


def preorder(root, graph):
    left, right = graph[root]
    print(root, end="")
    if left != None:
        preorder(left, graph)
    if right != None:
        preorder(right, graph)


def inorder(root, graph):
    left, right = graph[root]
    if left != None:
        inorder(left, graph)
    print(root, end="")
    if right != None:
        inorder(right, graph)


def postorder(root, graph):
    left, right = graph[root]
    if left != None:
        postorder(left, graph)
    if right != None:
        postorder(right, graph)
    print(root, end="")


def orders(i, graph):
    if i == 0:
        preorder("A", graph)
    if i == 1:
        inorder("A", graph)
    if i == 2:
        postorder("A", graph)
    print()


for i in range(3):
    orders(i, graph)
