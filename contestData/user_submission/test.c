#include<stdio.h>
#include<string.h>
#define MAX 1000
char arr[MAX];
int main()
{
    int test,i,j,len;
    scanf("%d",&test);
    getchar();
    while(test--)
    {
        scanf("%s",&arr);
        len = strlen(arr);
        if(arr[len-1]=='5' && arr[len-2]=='3')
        {
            printf("-\n");
        }
        else if(arr[0]=='1' && arr[1]=='9' && arr[2]=='0')
        {
            printf("?\n");
        }
        else if(arr[0]=='9' && arr[len-1]=='4')
        {
            printf("*\n");
        }
        else if(arr[0]=='1' && len==1|| arr[0]=='4' && len==1 || arr[0]=='7'&& arr[1]=='8' && len==2)
        {
            printf("+\n");
        }
    }
}
