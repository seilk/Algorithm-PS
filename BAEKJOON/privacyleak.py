lst = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]
lst3 = [0]
lst4 = lst2
lst2.append(1)
print(lst3) # privacy leack 발생 안함
print(lst4) # privacy leak 발생