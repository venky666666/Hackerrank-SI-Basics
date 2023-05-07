n=int(input())
for i in range(1,n+1):
    for k in range(1,i+1):
        print(chr(k+65-1),end=' ')
    for l in range(i-1,0,-1):
        print(chr(l+65-1),end=' ')
    print()
