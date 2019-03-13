#include<stdio.h>
int main()
{
    int i,n,q;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
       {
           scanf("%d",&q);
    if(q%2==0)
        printf("NO\n");
    else
        printf("yes\n");
    }
}
