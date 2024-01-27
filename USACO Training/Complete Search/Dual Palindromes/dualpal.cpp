/*
ID: khilfik1
LANG: C++
TASK: dualpal
*/
#include <iostream>
#include <fstream>
#include <unordered_map>
using namespace std;

unordered_map<int, string> n_base_map;

bool is_palindrome(string t)
{
  int lo = 0, hi = t.length() - 1;
  while (lo < hi)
  {
    if (t[lo] != t[hi])
      return false;
    lo += 1;
    hi -= 1;
  }
  return true;
}

string to_base_b(int num, int b)
{
  if (b == 10)
    return to_string(num);

  string out = "";
  while (num != 0)
  {
    out.insert(0, n_base_map[num % b]);
    num /= b;
  }
  return out;
}

int main()
{
    n_base_map = {
    {0, "0"},
    {1, "1"},
    {2, "2"},
    {3, "3"},
    {4, "4"},
    {5, "5"},
    {6, "6"},
    {7, "7"},
    {8, "8"},
    {9, "9"},
    {10, "A"},
    {11, "B"},
    {12, "C"},
    {13, "D"},
    {14, "E"},
    {15, "F"},
    {16, "G"},
    {17, "H"},
    {18, "I"},
    {19, "J"},
  };

  ifstream fileIn("dualpal.in");
  ofstream fileOut("dualpal.out");

  int N, S;
  fileIn >> N >> S;
  
  int b_found = 0;
  for (int n = S+1; n < 100000 && N != 0; n++)
  {
    for (int b = 2; b <= 10; b++)
    {
      string n_b = to_base_b(n, b);
      if (is_palindrome(n_b))
      {
        b_found += 1;
      }
      if (b_found == 2)
      {
        fileOut << n << endl;
        cout << n << endl;
        b_found = 0;
        N -= 1;
        break;
      }
    }
    b_found = 0;
  }
}