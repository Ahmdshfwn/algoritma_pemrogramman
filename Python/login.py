username = "admin"
password = 123456
input_user = str(input('Masukan username : '))
input_pass = int(input('Masukan password : '))

if input_user == username:
    print('Berhasil Login!')
else :
    print('salah')

if input_pass == password:
    print('Berhasil Login!')
else :
    print('salah')