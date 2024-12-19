#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		vector<int> a(n);
		for (int i = 0; i < n; ++i) cin >> a[i];
		int need = n / 2 - 1;
		long long ans = 0;
		for (int i = 0; i < need; ++i) ans += a[i];
		long long cur = ans;
		for (int i = 0; i < need; ++i) {
			cur += a[n - 1 - i];
			cur -= a[need - 1 - i];
			ans = max(ans, cur);
		}
		long long total_sum = 0;
		for (int i = 0; i < n; ++i) total_sum += a[i];
		cout << total_sum - ans << " " << ans << endl;
	}
	return 0;
}

