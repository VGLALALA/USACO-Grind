#include <bits/stdc++.h>
using namespace std;

class FenwickTree {
public:
	FenwickTree(int n) : n(n), tree(n + 1, 0) {}
	
	void update(int i, int v) {
		while (i <= n) {
			tree[i] += v;
			i += i & -i;
		}
	}
	
	int sum(int i) {
		int s = 0;
		while (i > 0) {
			s += tree[i];
			i -= i & -i;
		}
		return s;
	}
	
	int rangeSum(int l, int r) {
		return sum(r) - sum(l - 1);
	}
	
	int findKth(int k) {
		int pos = 0, bitMask = 1 << (__lg(n));
		while (bitMask > 0) {
			int next = pos + bitMask;
			if (next <= n && tree[next] < k) {
				k -= tree[next];
				pos = next;
			}
			bitMask >>= 1;
		}
		return pos + 1;
	}
	
private:
	int n;
	vector<int> tree;
};

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int T;
	cin >> T;
	
	while (T--) {
		int N, K;
		cin >> N >> K;
		
		vector<int> trees(N);
		for (int i = 0; i < N; i++) cin >> trees[i];
		
		vector<tuple<int, int, int>> intervals(K);
		for (int i = 0; i < K; i++) {
			int l, r, t;
			cin >> l >> r >> t;
			intervals[i] = {l, r, t};
		}
		
		sort(trees.begin(), trees.end());
		sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
			return get<1>(a) < get<1>(b);
		});
		
		FenwickTree fenw(N);
		for (int i = 1; i <= N; i++) fenw.update(i, 1);
		
		auto idxLowerBound = [&](int val) {
			return lower_bound(trees.begin(), trees.end(), val) - trees.begin();
		};
		
		auto idxUpperBound = [&](int val) {
			return upper_bound(trees.begin(), trees.end(), val) - trees.begin() - 1;
		};
		
		int chosenCount = 0;
		
		for (const auto& [l, r, t] : intervals) {
			int leftIdx = idxLowerBound(l);
			int rightIdx = idxUpperBound(r);
			if (leftIdx > rightIdx || leftIdx < 0 || rightIdx < 0 || leftIdx >= N || rightIdx >= N) continue;
			
			int totalInInterval = rightIdx - leftIdx + 1;
			int availableInInterval = fenw.rangeSum(leftIdx + 1, rightIdx + 1);
			int chosenInInterval = totalInInterval - availableInInterval;
			
			int need = t - chosenInInterval;
			
			while (need > 0) {
				int sumR = fenw.sum(rightIdx + 1);
				int chosenIdx = fenw.findKth(sumR) - 1;
				fenw.update(chosenIdx + 1, -1);
				chosenCount++;
				need--;
			}
		}
		
		int result = N - chosenCount;
		cout << result << "\n";
	}
	
	return 0;
}

