#include <iostream>
using namespace std;

int main()
{
   int numRows;
   int numColumns;
   int currentRow;
   int currentColumn;
   char currentColumnLetter;

   cout << "Enter number of rows: ";
   cin >> numRows;

   cout << "Enter number of columns: ";
   cin >> numColumns;

   for (int currentRow = 1; currentRow <= numRows; currentRow++)
   {
      for (char currentColumn = 'A'; currentColumn < 'A' + numColumns; currentColumn++)
      {
         cout << currentRow << currentColumn << " ";
      }
   }

   cout << endl;

   return 0;
}