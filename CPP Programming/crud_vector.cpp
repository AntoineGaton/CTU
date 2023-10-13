#include <iostream>
#include <vector>

using namespace std;

void printVector(const vector<int> &vec)
{
   for (const int &element : vec)
   {
      cout << element << " ";
   }
   cout << endl;
}

int main()
{
   vector<int> myVector;
   int choice;

   while (true)
   {
  
      cout << "\nMenu:\n";
      cout << "1. Print Vector\n";
      cout << "2. Add Element\n";
      cout << "3. Delete Element\n";
      cout << "4. Move Element\n";
      cout << "5. Clear Vector\n";
      cout << "6. Exit\n";
      cout << "Enter your choice: ";
      cin >> choice;

      switch (choice)
      {
         case 1:
            cout << "Vector: ";
            printVector(myVector);
            break;
         case 2:
            int newValue;
            cout << "Enter a value to add: ";
            cin >> newValue;
            myVector.push_back(newValue);
            break;
         case 3:
            if (!myVector.empty())
            {
               int indexToDelete;
               cout << "Enter the index to delete: ";
               cin >> indexToDelete;
               if (indexToDelete >= 0 && indexToDelete < myVector.size())
               {
                  myVector.erase(myVector.begin() + indexToDelete);
               }
               else
               {
                  cout << "Invalid index.\n";
               }
            }
            else
            {
               cout << "Vector is empty. Nothing to delete.\n";
            }
            break;
         case 4:
            if (!myVector.empty())
            {
               int fromIndex, toIndex;
               cout << "Enter the index to move: ";
               cin >> fromIndex;
               if (fromIndex >= 0 && fromIndex < myVector.size())
               {
                  cout << "Enter the new index: ";
                  cin >> toIndex;
                  if (toIndex >= 0 && toIndex <= myVector.size())
                  {
                     iter_swap(myVector.begin() + fromIndex, myVector.begin() + toIndex);
                  }
                  else
                  {
                     cout << "Invalid destination index.\n";
                  }
               }
               else
               {
                  cout << "Invalid source index.\n";
               }
            }
            else
            {
               cout << "Vector is empty. Nothing to move.\n";
            }
            break;
         case 5:
            myVector.clear();
            break;
         case 6:
            return 0;
         default:
            cout << "Invalid choice. Please enter a valid option.\n";
      }
   }

   return 0;
}