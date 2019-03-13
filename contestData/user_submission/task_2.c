/*prime num*/
#include<stdio.h>
main()
{
    int q,i;
    scanf("%d",q);
        if((q%2==0)&&(q%3==0)&&(q%4==0)&&(q%5==0)&&(q%6==0)&&(q%7==0)&&(q%8==0)&&(q%9==0))
        printf("no");
    else
        printf("yes");

    return 0 ;
}
