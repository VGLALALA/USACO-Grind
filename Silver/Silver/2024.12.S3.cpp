#include <iostream>
#include <vector>
#include <deque>
#include <tuple>

using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	
	vector<vector<char>> a(n, vector<char>(n, 0));
	deque<pair<int, int>> q;
	vector<tuple<int, int, char>> c;
	
	for (int i = 0; i < k; ++i) {
		int x, y;
		char t;
		cin >> x >> y >> t;
		--x; --y;
		a[x][y] = t;
		c.emplace_back(x, y, t);
	}
	
	vector<int> ans(k, 0);
	int cur = n * n;
	vector<vector<int>> b(n, vector<int>(n, 0)); 
	
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if ((i == 0 || j == 0 || i == n - 1 || j == n - 1)) {
				if (a[i][j] == 0) {
					q.emplace_back(i, j);
					b[i][j] = 1;
					cur--;
				}
				if (i == 0 && a[i][j] == 'U') {
					q.emplace_back(i, j);
					b[i][j] = 1;
					cur--;
				}
				if (j == 0 && a[i][j] == 'L') {
					q.emplace_back(i, j);
					b[i][j] = 1;
					cur--;
				}
				if (i == n - 1 && a[i][j] == 'D') {
					q.emplace_back(i, j);
					b[i][j] = 1;
					cur--;
				}
				if (j == n - 1 && a[i][j] == 'R') {
					q.emplace_back(i, j);
					b[i][j] = 1;
					cur--;
				}
			}
		}
	}
	
	while (!q.empty()) {
		auto [x, y] = q.front();
		q.pop_front();
		
		if (x - 1 >= 0 && (a[x - 1][y] == 'D' || a[x - 1][y] == 0) && b[x - 1][y] == 0) {
			b[x - 1][y] = 1;
			q.emplace_front(x - 1, y);
			cur--;
		}
		if (x + 1 < n && (a[x + 1][y] == 'U' || a[x + 1][y] == 0) && b[x + 1][y] == 0) {
			b[x + 1][y] = 1;
			q.emplace_front(x + 1, y);
			cur--;
		}
		if (y - 1 >= 0 && (a[x][y - 1] == 'R' || a[x][y - 1] == 0) && b[x][y - 1] == 0) {
			b[x][y - 1] = 1;
			q.emplace_front(x, y - 1);
			cur--;
		}
		if (y + 1 < n && (a[x][y + 1] == 'L' || a[x][y + 1] == 0) && b[x][y + 1] == 0) {
			b[x][y + 1] = 1;
			q.emplace_front(x, y + 1);
			cur--;
		}
	}
	
	ans[k - 1] = cur;
	
	for (int z = k - 2; z >= 0; --z) {
		auto [i, j, t] = c[z + 1];
		if (i == 0 && a[i][j] != 'U' && b[i][j] != 1) {
			q.emplace_back(i, j);
			b[i][j] = 1;
			cur--;
		} else if (j == 0 && a[i][j] != 'L' && b[i][j] != 1) {
			q.emplace_back(i, j);
			b[i][j] = 1;
			cur--;
		} else if (i == n - 1 && a[i][j] != 'D' && b[i][j] != 1) {
			q.emplace_back(i, j);
			b[i][j] = 1;
			cur--;
		} else if (j == n - 1 && a[i][j] != 'R' && b[i][j] != 1) {
			q.emplace_back(i, j);
			b[i][j] = 1;
			cur--;
		}
		
		if (b[i][j] == 0) {
			for (auto [di, dj] : vector<pair<int, int>>{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}) {
				if (i + di >= 0 && i + di < n && j + dj >= 0 && j + dj < n &&
					b[i][j] == 0 && b[i + di][j + dj] == 1) {
					q.emplace_back(i, j);
					b[i][j] = 1;
					cur--;
				}
			}
		}
		
		a[i][j] = 0;
		
		while (!q.empty()) {
			auto [x, y] = q.front();
			q.pop_front();
			
			if (x - 1 >= 0 && (a[x - 1][y] == 'D' || a[x - 1][y] == 0) && b[x - 1][y] == 0) {
				b[x - 1][y] = 1;
				q.emplace_front(x - 1, y);
				cur--;
			}
			if (x + 1 < n && (a[x + 1][y] == 'U' || a[x + 1][y] == 0) && b[x + 1][y] == 0) {
				b[x + 1][y] = 1;
				q.emplace_front(x + 1, y);
				cur--;
			}
			if (y - 1 >= 0 && (a[x][y - 1] == 'R' || a[x][y - 1] == 0) && b[x][y - 1] == 0) {
				b[x][y - 1] = 1;
				q.emplace_front(x, y - 1);
				cur--;
			}
			if (y + 1 < n && (a[x][y + 1] == 'L' || a[x][y + 1] == 0) && b[x][y + 1] == 0) {
				b[x][y + 1] = 1;
				q.emplace_front(x, y + 1);
				cur--;
			}
		}
		
		ans[z] = cur;
	}
	
	for (int x : ans) {
		cout << x << endl;
	}
	
	return 0;
}

