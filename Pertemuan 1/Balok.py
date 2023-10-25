print("Aplikasi Menghitung Luas dan Volume Balok")
print("-----------------------------------------------------")

"""
Keterangan:
p = Panjang
l = Lebar
t = Tinggi
"""

# Atur Nilai
print("Masukkan Nilai")
p = int(input("Panjang: "))
l = int(input("Lebar: "))
t = int(input("Tinggi: "))
print("-----------------------------------------------------")

# Rumus
luas = (2 * p * l) + (2  * p * t) + (2* l * t)
volume = (p * l * t)

# Output
print("Hasil Perhitungan")
print("Luas:", luas)
print("Volume:", volume)
