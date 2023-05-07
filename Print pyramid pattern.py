r=int(input())
c=0
for i in range(1,r+1):
    for j in range(1,(r-i)+1):
        print(end=" ")
    while c!=(2*i-1):
        print("*",end="")
        c+=1
    c=0
    print()
