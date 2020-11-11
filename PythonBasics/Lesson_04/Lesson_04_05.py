from functools import reduce

print(reduce((lambda a, b: a*b), [ind for ind in range(100, 1000+1) if ind % 2 == 0]))
