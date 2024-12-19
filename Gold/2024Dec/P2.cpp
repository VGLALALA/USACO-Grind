#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 1.01e6;
const int MOD = 1000000007;

int N;
int red_prefix[MAX_N], blue_prefix[MAX_N], dp[MAX_N], dp_sum[MAX_N][2];
char color_preferences[MAX_N];
set<int> blue_positions, red_positions;

int find_previous_blue(int x) {
    auto it = blue_positions.lower_bound(x);
    --it;
    return *it;
}

int main() {
    cin >> N;
    scanf("%s", color_preferences + 1);

    for (int i = 1; i <= N; i++) {
        red_prefix[i] = red_prefix[i - 1];
        blue_prefix[i] = blue_prefix[i - 1];
        
        if (color_preferences[i] == 'R') {
            ++red_prefix[i];
            red_positions.insert(i);
        }
        if (color_preferences[i] == 'B') {
            ++blue_prefix[i];
            blue_positions.insert(i);
        }
    }

    blue_positions.insert(N + 1);
    blue_positions.insert(0);
    red_positions.insert(N + 1);
    red_positions.insert(0);

    dp[0] = dp_sum[0][0] = 1;

    for (int i = 1; i <= N; i++) {
        if (color_preferences[i] == 'X') dp[i] = dp[i - 1];
        
        int length = 1;
        while (true) {
            while (length * 2 <= i && find_previous_blue(i - length + 1) >= i - length * 2 + 1) {
                auto it = blue_positions.lower_bound(i - length * 2 + 1);
                length = i - (*it) + 1;
            }
            
            if (length * 2 > i || red_prefix[i] - red_prefix[i - length] > 0) break;
            
            int previous_position = find_previous_blue(i - length);
            auto it = red_positions.lower_bound(i - length + 1);
            --it;
            previous_position = max(previous_position, i - (i - *it + 1) * 2 + 1);
            
            (dp[i] += (dp_sum[i - length * 2][i & 1] - (previous_position ? dp_sum[previous_position - 1][i & 1] : 0))) %= MOD;
            (dp[i] += MOD) %= MOD;
            
            length = (i - previous_position + 1) / 2;
            if (i - length * 2 + 1 > previous_position) ++length;
        }
        
        dp_sum[i][0] = dp_sum[i - 1][0];
        dp_sum[i][1] = dp_sum[i - 1][1];
        (dp_sum[i][i & 1] += dp[i]) %= MOD;
    }
    
    printf("%d\n", dp[N]);
    return 0;
}
