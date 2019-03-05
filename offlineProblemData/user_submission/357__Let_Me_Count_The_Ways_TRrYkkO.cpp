#include <bits/stdc++.h>
using namespace std;
#define lli long long int
int make;
int coins[] = {1, 5, 10, 25, 50};
lli dp[6][30000+1];

lli coin_change(int pos, int amount)
{
    if(pos >= 5)
    {
        if(amount == 0) return 1;
        else return 0;
    }

    if(dp[pos][amount] != -1)
        return dp[pos][amount];

    lli r1 = 0, r2 = 0;

    if(amount-coins[pos] >= 0) r1 = coin_change(pos, amount-coins[pos]);
    r2 = coin_change(pos+1, amount);

    return dp[pos][amount] = r1+r2;
}

int main()
{
    memset(dp, -1, sizeof(dp));
    //FILE *f;
    //ifstream in("in.txt");
    //f = fopen("out.txt", "a");
    while(scanf("%d", &make)==1)
    {
        lli ans = coin_change(0, make);
        if(ans > 1)
            printf("There are %lld ways to produce %d cents change.\n", ans, make);
        else
            printf("There is only 1 way to produce %d cents change.\n", make);
    }

    return 0;
}
