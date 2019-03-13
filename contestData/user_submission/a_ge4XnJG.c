#include<stdio.h>
int main()
{
    int t,i,n,x,j,k;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d%d",&n,&x);
      int  a[n];
    for(j=0;j<n;j++)
    {
        scanf("%d",&a[j]);
    }
    for(k=0;k<n;k++)
    {
        if(a[k]==x){
            if(k%2==0)
            printf("no\n");

        else if(k%2!=0)
        printf("yes\n");

        }
    }
}
return 0;
}

