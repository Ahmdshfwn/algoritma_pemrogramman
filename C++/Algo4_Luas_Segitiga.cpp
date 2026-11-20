#include <iostream>
using namespace std;

main()
{
	double alas,
	tinggi,
	setengah = 0.5;
	
	
	cout<<"Hitunglah Luas Segitiga"<<endl;
	cout<<"Masukan Alas : ";
	cin>>alas;
	cout<<"Masukan Tinggi : ";
	cin>>tinggi;
	
	double luas = setengah * alas * tinggi;
	cout<<"Luas segitiga adalah : "<<luas<<endl;
	return 0;
}
