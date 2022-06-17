# database untuk user
# -----------------------
kata_sandi = "1234"
# -----------------------
no_card_inside_atm = True
while no_card_inside_atm:
    print('WELCOME TO THE ATM MACHINE BANK RAFIANO')
    print('---------------------------------------\n')
    
    error_counter = 0
    while error_counter < 3:
        user_pin = input("masukkan PIN anda: ")
        if user_pin == kata_sandi:
            print('Anda berhasil login') #hapus aja ntar anda berhasil login ni ga keoutput soalnya awkodaok bingung deh
            
            error_counter = 0
            break
        else:
            error_counter = error_counter + 1
            allowed_attempt = 3 - error_counter
            print(f'\nPIN salah, {allowed_attempt} percobaan lagi')
    
    if error_counter == 3:
        print('Password salah')
    
    
