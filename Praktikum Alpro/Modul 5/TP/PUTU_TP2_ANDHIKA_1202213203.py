jumlah=int(input("Masukan banyaknya angka: "))
hasil=[]
for i in range (jumlah):
    angka=int(input(f"Masukan angka ke-{i+1}  : "))  
    condition=angka in hasil
    if condition == True:
         continue 
    hasil.append(angka)    
hasil.sort()
print(hasil)
