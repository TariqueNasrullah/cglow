
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
       int a,b,c=0;
       cin>>a>>b;
       int ac[n+1];
       for(int i=1;i<=n;i++)
       {
           cin>>ac[i];

       }
       for(int i=1;i<=n;i++)
       {
       if(ac[i]==b&&i%2==0){cout<<"yes"<<endl;c=1;break;}
       }
      if(c==0){cout<<"no"<<endl;}
    }
    return 0;
}
