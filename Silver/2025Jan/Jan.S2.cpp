#include <bits/stdc++.h>
using namespace std;

/*
  给定一个数组 a[0..N-1]，每个元素非负，给定模数 M。
  要找 min_{x} (sum_{i} cost_i)，其中 cost_i 是把 a[i] 调整到满足 (a[i] - x) % M = 0 所需的操作数。
  等价于：令 r[i] = a[i] % M，然后令 r[i] -> R (同一个余数)，花费 = circular_dist(r[i], R)。
  在圆周 [0..M) 上找一点 R，使 sum_{i} dist(r[i], R) 最小。
*/

static const long long INF = LLONG_MAX;

// 计算前缀和 prefixSum 用于快速区间求和
vector<long long> buildPrefix(const vector<long long> &arr){
    int n = (int)arr.size();
    vector<long long> ps(n+1, 0LL);
    for(int i=0; i<n; i++){
        ps[i+1] = ps[i] + arr[i];
    }
    return ps;
}

// 区间 [L,R] 的和
long long rangeSum(const vector<long long> &ps, int L, int R){
    if(R < L) return 0;
    return ps[R+1] - ps[L];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; // 测试用例数量
    cin >> T;
    while(T--){
        int N;
        long long M;
        cin >> N >> M;

        vector<long long> a(N);
        for(int i=0; i<N; i++){
            cin >> a[i];
        }

        // 1) 求所有 a[i] 的余数
        // 如果 M=1，所有数 mod 1 = 0，代价就是 0，直接输出 0
        if(M == 1){
            cout << 0 << "\n";
            continue;
        }
        vector<long long> r(N);
        for(int i=0; i<N; i++){
            r[i] = a[i] % M; 
        }
        // 2) 排序 r
        sort(r.begin(), r.end());

        // 3) 若所有 r 都相同 => 代价 0
        // 也可以在后面滑窗一起处理，这里可以省一下时间
        // 先不做此简化

        // 4) 将序列 "倍增"：v[i] = r[i], v[i+N] = r[i]+M
        // 这样就可以在 [0..2N-1] 中用滑窗长为 M
        vector<long long> v(2*N);
        for(int i=0; i<N; i++){
            v[i] = r[i];
            v[i+N] = r[i] + M; 
        }

        // 5) 准备 prefix sum 来快速计算子区间和
        //   因为求区间 [i..j] 中的 v[k] sum
        //   以及分段距离运算
        vector<long long> ps = buildPrefix(v);

        // ans 记录最小代价
        long long ans = LLONG_MAX;

        // 双指针 j，表示在 v[i] 的起点下，找最大 j s.t. v[j] < v[i] + M
        // dist = 对区间 [i.. j] 计算 "圆周距离" 之和
        // 在这区间内 diff_k = v[k] - v[i] < M
        // cost_k = (diff_k <= M/2)? diff_k : M - diff_k
        // 要先二分 mid：mid = 最大 p s.t. v[p] - v[i] <= M/2
        // then cost = sum_{k=i..mid} (v[k] - v[i]) + sum_{k=mid+1..j} (M - (v[k] - v[i]))

        int j = 0;
        for(int i=0; i<N; i++){
            while(j < 2*N && v[j] < v[i] + M){
                j++;
            }
            // 区间 [i.. j-1] 长度 <= N
            // 找 mid = 最大 p in [i.. j-1] with v[p] - v[i] <= M/2
            // => use binary search
            long long limitVal = v[i] + M/2; 
            int midPos = int( upper_bound(v.begin()+i, v.begin()+j, limitVal) - v.begin() ) - 1;

            // midPos 范围 [i-1.. j-1]
            if(midPos < i) midPos = i; // case M/2 < 0 => not possible
            if(midPos >= j) midPos = j-1;

            // cost = sum_{k=i..midPos}(v[k] - v[i]) + sum_{k=midPos+1.. j-1}(M - (v[k] - v[i]))
            // => first part:
            long long sumLeft = rangeSum(ps, i, midPos);
            long long countLeft = (midPos - i + 1);
            long long costLeft = sumLeft - countLeft*v[i]; 
            // second part:
            long long sumRight = rangeSum(ps, midPos+1, j-1);
            long long countRight = (j-1 - (midPos+1) + 1);
            // sum_{k=midPos+1..j-1}( M - (v[k] - v[i]) )
            // = countRight * M - [ sumRight - (countRight)*v[i] ]
            long long costRight = countRight*M - ( sumRight - countRight*v[i] );

            long long totalCost = costLeft + costRight;
            ans = min(ans, totalCost);
        }

        // 输出最小代价
        cout << ans << "\n";
    }

    return 0;
}
