print("Aplikasi Menghitung Luas dan Volume Selinder (Tabung)")
print("-----------------------------------------------------")

"""
Keterangan:
L = Luas permukaan tabung
r = Jari - jari lingkaran tabung
t = Tinggi
phi = 3.14
"""

# Atur Nilai
print("Masukkan Nilai")
phi = 3.14
r = float(input("Jari - Jari: "))
t = float(input("Tinggi: "))
print("phi:", phi)
print("-----------------------------------------------------")

# Rumus
luas_selimut = 2 * phi * r * t
luas_permukaan = (2 * phi * r * t) + (2 * phi * r**2)
volume = phi * r**2 * t

# output
print("Hasil Perhitungan")
print("Luas Selimut:", luas_selimut)
print("Luas Permukaan:", luas_permukaan)
print("Volume:", volume)