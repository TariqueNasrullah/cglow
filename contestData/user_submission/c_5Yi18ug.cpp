#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,a,b,c,sum,s;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        cin>>a>>b>>c;

        sum=(b*b)-(4*a*c);

        if(sum<0) cout<<"imaginary"<<endl;
        else cout<<"real"<<endl;
    }
    return 0;
}

