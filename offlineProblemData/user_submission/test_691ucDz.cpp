#include<bits/stdc++.h>
using namespace std;

int a[100];
int main()
{
//    freopen("in.txt", "r", stdin);
  //  freopen("out.txt", "w", stdout);

    int t;
    cin>>t;
    for(int i=1; i<=t; i++){
        int n,val;
        cin>>n>>val;
        int idx=-1;
        for(int j=1; j<=n; j++)cin>>a[j];
        for(int j=1; j<=n; j++){
            if(a[j]==val)idx=j;
        }
        if(idx & 1)cout<<"no"<<endl;
        else cout<<"yes"<<endl;

    }

    return 0;
}
