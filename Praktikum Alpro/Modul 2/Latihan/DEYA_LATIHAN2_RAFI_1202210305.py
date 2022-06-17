x=int(input('\nMasukkan umur: '))
if x >= 0 and x <=5:
    print('Balita')
elif x>=6 and x <=13:
    print('Anak-anak')
elif x>=14 and x <=17:
    print('Remaja')
elif x>=18 and x <=59:
    print('Dewasa')
elif x>=60:
    print('Dewasa')
else: 
    print('Input salah')


