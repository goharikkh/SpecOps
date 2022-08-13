lst = [1, 2, 2, 3, 3, 3, 4, 4, 5]
dup = {}
unique_lst = set(lst)
for i in unique_lst:
    dup[i] = lst.count(i)
print(dup)    
