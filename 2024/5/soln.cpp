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

void solve(map<int, vector<int>> rules, vector<vector<int>> prints) {
  int ans = 0;
  for (vector<int> v : prints) {
    vector<int> seen;
    bool valid = true;
    for (int i = 0; i < v.size(); ++i) {
      if (rules.find(v[i]) == rules.end()) {
        seen.push_back(v[i]);
        continue;
      }
      vector<int> afters = rules[v[i]];
      for (int after : afters) {
        if (find(seen.begin(), seen.end(), after) != seen.end()) {
          valid = false;
          break;
        }
      }
      if (!valid) {
        break;
      }
      seen.push_back(v[i]);
    }
    if (valid) {
      int mid = v.size() / 2;
      if (v.size() == 0) {
        continue;
      }
      ans += v[mid];
    }
  }
  cout << ans << "\n";
}

int main() {
  int i = 0;
  ifstream myfile("input.txt");
  string line;
  map<int, vector<int>> rules;
  vector<vector<int>> prints;

  if (myfile.is_open()) {
    while (!myfile.eof()) {
      getline(myfile, line);
      if (line == "\n" || line == "") {
        break;
      }
      int idx = line.find("|");
      int n1 = stoi(line.substr(0, idx));
      int n2 = stoi(line.substr(idx + 1, line.length() - idx));
      rules[n1].push_back(n2);
      i++;
    }

    while (!myfile.eof()) {
      getline(myfile, line);
      stringstream linee(line);
      string numS;
      vector<int> v = {};
      while (getline(linee, numS, ',')) {
        v.push_back(stoi(numS));
      }
      prints.push_back(v);
    }
    myfile.close();
  }

  solve(rules, prints);
}
