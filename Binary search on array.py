n,k=map(int,input().split())
arr=list(map(int,input().split()))
lo=0
hi=n-1
# while lo<=hi:
#     mid=(lo+hi)
#     k=
#     if k==
    
def BS(arr,lo,hi,k): 
    if hi>=lo: 
        mid=lo+(hi-lo)//2
        if arr[mid]==k: 
            return mid 
        elif arr[mid]>k: 
            return BS(arr,lo,mid-1,k) 
        else: 
            return BS(arr,mid+1,hi,k) 
    else: 
        return -1
result=BS(arr,0,n-1,k) 

if result!=-1: 
    print("true") 
else: 
    print("false") 
