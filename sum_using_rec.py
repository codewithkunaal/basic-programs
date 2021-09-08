def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)
s = sum(3)
print(s)