def fatorial(n):
    if(n == 0 or n == 1):
        return 1
    elif(n > 1):
        return n * fatorial(n - 1)

print(fatorial(20))
