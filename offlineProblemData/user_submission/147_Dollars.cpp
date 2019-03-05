#include <bits/stdc++.h>
using namespace std;
#define lli long long int

int make;
lli coins[] = {100, 200, 500, 1000, 2000, 5000, 10000, 5, 10, 20, 50};
lli dp[12][300*100+1];

lli coin_change(int pos, int amount)
{
    if(pos >= 11)
    {
        if(amount == 0) return 1;
        else return 0;
    }

    if(dp[pos][amount] != -1) return dp[pos][amount];

    lli r1 = 0, r2 = 0;

    if(amount-coins[pos] >= 0) r1 = coin_change(pos, amount-coins[pos]);

    r2 = coin_change(pos+1, amount);

    return dp[pos][amount] = r1+r2;
}

int main()
{
    //FILE *f ;
    //f = fopen("out.txt", "a");
    //ifstream in("in.txt");
    float a;
    memset(dp, -1, sizeof(dp));

    while(scanf("%f", &a))
    {
        if(a == 0.0)
            return 0;
        make =  static_cast<int>(a*100);
        if(make%5 != 0)
            make++;

        printf("%6.2lf%17lld\n", a, coin_change(0, make));
    }

    return 0;
}
