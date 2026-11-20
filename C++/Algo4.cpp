#include <iostream>
using namespace std;

main()
{
	int alas,tinggi;
	double setengah = 0.5;
	cout<<"Hitunglah Luas Segitiga"<<endl;
	cout<<"Masukan alas : ";
	cin>>alas;
	cout<<"Masukan tinggi : ";
	cin>>tinggi;
	
	double luas = setengah * alas * tinggi;
	cout<<"Luas segitiga "<<luas<<endl;
	return 0;
}
