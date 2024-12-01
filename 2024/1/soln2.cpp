#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
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

  map<int, int> freq;
  vector<int> fl;
  freopen("input.txt", "r", stdin);
  while (--lines) {
    int a, b;
    cin >> a >> b;
    freq[b]++;
    fl.push_back(a);
  }
  ll similarity = 0;
  for (int i = 0; i < fl.size(); ++i) {
    similarity += (ll)fl[i] * freq[fl[i]];
  }
  cout << similarity << "\n";
}
