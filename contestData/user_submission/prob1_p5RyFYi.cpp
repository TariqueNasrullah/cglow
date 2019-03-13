#include<bits/stdc++.h>
using namespace std;



typedef long long ll;
vector <ll>v;
int main()
{
   ll n;

   cin >> n;

   while(n--){

        ll a,target,c,n;
        cin >> a >> target;

        for(int i=0; i<a; i++){
        cin >> n;
        v.push_back(n);

        }

        if(v[target-1]%2 == 0) cout << "yes\n";
        else cout << "no\n";

        v.clear();


   }
   return 0;



}

