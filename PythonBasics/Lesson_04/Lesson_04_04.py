list_my = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([arg for ind, arg in enumerate(list_my) if arg not in list_my[:ind] + list_my[ind+1:]])
