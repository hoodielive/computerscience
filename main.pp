#include <iostream>

using namespace std; 

void doPrint()
{
	count << "In doPrint()\n"; 
}

int main()
{
	count << "Starting main()\n"; 
	doPrint(); 
	cout << "Entering main()\n";
}
