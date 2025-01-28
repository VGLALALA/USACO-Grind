#include <iostream>
#include <vector>

using namespace std;

int main(){

    int N;
    cin >> N;
    vector<int> arr(N);
    for(int i = 0; i < N; i++){
        cin >> arr[i];
    }

    vector<int> lo(N + 1, -1);  
    vector<int> pd(N + 1, 0);
    int dc = 0;

    for(int i = 0; i < N; i++){
        int val = arr[i];
        if(lo[val] == -1) {
            dc++;
        }
        pd[i + 1] = dc;
        lo[val] = i;
    }

    vector<vector<int> > p(N + 1);
    for(int i = 0; i < N; i++){
        p[arr[i]].push_back(i);
    }

    long long ans = 0; 
    for(int y = 1; y <= N; y++){
        const auto &occ = p[y];
        int k = (int)occ.size();
        if(k < 2) {
            continue;
        }

        int ST = occ[k - 2];  
        long long tol_d = pd[ ST ]; 

        if(occ[0] < ST){
            tol_d--; 
        }

        if(tol_d < 0){
            tol_d = 0;
        }

        ans += tol_d;
    }

    cout << ans << "\n";
    return 0;
}
