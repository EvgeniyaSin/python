lst = [1, 33, 7, 18, 7, 9, 11, -5, 0, 12, 32]
max_elem = lst[0]
for element in range(len(lst)):
  if lst[element] > max_elem:
    max_elem = lst[element]
    

print max_elem
