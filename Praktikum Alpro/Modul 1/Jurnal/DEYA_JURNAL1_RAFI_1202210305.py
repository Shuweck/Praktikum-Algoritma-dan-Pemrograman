#konversi ke suhu celcius menjadi reamur, fahrenheit, dan kelvin
print("\n===PROGRAM KONVERSI SUHU===")
celcius=float(input("Masukkan suhu celcius: "))
reamur=(4 / 5) * celcius
fahrenheit=(9 / 5) * celcius + 32
kelvin=celcius + 273

print("{} celcius ke reamur : {}".format(celcius,reamur))
print("{} celcius ke fahrenheit : {}".format(celcius,fahrenheit))
print("{} celcius ke kelvin : {}".format(celcius,kelvin))