#include <bits/stdc++.h>
using namespace std;

int n, m;
int sum, mn;
int arr[1010];

bool is_possible(int mid)
{
    int _current_container_size = 0;
    int cnt = 1;

    for (int i = 0; i < n; i++)
    {
        _current_container_size += arr[i];
        if (_current_container_size > mid)
        {
            _current_container_size = arr[i];
            cnt++;
        }
    }

    if (cnt > m)
        return false;
    else
        return true;
}

int get_res(int l, int r)
{
    int ans = 0;

    while (l <= r)
    {
        int mid = (l + r) / 2;

        if (is_possible(mid))
        {
            r = mid - 1;
            ans = mid;
        }
        else
        {
            l = mid + 1;
        }
    }

    return ans;
}

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);

    for (int tc = 1; tc <= t; tc++)
    {
        scanf("%d %d", &n, &m);

        sum = 0;
        mn = 0;

        for (int i = 0; i < n; i++)
        {
            scanf("%d", &arr[i]);

            sum += arr[i];

            mn = max(arr[i], mn);
        }

        int ans = get_res(mn, sum);

        printf("Case %d: %d\n", tc, ans);
    }
}