list_my = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([arg for ind, arg in enumerate(list_my[1:]) if arg > list_my[ind]])
