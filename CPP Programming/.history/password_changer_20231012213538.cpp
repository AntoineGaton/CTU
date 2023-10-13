
using namespace std;

int main()
{
   string passwdStr;
   unsigned int i;

   cin >> passwdStr;

   for (char &c : passwdStr)
   {
      if (!std::isalpha(c))
      {
         c = 'z';
      }
   }

   cout << "Valid password: " << passwdStr << endl;

   return 0;
}