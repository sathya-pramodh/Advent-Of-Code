#include<bits/stdc++.h>
using namespace std;

int get_count(vector<vector<char>> v, int i, int j, int m, int n) {
	vector<vector<int>> d = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {-1, -1}, {-1, 1}, {1, -1}};
	int ans = 0;
	for (vector<int> p: d) {
		int r = p[0];
		int c = p[1];
		string next = "XMAS";
		int mul = 0;
		for (mul = 0; mul <= 3; ++mul) {
			if (i + r*mul >= m || j + c*mul >= n || i + r*mul < 0 || j + c*mul < 0) {
				break;
			}
			char chr = v[i + r*mul][j + c*mul];
			if (chr != next[mul]) {
				break;
			}
		}
		if (mul == 4) {
			cout << v[i][j] << "\n";
			ans++;
		}
	}
	return ans;
}

int main() {
	vector<vector<char>> v;
	int i = 0;
	string line;
	ifstream myfile("input.txt");

	if (myfile.is_open()) {
	  while (!myfile.eof()) {
	    getline(myfile, line);
	    // cout << line << endl;
	    v.push_back({});
	    for (char c: line) {
		v[i].push_back(c);
	    }
	    i++;
	  }
	  myfile.close();
	}
	int m = i;
	int n = v[0].size();
	
	int ans = 0;
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			ans += get_count(v, i, j, m, n);
		}
	}
	cout << ans << "\n";
}
