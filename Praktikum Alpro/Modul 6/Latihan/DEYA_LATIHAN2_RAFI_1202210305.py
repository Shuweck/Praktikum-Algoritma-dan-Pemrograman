
world_data = {
    'Filipina': 'Manila',
    'Indonesia': 'Jakarta',
    'Swedia': 'Stockholm'
}

try:
    pilihan_user = input('Sebutkan negara: ')
    print(f'Ibukota {pilihan_user} adalah {world_data[pilihan_user]}')
except:
    print(f'{pilihan_user} tidak terdaftar di dalam dictionary')