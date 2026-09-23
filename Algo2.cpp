#include <iostream>
using namespace std;
int main()
{
	float C,F;
	cout<<"Masukkan suhu celcius : ";
	cin>>C;
	F = (C * 9.0 / 5.0) + 32;
	cout<<"Suhu "<<C <<" Celcius sama dengan : "<<F << " Fahrenheit. "<<endl;
	return 0;	
}
