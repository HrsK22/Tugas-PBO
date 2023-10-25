print("Aplikasi Menghitung Luas dan Volume Bola")
print("-----------------------------------------------------")

"""
Keterangan:
phi = 3.14
r = Jari - jari
"""

# Atur Nilai
print("Masukkan Nilai")
phi = 3.14
r = float(input("Jari - jari: "))
print("phi:", phi)
print("-----------------------------------------------------")

# Rumus
luas_bola = 4 * phi * r**2
volume_bola = 4/3 * phi * r**3

# Output
print("Hasil Perhitungan")
print("Luas:", luas_bola)
print("Volume:", volume_bola)