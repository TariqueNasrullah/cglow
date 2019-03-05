#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    ll n,u,v,c,m;
    cin>>n>>m;
    ll Warshalls[n+5][n+5];
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(i==j)Warshalls[i][j]=0;
            else Warshalls[i][j]=INT_MAX;
        }
    }
    for(int i=0; i<m; i++){
        cin>>u>>v>>c;
        Warshalls[u][v]=c;
    }

    for(int k=1; k<=n; k++){
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                if(i!=j || k!=i || k!=j)Warshalls[i][j]=min(Warshalls[i][j],Warshalls[i][k]+Warshalls[k][j]);
            }
        }
        cout<<endl;
        for(int ii=1; ii<=n; ii++){
            for(int jj=1; jj<=n; jj++){
                if(Warshalls[ii][jj]<INT_MAX)cout<<Warshalls[ii][jj]<<" ";
                else cout<<"# ";
            }
            cout<<endl;
        }
        cout<<endl;
    }
}
