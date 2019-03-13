#include<bits/stdc++.h>
using namespace std;



typedef long long ll;

ll func(char ch)
{
    if(ch == '2' || ch == '3' || ch == '5' || ch == '7'){
        return 1;
    }
    return 0;
}

int main()
{
   ll n,sum;

   cin >> n;

   while(n--){

      string  s1;

      cin >> s1;
      ll sz = s1.size();

      for(int i=0; i<sz; i++){
             sum = func(s1[i]);
            if(sum == 0) break;
      }

      if(sum == 1){
        cout << "YES\n";
      }
      else{
        cout << "NO\n";
      }



   }
   return 0;



}

