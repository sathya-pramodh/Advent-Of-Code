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

int solve(vector<vector<int>> graph, int i, int j, int m, int n, int prev,
          vector<vector<int>> &visited) {
  if (graph[i][j] != prev + 1) {
    return 0;
  }
  if (graph[i][j] == 9 && prev == 8) {
    if (!visited[i][j]) {
      visited[i][j] = 1;
      return 1;
    }
    return 0;
  }
  vector<pair<int, int>> neighbors = pad4c(i, j, m, n, 1);
  int ans = 0;
  for (pair<int, int> pt : neighbors) {
    ans += solve(graph, pt.first, pt.second, m, n, prev + 1, visited);
  }
  return ans;
}

int main() {
  int i = 0;
  string line;
  ifstream myfile("input.txt");

  vector<vector<int>> graph;

  if (myfile.is_open()) {
    while (!myfile.eof()) {
      getline(myfile, line);
      // cout << line << endl;
      for (char c : line) {
        if (graph.size() < i + 1) {
          graph.push_back({});
        }
        graph[i].push_back(c - '0');
      }
      i++;
    }
    myfile.close();
  }

  int m = graph.size();
  int n = graph[0].size();

  int ans = 0;
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (graph[i][j] == 0) {
        vector<vector<int>> visited(m, vector<int>(n));
        ans += solve(graph, i, j, m, n, -1, visited);
      }
    }
  }
  cout << ans << "\n";
}
