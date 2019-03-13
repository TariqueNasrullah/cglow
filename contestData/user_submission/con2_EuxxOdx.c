#include<stdio.h>
int main()
{
    int i,n,q;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
   {
       scanf("%d",&q);
    if(q%2==0)
        printf("YES\n");
    else
        printf("NO\n");
   }
}
