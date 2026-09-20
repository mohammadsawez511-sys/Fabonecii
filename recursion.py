def fact(n):
    if n == 1:
        return 1
    else:
        f = n * fact(n-1)
        return f
print(fact(5))
