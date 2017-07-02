lst = [1, 33, 7, 18, 7, 9, 11, -5, 0, 12, 32]
min_elem = lst[0]
for element in range(len(lst)):
  if lst[element] < min_elem:
    min_elem = lst[element]

print min_elem
