def reverseint(n):
    sign = n//abs(n)
    n = abs(n)
    return int(str(n)[::-1])*sign
n=int(input())
print(reverseint(n))
