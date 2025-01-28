#include <bits/stdc++.h>
using namespace std;

// 用于计算 arr 的前缀和
// prefix[i] = arr[0] + arr[1] + ... + arr[i-1]
vector<long long> prefixSums(const vector<int> &arr) {
    vector<long long> ps(arr.size() + 1, 0LL);
    long long sum = 0;
    for(int i = 0; i < (int)arr.size(); i++){
        sum += arr[i];
        ps[i+1] = sum;
    }
    return ps;
}

// 在前缀和 ps 上计算区间 [L, R] 的和
// 若 R < L 则返回 0
long long rangeSum(const vector<long long> &ps, int L, int R){
    if(R < L) return 0LL;
    return ps[R+1] - ps[L];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 读取输入
    int N; 
    cin >> N;
    vector<long long> a(N), b(N);
    for(int i = 0; i < N; i++){
        cin >> a[i];
    }
    for(int i = 0; i < N; i++){
        cin >> b[i];
    }

    // 计算 T1
    // 当 a[i] == b[i] 时，对应左侧区间与右侧区间的组合计数
    long long T1 = 0;
    for(int i = 0; i < N; i++){
        if(a[i] == b[i]){
            long long leftCount = (long long)i * (i + 1) / 2; 
            long long rightCount = (long long)(N - i - 1) * (N - i) / 2;
            T1 += leftCount + rightCount;
        }
    }

    // 将每个物种对应的下标 (1-based) 存储到 A_by_species, B_by_species
    // 其中下标+1 是为了与原 Python 代码逻辑保持一致
    vector<vector<int>> A_by_species(N+1), B_by_species(N+1);
    for(int i = 0; i < N; i++){
        A_by_species[a[i]].push_back(i + 1);
    }
    for(int i = 0; i < N; i++){
        B_by_species[b[i]].push_back(i + 1);
    }

    long long T2 = 0;

    // 遍历每一个可能的物种 s
    for(int s = 1; s <= N; s++){
        auto &A_list = A_by_species[s]; 
        auto &B_list = B_by_species[s];

        // 如果该物种在 a 或 b 中不存在，则跳过
        if(A_list.empty() || B_list.empty()) continue;

        // 排序位置索引
        sort(A_list.begin(), A_list.end());
        sort(B_list.begin(), B_list.end());

        // 前缀和，用于快速求部分区间之和
        auto psA = prefixSums(A_list);
        long long speciesSum = 0;
        int nA = (int)A_list.size();

        // 遍历 B_list 中每个位置 i_pos
        for(auto i_pos : B_list){
            // 计算 u = bisect_right(A_list, N - i_pos) - 1
            // 即在 A_list 中找出 > (N - i_pos) 的第一个下标，然后 -1
            {
                auto it = upper_bound(A_list.begin(), A_list.end(), N - i_pos);
                int u = (int)(it - A_list.begin()) - 1;
                if(u >= 0){
                    // 计算 t_prime = bisect_left(A_list, i_pos) - 1
                    auto it2 = lower_bound(A_list.begin(), A_list.end(), i_pos);
                    int t_prime = (int)(it2 - A_list.begin()) - 1;
                    if(t_prime > u) t_prime = u;

                    long long sum1 = 0;
                    if(t_prime < 0){
                        int count_ = u - 0 + 1;
                        sum1 = (long long)i_pos * count_;
                    } else {
                        long long sum_p = rangeSum(psA, 0, t_prime);
                        int count2 = u - (t_prime + 1) + 1;
                        sum1 = sum_p + (long long)i_pos * count2;
                    }
                    speciesSum += sum1;
                }

                int L = u + 1;
                // 若 L < nA，需要计算剩余部分
                if(L < nA){
                    int count_ = nA - L;
                    long long sumMax = 0;

                    // t_dblprime = bisect_left(A_list, i_pos) - 1
                    auto it3 = lower_bound(A_list.begin(), A_list.end(), i_pos);
                    int t_dblprime = (int)(it3 - A_list.begin()) - 1;

                    if(t_dblprime < L){
                        sumMax = rangeSum(psA, L, nA - 1);
                    } else {
                        if(t_dblprime >= nA - 1){
                            int cnt_temp = nA - L;
                            sumMax = (long long)i_pos * cnt_temp;
                        } else {
                            int cnt1 = t_dblprime - L + 1;
                            long long part1 = (long long)i_pos * cnt1;
                            long long part2 = rangeSum(psA, t_dblprime + 1, nA - 1);
                            sumMax = part1 + part2;
                        }
                    }
                    long long sum2 = (long long)count_ * (N + 1) - sumMax;
                    speciesSum += sum2;
                }
            }
        }
        T2 += speciesSum;
    }

    cout << T1 + T2 << "\n";
    return 0;
}
