vow=['a','e','i','o','u','A','E','I','O','U']
# con=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
s=str(input())
v=0
c=0
for i in s:
    if i in vow:
        v+=1
    else:
        c+=1

print(v,c)
