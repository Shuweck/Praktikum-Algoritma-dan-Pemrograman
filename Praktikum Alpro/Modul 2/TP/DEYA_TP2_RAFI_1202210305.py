print('\n== Kalkulator ==\n')

#input operasi
bilangan_pertama=int(input('masukkan bilangan ke-1: '))
operator_bilangan=str(input('Masukkan operasinya:(+),(-),(*),(/): '))
bilangan_kedua=int(input('masukkan bilangan ke-2: '))


match operator_bilangan:
    case '+':
        operasi_bilangan=bilangan_pertama + bilangan_kedua
    case '-':
        operasi_bilangan=bilangan_pertama - bilangan_kedua
    case '*':
        operasi_bilangan=bilangan_pertama * bilangan_kedua
    case '/':
        operasi_bilangan=bilangan_pertama / bilangan_kedua
    case _  : 
        print('operasi tidak valid')

#output hasil    
print(f'\nHasil operasi: {bilangan_pertama} {operator_bilangan} {bilangan_kedua} : {operasi_bilangan}')



        
        


