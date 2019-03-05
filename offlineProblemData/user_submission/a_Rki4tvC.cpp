#include <bits/stdc++.h>
#define ll long  long
using namespace std;

int main(){


    int q;

    cin >> q;

    while(q--) {


        string num;
        cin >> num;

        int len = num.size(), cnt = 0;
        for(int i = 0;i < len;i++) {

            if(num[i]=='2' || num[i] == '3' || num[i] == '5' || num[i] == '7') {

                cnt++;
            }


        }

        if(cnt == len) {

            cout << "YES" << endl;
        }
        else {

            cout << "NO" << endl;
        }
    }
    return 0;
}
