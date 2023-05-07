n=str(input())
vowels=['A','E','I','O','U','a','e','i','o','u']
nope=0
for i in n:
    if i not in vowels:
        nope+=1
    else:
        pass
if nope==0:
    print('Yes')
else:
    print('No')
