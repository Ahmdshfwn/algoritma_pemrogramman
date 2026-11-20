#include <iostream>
using namespace std;

int main()
{
	cout<<"AHMAD SHAFWAN"<<endl;
	int a,b,c;
	cout<<"MASUKAN NILAI KE-1 : "; cin>>a;
	cout<<"MASUKAN NILAI KE-2 : "; cin>>b;
	cout<<"MASUKAN NILAI KE-3 : "; cin>>c;
	if(a<b)
		if(b<c)
		cout<<"\nUrutkan nilai dari yang terkecil : "<<a<<" "<<b<<" "<<c<<" ";
		
		else 
			if(a<c)
			cout<<"\nUrutkan nilai dari yang terkecil : "<<a<<" "<<c<<" "<<b<<" ";
		
		else
			cout<<"\nUrutkan nilai dari yang terkecil : "<<c<<" "<<a<<" "<<b<<" ";
		
		else 
			if(a<c)
			cout<<"\nUrutkan nilai dari yang terkecil : "<<b<<" "<<a<<" "<<c<<" ";
		else 
			if(b<c)
			cout<<"\nUrutkan nilai dari yang terkecil : "<<b<<" "<<c<<" "<<a<<" ";
		else
		cout<<"\nUrutkan nilai dari yang terkecil : "<<c<<" "<<b<<" "<<a<<" ";
		
	return 0;
}
