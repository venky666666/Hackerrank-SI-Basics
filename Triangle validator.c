#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    long long  a,b,c,s1,s2,s3;
    scanf("%lld %lld %lld",&a,&b,&c);
    s1=a+b;
    s2=b+c;
    s3=a+c;
    if(s1>c && s2>a && s3>b)
        printf("Yes");
    else
        printf("No");
    
}
