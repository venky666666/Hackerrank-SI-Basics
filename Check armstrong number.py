n=str(input())
cube=0
for i in n:
    cube+=(int(i))**3
#print(cube)
if cube==int(n):
    print('Yes')
else:
    print('No')
