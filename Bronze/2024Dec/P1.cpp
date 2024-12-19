#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	// Read input
	int T;
	cin >> T;
	vector<int> queries(T);
	for(int &x: queries) {
		cin >> x;
	}

	// Precompute valid ranges
	vector<pair<int,int>> ranges;
	for(int len = 2; len <= 9; len++) {
		// Build lower bound (45, 445, 4445, etc)
		string low;
		for(int i = 0; i < len-1; i++) {
			low += '4';
		}
		low += '5';
		
		// Build upper bound (49, 499, 4999, etc) 
		string high = "4";
		for(int i = 0; i < len-1; i++) {
			high += '9';
		}
		
		ranges.emplace_back(stoi(low), stoi(high));
	}

	// Process each query
	for(int query: queries) {
		if(query < 2) {
			cout << "0\n";
			continue;
		}

		long long ans = 0;
		for(auto &[start, end]: ranges) {
			if(start > query) continue;
			
			int validEnd = min(end, query);
			if(validEnd >= start) {
				ans += (long long)(validEnd - start + 1);
			}
		}
		cout << ans << "\n";
	}
}