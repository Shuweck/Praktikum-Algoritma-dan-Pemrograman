total_diskon = 0
total_dibayar_sebelum_diskon_akhir = 0

diskon_minyak = 0.1     # 10%
diskon_total = 0.1      # 10%
batas_minimal_diskon = 200000

jalan_terus = True

while jalan_terus:
    barang = input('masukkan nama barang yang ingin dibeli: ')

    # jika barang minyak, apply diskon 10% lalu masukkan ke total
    if barang == 'minyak':
        # tanya user berapa minyak yg dibeli
        jumlah_item = int(input('masukkan jumlah barang yang ingin dibeli: '))

        # masukkan harga minyak
        harga_item = int(input('masukkan harga barang: '))

        # hitung total harga sblm diskon
        harga_total_sebelum_diskon = harga_item * jumlah_item

        # hitung total setelah diskon
        total_diskon_minyak = diskon_minyak * harga_total_sebelum_diskon
        harga_total_setelah_diskon = harga_total_sebelum_diskon - total_diskon_minyak

        # jadi total diskon minyak
        total_diskon += total_diskon_minyak

        # tambahkan harga setelah diskon ke total yang harus dibayar
        total_dibayar_sebelum_diskon_akhir += harga_total_setelah_diskon

     # jika user sudah selesai belanja
    elif barang == 'selesai':
        # cek apakah total sebelum diskon akhir >= 200000
        if total_dibayar_sebelum_diskon_akhir >= batas_minimal_diskon:

            # hitung total yang harus dibayar user setelah semua diskon
            total_diskon_minyak = total_dibayar_sebelum_diskon_akhir * diskon_total
            total_dibayar_sesudah_diskon_akhir = total_dibayar_sebelum_diskon_akhir - total_diskon_minyak
        
            # update total diskon semuanya
            total_diskon_akhir = total_dibayar_sebelum_diskon_akhir - total_dibayar_sesudah_diskon_akhir
        else:
            total_dibayar_sesudah_diskon_akhir = total_dibayar_sebelum_diskon_akhir

        # tunjukkan ke user
        print(f'\nTotal harga sebelum diskon adalah: {total_dibayar_sebelum_diskon_akhir}')
        print(f'Total diskon: {total_diskon_akhir}')
        print('-------------------------------------------')
        print(f'Total yang harus anda bayar: {total_dibayar_sesudah_diskon_akhir}\n')

    # jika barang bukan minyak
    else:
        # tanya user berapa barang yang dibeli
        jumlah_item = int(input('masukkan jumlah barang yang ingin dibeli: '))

        # masukkan harga barang
        harga_item = int(input('masukkan harga barang: '))

        # hitung total harga sblm diskon
        harga_total_sebelum_diskon = harga_item * jumlah_item

        # langsung masukkan ke total, hitung diskon akhir ketika sudah selesai
        total_dibayar_sebelum_diskon_akhir += harga_total_sebelum_diskon