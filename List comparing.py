def list_comparing():
    pass

list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_3 = []
comparing = set(list_1).intersection(list_2)
list_3.append(comparing)
print(sorted(list_3))



