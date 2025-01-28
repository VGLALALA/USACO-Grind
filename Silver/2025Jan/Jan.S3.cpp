#include <bits/stdc++.h>
using namespace std;

static const int MAXN = 2005;

// 全局变量
int n;             // 矩阵大小
int pivotR, pivotC;  // 用于选择某行某列做参照
int matrixVal[MAXN][MAXN];  // 存储输入的矩阵
int answer[MAXN][MAXN];     // 最终输出的结果矩阵
int mappedVal[2 * MAXN];    // 映射表：对每个可能的值进行重新映射
int freqCount[2 * MAXN];    // freqCount[x] 表示值 x 在矩阵中出现的次数
vector<int> freqGroup[2 * MAXN]; // freqGroup[c] 存储“出现次数为 c”的所有值
vector<pair<int,int>> positions[2 * MAXN]; // positions[x] 存储值 x 出现过的所有 (行,列) 位置

// 验证当前 mappedVal 对矩阵的映射是否满足 “各行、各列均是连续区间” 的要求
bool isConsecutiveMapping() {
    // 检查每一行
    for(int row = 1; row <= n; row++){
        int minVal = INT_MAX, maxVal = INT_MIN;
        for(int col = 1; col <= n; col++){
            int val = mappedVal[ matrixVal[row][col] ];
            minVal = min(minVal, val);
            maxVal = max(maxVal, val);
        }
        // 若该行映射之后的最大值 - 最小值 != n-1，则说明无法构成连续区间
        if(maxVal - minVal != n - 1) return false;
    }
    // 检查每一列
    for(int col = 1; col <= n; col++){
        int minVal = INT_MAX, maxVal = INT_MIN;
        for(int row = 1; row <= n; row++){
            int val = mappedVal[ matrixVal[row][col] ];
            minVal = min(minVal, val);
            maxVal = max(maxVal, val);
        }
        if(maxVal - minVal != n - 1) return false;
    }
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;

    // 若 n=1，题意下直接输出 2 (仅需保证取值在[2..2])
    // 原代码写法是简单输出 2
    if(n == 1){
        cout << 2 << "\n";
        return 0;
    }

    // 读入矩阵，并记录每个值的出现次数、出现位置
    for(int row = 1; row <= n; row++){
        for(int col = 1; col <= n; col++){
            cin >> matrixVal[row][col];
            freqCount[ matrixVal[row][col] ]++;
            positions[ matrixVal[row][col] ].push_back({row, col});
        }
    }

    // freqGroup[c] 将存出现次数为 c 的所有值
    // 其中值的范围是 [2..2n] (一般题目条件)
    for(int val = 2; val <= 2 * n; val++){
        freqGroup[ freqCount[val] ].push_back(val);
    }

    // 从 freqGroup[1] 中选第二个值 freqGroup[1][1]，取其出现位置
    // 作为第一次尝试选的 pivotR, pivotC
    pivotR = positions[ freqGroup[1][1] ][0].first;
    pivotC = positions[ freqGroup[1][1] ][0].second;

    // 第一次给 mappedVal 赋值
    // 对 pivotR, pivotC 所在行、列的所有值做映射： mappedVal[x] = 2 + freqCount[x] - 1
    // 其余尚未映射的，后面统一处理
    for(int col = 1; col <= n; col++){
        int x = matrixVal[pivotR][col];
        mappedVal[x] = 2 + freqCount[x] - 1;
    }
    for(int row = 1; row <= n; row++){
        int x = matrixVal[row][pivotC];
        mappedVal[x] = 2 + freqCount[x] - 1;
    }

    // 剩余尚未映射的值，统一赋值为 (2n - freqCount[x] + 1)
    int notMappedCount = 0;
    for(int val = 2; val <= 2 * n; val++){
        if(!mappedVal[val]){
            mappedVal[val] = 2 * n - freqCount[val] + 1;
            notMappedCount++;
        }
    }
    // 若没有满足 n-1 个，则原代码的逻辑进入死循环(可能是特定实现)
    if(notMappedCount != n - 1){
        while(true) {}
    }

    // 若映射 valid，则先存到 answer
    if(isConsecutiveMapping()){
        for(int row = 1; row <= n; row++){
            for(int col = 1; col <= n; col++){
                answer[row][col] = mappedVal[ matrixVal[row][col] ];
            }
        }
    }

    // 清空 mappedVal 再进行第二次映射尝试
    memset(mappedVal, 0, sizeof(mappedVal));

    // 从 freqGroup[1][0] 中取位置
    pivotR = positions[ freqGroup[1][0] ][0].first;
    pivotC = positions[ freqGroup[1][0] ][0].second;

    // 同样方式给 mappedVal 赋值
    for(int col = 1; col <= n; col++){
        int x = matrixVal[pivotR][col];
        mappedVal[x] = 2 + freqCount[x] - 1;
    }
    for(int row = 1; row <= n; row++){
        int x = matrixVal[row][pivotC];
        mappedVal[x] = 2 + freqCount[x] - 1;
    }
    notMappedCount = 0;
    for(int val = 2; val <= 2 * n; val++){
        if(!mappedVal[val]){
            mappedVal[val] = 2 * n - freqCount[val] + 1;
            notMappedCount++;
        }
    }
    if(notMappedCount != n - 1){
        while(true) {}
    }

    // 若新映射也 valid，则与上一次存的 answer 比较行优先顺序
    if(isConsecutiveMapping()){
        int flag = 0; // 1 => 本次更优, -1 => 不如上次, 0 => 完全相同
        for(int row = 1; row <= n && flag == 0; row++){
            for(int col = 1; col <= n; col++){
                int newVal = mappedVal[ matrixVal[row][col] ];
                if(newVal < answer[row][col]){
                    flag = 1; // 新映射更优
                    break;
                }
                else if(newVal > answer[row][col]){
                    flag = -1; // 上一次更优
                    break;
                }
            }
        }
        // 若新映射更优，就更新 answer
        if(flag == 1){
            for(int row = 1; row <= n; row++){
                for(int col = 1; col <= n; col++){
                    answer[row][col] = mappedVal[ matrixVal[row][col] ];
                }
            }
        }
    }

    // 输出最终 answer
    for(int row = 1; row <= n; row++){
        for(int col = 1; col <= n; col++){
            cout << answer[row][col] << (col == n ? '\n' : ' ');
        }
    }

    return 0;
}
