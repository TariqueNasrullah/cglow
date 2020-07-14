#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ll n;
    scanf("%lld", &n);
    ll a = n;
    ll cnt = 0;
    ll val;
    char c;
    vector<char> v;
    while (n > 0)
    {
        ll d = n % 26;
        if (d == 0)
        {
            d = 96 + 26;
            c = d;
        }
        else
        {
            c = 96 + d;
        }
        v.push_back(c);
        if (n % 26 == 0)
        {
            n = n / 26 - 1;
        }
        else
        {
            n = n / 26;
        }
    }

    for (int i = v.size() - 1; i >= 0; i--)
    {
        printf("%c", v[i]);
    }
    printf("\n");
}