#include<stdio.h>

int main()
{
    int Q,t,a,b,c;

    scanf("%d",&Q);

    for (t=1;t<=Q;t++){

            scanf("%d %d %d",&a,&b,&c);

    int d = b*b -4*a*c;

    if (d>=0){

        printf("real\n");

    }

    else
        printf("imaginary\n");


    }



    return 0;
}
