L = [1,2,3, 'toto', 8, True]  

print(L[0])   # 1

print(L[4])  # 8

print(len(L))  # 6

print(L[len(L)])  # ERROR! TypeError: 'str' object does not support item assignment

print(L[3][1])  # o

L[5] = False  # Replaces True with False in index 5 in the List 'L' = [1, 2, 3, 'toto', 8, False]

L[3][0] = 'T' # ERROR! TypeError: 'str' object does not support item assignment

