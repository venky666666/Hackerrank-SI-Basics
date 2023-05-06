# mod=1000000007
n=int(input())
# n=n%mod
# def prime(n):
#     if n<=1:
#         print('No')
#     else:
#         for i in range(2,int((n)**(1/2))):
#             if n%i==0:
#                 return('No')
#             else:
#                 return('Yes')
# print(prime(n))

if n > 1:
    for i in range(2,int((n)**(1/2))):
        if (n % i) == 0:
            print("No")
            break
    else:
        print("Yes")
else:
    print("No")
