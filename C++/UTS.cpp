#include <iostream>
using namespace std;

int main()
{
	int 
		namaPesanan = 3,
		harga;
		
	string namaMahasiswa;
	
	cout<<"==========================\n";
	cout<<"MAKANAN YANG ADA DISINI"<<endl;
	cout<<"1. NASI GORENG RP10.000"<<endl;
	cout<<"2. NASI AYAM RP15.000"<<endl;
	cout<<"3. NASI BEBEK RP20.000"<<endl;
	cout<<"==========================\n";
	
	cout<<"Masukkan Nama : ";
	cin>>namaMahasiswa;
	cout<<"Nama anda adalah : "<<namaMahasiswa<<endl;
	
	cout<<"Masukan kode pesanan : ";
	cin>>namaPesanan;
		
	if(namaPesanan == 1)
	{
		cout<<"1. NASI GORENG"<<endl;
		harga = 10000;
		
	}
	else if(namaPesanan == 2)
	{
		cout<<"2. NASI AYAM"<<endl;
		harga = 15000;
	}
	else if(namaPesanan == 3)
	{
		cout<<"3. NASI BEBEK"<<endl;
		harga = 20000;
	}
	else
	{
		cout<<"INVALID NUMBER"<<endl;
		return 0;
	}
	cout<<"HARGA PESANAN : "<<harga<<endl;

	return 0;
}
