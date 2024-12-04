#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> pad4c(int i, int j, int m, int n, int c) {
  vector<pair<int, int>> neigh = {};
  vector<pair<int, int>> d = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
  for (int cnt = 1; cnt <= c; ++cnt) {
    for (pair<int, int> dr : d) {
      int r = dr.first;
      int c = dr.second;
      if (i + r * cnt < 0 || i + r * cnt >= m || j + c * cnt < 0 ||
          j + c * cnt >= n)
        continue;
      neigh.push_back({i + r * cnt, j + c * cnt});
    }
  }
  return neigh;
}

vector<pair<int, int>> pad8c(int i, int j, int m, int n, int c) {
  vector<pair<int, int>> neigh = pad4c(i, j, m, n, c);
  vector<pair<int, int>> d = {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}};
  for (int cnt = 1; cnt <= c; ++cnt) {
    for (pair<int, int> dr : d) {
      int r = dr.first;
      int c = dr.second;
      if (i + r * cnt < 0 || i + r * cnt >= m || j + c * cnt < 0 ||
          j + c * cnt >= n)
        continue;
      neigh.push_back({i + r * cnt, j + c * cnt});
    }
  }
  return neigh;
}

int get_count(vector<vector<char>> v, int i, int j, int m, int n) {
  if (v[i][j] != 'A')
    return 0;

  if (i - 1 < 0 || i + 1 >= m || j - 1 < 0 || j + 1 >= n)
    return 0;

  char c1 = v[i - 1][j - 1];
  char c2 = v[i + 1][j - 1];
  char c3 = v[i - 1][j + 1];
  char c4 = v[i + 1][j + 1];
  if (c1 == 'M' && c2 == 'M' && c3 == 'S' && c4 == 'S') {
    return 1;
  }
  if (c1 == 'S' && c2 == 'S' && c3 == 'M' && c4 == 'M') {
    return 1;
  }
  if (c1 == 'S' && c2 == 'M' && c3 == 'S' && c4 == 'M') {
    return 1;
  }
  if (c1 == 'M' && c2 == 'S' && c3 == 'M' && c4 == 'S') {
    return 1;
  }
  return 0;
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
      for (char c : line) {
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
