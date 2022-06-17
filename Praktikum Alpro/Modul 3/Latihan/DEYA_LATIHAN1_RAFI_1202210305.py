max_attempt = 3
status_login = False
username = 'qwerty'
password = 'kijolp'

print('---silahkan login---')
while (max_attempt >0):
    #input username
    current_user = input ('Masukkan username: ')

    #pastikan username benar
    if current_user != username:
        max_attempt -= 1
        print(f'gagal login, wrong username, {max_attempt} percobaan tersisa')
        continue

    #if username is correct
    current_password = input ('Masukkan password: ')

    if current_password != password:
        max_attempt -= 1
        print(f'gagal login, wrong password, {max_attempt} percobaan tersisa')
        continue
    
    #bila user dan pass benar, status login True
    status_login = True
    break

if status_login:
    print('Anda berhasil login!')
else:
    print('Maaf percobaan habis... Aplikasi tertutup otomatis...')