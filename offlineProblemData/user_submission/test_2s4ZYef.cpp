

    #include <bits/stdc++.h>
    using namespace std;
    int a[100];
    int main()
    {
        int t;
        cin >> t;
        while(t--){
            int n, val;
            cin >> n >> val;
            for(int i = 1; i <= n; i++)
                cin >> a[i];
            int idx = -1;
            for(int i = 1; i <= n; i++)
                if(a[i] == val)
                    idx = i;
            if(idx & 1)
                cout << "no" << endl;
            else
                cout << "yes" << endl;
        }
        return 0;
    }

