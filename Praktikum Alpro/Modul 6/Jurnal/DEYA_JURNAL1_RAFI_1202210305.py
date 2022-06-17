try:
    NIM = int(input('Masukkan kode NIM mu: '))
    password = str(input('Masukkan password kamu: '))
    assert len(password) >= 8
    if password == 'PestaRahasiaNihBos':
        password = True
        print('Kamu berhasil masuk')
    else:    
        password = False
        
except AssertionError:
    print('Password kamu kurang dari 8 karakter')


