#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int a,b,c,d,k;
        cin>>a>>b>>c;
        d=b*b;
        k=4*a*c;
        if(d<k){cout<<"imaginary"<<endl;}
        else
        {
          cout<<"real"<<endl;

        }

    }
}
