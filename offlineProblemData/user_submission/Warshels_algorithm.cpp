#include<bits/stdc++.h>
using namespace std;
#define ll long long

#define pii pair<ll,ll>

vector<pii>tree[300004];
vector<pii>:: iterator it;

int main()
{
    ll n,u,v,c;
    cin>>n;
    ll w[n+5];
    for(int i=0; i<n; i++)cin>>w[i];
    for(int i=0; i<n-1; i++){
        cin>>u>>v>>c;
        tree[u].push_back(make_pair(v,c));
        tree[v].push_back(make_pair(u,c));
    }
    for(int i=1; i<=n; i++){
        cout<<i<<endl;
        for(it=tree[i].begin(); it!=tree[i].end(); it++){
            cout<<it->first<<" "<<it->second<<endl;
        }
    }
}
