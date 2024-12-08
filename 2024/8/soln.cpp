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

int main() {
  int i = 0;
  string line;
  map<char, vector<pair<int, int>>> towers;
  ifstream myfile("input.txt");

  int n = 0;
  vector<vector<char>> graph;
  if (myfile.is_open()) {
    while (!myfile.eof()) {
      getline(myfile, line);
      // cout << line << endl;
      int j = 0;
      graph.push_back({});
      for (char c : line) {
        if (c == '.') {
          j++;
          graph[i].push_back(c);
          continue;
        }
        towers[c].push_back({i, j});
        graph[i].push_back(c);
        j++;
      }
      if (n == 0) {
        n = j;
      }
      i++;
    }
    myfile.close();
  }
  int ans = 0;
  int m = i - 1;
  vector<vector<bool>> visited(m, vector<bool>(n));
  for (pair<char, vector<pair<int, int>>> tower : towers) {
    char t = tower.first;
    vector<pair<int, int>> occ = tower.second;
    for (int i = 0; i < occ.size(); ++i) {
      for (int j = 0; j < occ.size(); ++j) {
        if (i == j) {
          continue;
        }
        pair<int, int> t1 = occ[i];
        pair<int, int> t2 = occ[j];
        int dx = t1.first - t2.first;
        int dy = t1.second - t2.second;
        int x1 = t1.first + dx;
        int y1 = t1.second + dy;
        if (x1 < 0 or x1 >= m or y1 < 0 or y1 >= n or visited[x1][y1]) {
          continue;
        }
        ans++;
        visited[x1][y1] = 1;
        graph[x1][y1] = '#';
      }
    }
  }
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      cout << graph[i][j];
    }
    cout << "\n";
  }
  cout << ans << " \n";
}
