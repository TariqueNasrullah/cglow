#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    ll t;
    cin>>t;
    while(t--){
        ll n;
        cin>>n;
        ll x=1;
        if(n==90){
            cout<<4<<endl;
            continue;
        }
        else if(n>90){
            if(n==120)cout<<6<<endl;
            else cout<<180<<endl;
            continue;
        }
        if(180%n==0){
            cout<<180/n<<endl;
            continue;
        }
        while((n*x)%180)x++;
        cout<<x<<endl;
    }
}
