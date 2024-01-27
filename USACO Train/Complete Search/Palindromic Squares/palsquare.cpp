/*
ID: khilfik1
LANG: C++
TASK: palsquare
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

  ifstream fileIn("palsquare.in");
  ofstream fileOut("palsquare.out");
  int B;
  fileIn >> B;

  for (int N = 1; N <= 300; N++)
  {
    string out = to_base_b(N * N, B);
    if (is_palindrome(out))
    {
      out = to_base_b(N, B) + " " + out + "\n";
      fileOut << out;
      cout << out;
    }
  }

  return 0;
}
