/*
ID: khilfik1
LANG: C++
TASK: milk
*/
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
  ifstream fileIn("milk.in");

  int N, M;
  fileIn >> N >> M;
  vector<vector<int>> farmers;
  for (int i = 0; i < M; i++)
  {
    vector<int> farmer = {0, 0};
    fileIn >> farmer[0] >> farmer[1];
    farmers.push_back(farmer);
  }
  fileIn.close();

  int total = 0;
  while (N > 0)
  {
    int lo = farmers[0][0], lo_i = 0;
    for (int i = 1; i < farmers.size(); i++)
    {
      if (farmers[i][0] < lo)
      {
        lo = farmers[i][0];
        lo_i = i;
      }
    }
    vector<int> lo_farmer = farmers[lo_i];
    if (lo_farmer[1] < N)
    {
      // Take everything
      total += lo_farmer[1] * lo_farmer[0];
      N -= lo_farmer[1];
      farmers.erase(farmers.begin() + lo_i);
    }
    else
    {
      // Take only some
      total += N * lo_farmer[0];
      N = 0;
    }
  }

  ofstream fileOut("milk.out");
  fileOut << total << endl;
  cout << total << endl;
  fileOut.close();
}