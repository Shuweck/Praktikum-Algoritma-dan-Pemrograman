print('Silahkan tulis kesan dan pesan kamu untuk Praktikum Alpro 2022!')
print('Mungkin kalian punya masukan, atau mungkin ada pesan untuk para asisten boleh banget ditulis ya!')
print('\n--------\n')

kesan = 'Saya ingin berterimakasih atas ilmu yang telah dibagikan oleh kakak asisten praktikum daspro yang telah membantu saya dalam menyelesaikan tugas praktikum Alpro 2022. Mungkin sekian dari saya, semoga ilmu yang telah kakak berikan akan berguna bagi banyak orang.'

file = open('C:\Workspace\Alpro\Praktikum Alpro\Modul 6\Jurnal\Masukan.txt','w')
file.write(f'{kesan}\n')
file.close()