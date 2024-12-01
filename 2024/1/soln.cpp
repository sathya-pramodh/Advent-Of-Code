#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
  priority_queue<int, vector<int>, greater<int>> fl, sl;
  int lines = 0;
  string line;
  ifstream myfile("input.txt");

  if (myfile.is_open()) {
    while (!myfile.eof()) {
      getline(myfile, line);
      // cout << line << endl;
      lines++;
    }
    myfile.close();
  }

  freopen("input.txt", "r", stdin);
  while (--lines) {
    int a, b;
    cin >> a >> b;
    fl.push(a);
    sl.push(b);
  }
  int cost = 0;
  while (fl.size()) {
    int a = fl.top();
    fl.pop();
    int b = sl.top();
    sl.pop();
    cost += abs(a - b);
  }
  cout << cost << "\n";
}
