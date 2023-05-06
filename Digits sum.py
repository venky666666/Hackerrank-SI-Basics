number=int(input())
addition=0
modulo=0
while number!=0:
    modulo=number%10
    addition+=modulo
    number//=10
print(addition)
