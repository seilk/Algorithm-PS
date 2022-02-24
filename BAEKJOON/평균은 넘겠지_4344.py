count=int(input())
score_list=[]

for _ in range (0,count):
  score_list=input().split()
  score_list=[int(i) for i in score_list]
  score_count=score_list[0]
  del score_list[0]

  average=sum(score_list)/score_count
  n=0
  for i in score_list:
    if i>average:
      n=n+1
    else:
      pass

  print(round(n/score_count*100,3),"%")