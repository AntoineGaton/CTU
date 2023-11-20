#include <iostream>
using namespace std;

void printPattern(int userNum)
{
   for (int i = 1; i <= userNum; i++)
   {
      for (int j = 0; j < i; j++)
      {
         cout << " ";
      }
      cout << i << endl;
   }

   for (int i = userNum - 1; i > 0; i--)
   {
      for (int j = 0; j < i; j++)
      {
         cout << " ";
      }
      cout << i << endl;
   }
}

int main()
{
   int userNum;
   int numLoops;

   cout << "Enter number: ";
   cin >> userNum;

   cout << "Enter number of loops: ";
   cin >> numLoops;

   for (int w = 0; w < numLoops; w++)
   {
      printPattern(userNum);
   }

   return 0;
}
