#include <iostream>
#include <cstring>
using namespace std;

int n, a, b;
const int MAX_N = 1005;
char g[MAX_N][MAX_N];
bool o[MAX_N][MAX_N];

// 1需要改, 0不需要, 2改上一个
int check(int i,int j) {
    if (i-b<0||j-a<0||g[i-b][j-a]=='W') {
        return 1;
    }
    if (g[i-b][j-a]=='B'||o[i-b][j-a]) {
        return 0;
    }
    if (g[i-b][j-a]=='G'&&o[i-b][j-a]) {
        return 0;
    }
    if (g[i-b][j-a]=='G'&&!o[i-b][j-a]) {
        return 2;
    }
}
void solve() {
    cin>>n>>a>>b;
    for (int i=0;i<n;i++) {
        string s;
        cin>>s;
        for (int j=0;j<=n;j++) {
            g[i][j]=s[j];
        }
    }
    memset(o, 0, sizeof(o));

    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            if (g[i][j]=='G'&&check(i, j))
                o[i][j]=true;
            if (g[i][j]=='B') {
                if (check(i,j)==1) {
                    cout<<-1<<endl;
                    return;
                }
                if (check(i,j)==2) {
                    o[i-b][j-a]=true;;
                    o[i][j]=true;
                }
                else o[i][j]=true;
            }
        }
    }
    int ans=0;
    for (int i=0;i<n;i++) for (int j=0;j<n;j++) ans += o[i][j];
    cout<<ans<<endl;
}
int main () {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t; cin>>t;
    while(t--) solve();
    return 0;
}