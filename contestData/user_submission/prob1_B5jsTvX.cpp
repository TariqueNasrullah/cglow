#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
   ll n;

   cin >> n;

   while(n--){
        ll a,b,c;

        ll d;

        cin >> a >> b >> c;

        d = (b*b)-(4*a*c);

        if(d<0)


        cout << "imaginary\n";

        else
            cout << "real\n";

   }
   return 0;



}

