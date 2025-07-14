def rekursi(n):
    if n == 1: # base case
        return 1
    else:
        return n * rekursi(n-1)


b = rekursi(4)
print(b)