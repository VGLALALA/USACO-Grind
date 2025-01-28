#include <bits/stdc++.h>
using namespace std;

// 如果想支持 N=7500，需要至少声明到 2*N+1=15001。
// 数组大小约为 15001 x 7501 ~= 1.125e8，存 short (2 字节) 时约占用 225 MB，仍然很大。
static const int MAXN = 7500;

// P[d][i] 用 short 存储前缀和：P[d][i] = ∑_{k=1..i} X_d(k)
// X_d(k) = 1 当 a[k] = b[d-k], 否则 0
static short P[15001][MAXN + 1];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; 
    cin >> N;
    vector<int> A(N+1), B(N+1);

    for(int i = 1; i <= N; i++){
        cin >> A[i];
    }
    for(int i = 1; i <= N; i++){
        cin >> B[i];
    }

    // 1. 计算初始匹配数 M，以及前缀和 Mprefix
    vector<int> m(N+1);
    for(int i = 1; i <= N; i++){
        m[i] = (A[i] == B[i]) ? 1 : 0;
    }
    vector<int> Mprefix(N+1, 0);
    for(int i = 1; i <= N; i++){
        Mprefix[i] = Mprefix[i-1] + m[i];
    }
    int M = Mprefix[N]; // 总的初始匹配数

    // 2. 构建 P[d][i] 的前缀和
    //    d 从 2 到 2N； i 从 1 到 N
    //    P[d][0] = 0，P[d][i] = P[d][i-1] + (A[i] == B[d-i] ? 1 : 0)
    for(int d = 2; d <= 2*N; d++){
        short runningSum = 0;
        for(int i = 1; i <= N; i++){
            int j = d - i;
            if(j >= 1 && j <= N && A[i] == B[j]){
                runningSum++;
            }
            P[d][i] = runningSum;
        }
    }

    // 3. 枚举 (l, r) 计算新匹配数：newMatches
    //    newMatches(l,r) = M - lostMatches + sumReversed
    //    其中 lostMatches = ∑_{i=l..r} [A[i] == B[i]]
    //         sumReversed = ∑_{i=l..r} [A[l+r-i] == B[i]]
    //    我们借助 P[d][·] 来在 O(1) 时间得到 sumReversed
    //    sumReversed = P[l+r][r] - P[l+r][l-1]
    //    lostMatches = Mprefix[r] - Mprefix[l-1]
    vector<long long> freq(N+1, 0LL);
    for(int l = 1; l <= N; l++){
        for(int r = l; r <= N; r++){
            short sumReversed = P[l+r][r] - P[l+r][l-1];
            int lostMatches = Mprefix[r] - Mprefix[l-1];
            int newMatches = M + sumReversed - lostMatches;
            freq[newMatches]++;
        }
    }

    // 4. 输出 freq[0..N]，即匹配数为 c 的翻转方案个数
    for(int c = 0; c <= N; c++){
        cout << freq[c] << "\n";
    }

    return 0;
}
