#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
long long num,n,rem=0,cube=0,sum=0;
    scanf("%lld",&num);
    n=num;
    while(n!=0)
    {
        rem=n%10;
        cube=rem*rem*rem;
        sum=sum+cube;
        n=n/10;
    }
    if(sum==num)
    {
        printf("Yes");        
    }
    else
        printf("No");   
}
