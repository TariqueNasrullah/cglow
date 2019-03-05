#include<bits/stdc++.h>
using namespace std;
#define ll long long
const int MX=1e5 +7;

void SegmentTree(ll Tree[], ll a[], int node, int Beg, int End)
{
    if(Beg==End){
        Tree[node]=a[Beg];
        return;
    }
    SegmentTree(Tree,a,node*2,Beg,(Beg+End)/2);
    SegmentTree(Tree,a,(node*2)+1,(Beg+End)/2+1,End);
    Tree[node]=Tree[2*node]+Tree[(2*node)+1];
}

ll Query(ll Tree[], int node, int b, int e, int l, int r)
{
    if(e<l || b>r)return 0;
    if(b>=l && e<=r){
        return Tree[node];
    }
    else {
        return Query(Tree, node*2,b,(b+e)/2,l,r)+Query(Tree,(node*2)+1,((b+e)/2)+1,e,l,r);
    }
}

int main()
{
    int n;
    cin>>n;
    ll a[n+5];
    ll Tree[MX];
    for(int i=1; i<=n; i++)cin>>a[i];
    SegmentTree(Tree,a,1,1,n);
    for(int i=1; i<=15; i++){
        cout<<Tree[i]<<" ";
    }
    cout<<endl;
    cout<<Query(Tree,1,1,8,1,1)<<endl;
}
