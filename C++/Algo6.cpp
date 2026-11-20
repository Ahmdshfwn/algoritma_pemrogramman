#include <iostream>
using namespace std;

int main()
{
	cout<<"AHMAD SHAFWAN"<<endl;
	int a,b,c;
	cout<<"MASUKAN NILAI KE-1 : "; cin>>a;
	cout<<"MASUKAN NILAI KE-2 : "; cin>>b;
	cout<<"MASUKAN NILAI KE-3 : "; cin>>c;
	
	if(a>b)
		if(a>c)
			cout<<"\n Nilai Terbesar : "<<a;
		else
			cout<<"\n Nilai Terbesar : "<<c;
	else
		if(b>c)
			cout<<"\n Nilai Terbesar : "<<b;
		else
			cout<<"\n Nilai Terbesar : "<<c;
		
	return 0;
}
