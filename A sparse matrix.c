#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int i,j,m,n,count=0;
    long long a[100][100];
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
     for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i][j]==0)
            {
                count=count+1;
            }
        }
    }
   int d=(n*m)/2;
    if(count>d)
        printf("Yes");
    else
        printf("No");
}
