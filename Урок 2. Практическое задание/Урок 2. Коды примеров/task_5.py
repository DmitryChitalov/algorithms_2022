from sys import getrecursionlimit, setrecursionlimit

print(getrecursionlimit())
setrecursionlimit(10000)
print(getrecursionlimit())
