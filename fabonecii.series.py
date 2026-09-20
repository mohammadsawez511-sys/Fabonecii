def fabo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        f =fabo(n-1)+fabo(n-2)
        return f
print("ANSWER :",fabo(10))    