#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
      long long n,rem,c=0;

      cin>>n;
      while(n!=0)
      {
           rem=n%10;
          if(rem==4||rem==6||rem==9||rem==8||rem==1){c=1;break;}
          n=n/10;
      }
      if(c==0){cout<<"YES"<<endl;}
      else{cout<<"NO"<<endl;}

    }
}
