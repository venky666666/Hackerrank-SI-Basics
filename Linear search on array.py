n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
c=0
for i in arr:
    if i==k :
        print(arr.index(i))
        c+=1
if c==0:
    print(-1)
