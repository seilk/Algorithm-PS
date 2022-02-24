import sys
sys.setrecursionlimit(10**5)
def find(node,idx):
  if node==1:
    if gate_check[node]>0:
      return -1
    gate_check[1]=idx
    return node
  if gate_check[node]==-1:
    gate_check[node]=idx
    return node
  gate[node]=find(gate[node],idx)
  return gate[node]

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda :map(int, In().split())
G=int(In())
P=int(In())
gate=[i-1 for i in range(G+1)]
gate_check=[-1]*(G+1)
tot=0
for idx in range(1,P+1):
  node=int(In())
  if find(node, idx)<0:
    break
  tot+=1
print(tot)