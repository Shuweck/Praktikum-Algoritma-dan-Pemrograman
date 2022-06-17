print("|| Program Tantangan Mr. X ||")
nama = input('Masukkan nama: ')
id = input('Masukkan ID: ')
divisi = input('Masukkan divisi: ')
status = input('Masukkan status: ')

data = f'nama: {nama}\nID: {id}\ndivisi: {divisi}\nstatus: {status}'

file_data = open('C:\\Workspace\\tantangan.txt','w')

file_data.write(data)
file_data.write('\n')

file_data.close()

