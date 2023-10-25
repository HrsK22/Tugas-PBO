print("Aplikasi Menghitung Luas dan Volume Prisma Segitiga")
print("-----------------------------------------------------")
"""
Keterangan:
S = Sisi
T = Tinggi prisma
a = Alas
t = Tinggi
"""

# Atur Nilai
print("Masukkan Nilai")
S_1 = float(input("Sisi 1: "))
S_2 = float(input("Sisi 2: "))
S_3 = float(input("Sisi 3: "))
T = float(input("Tinggi Prisma: "))
a = float(input("Alas: "))
t = float(input("Tinggi: "))
print("-----------------------------------------------------")

# Rumus
keliling_segitiga = S_1 + S_2 + S_3
luas_selimut = keliling_segitiga * T
luas_permukaan = keliling_segitiga * T * a * t
volume = 1/2 * a * t * T

# Output
print("Hasil Perhitungan")
print("Keliling Segitiga: ", keliling_segitiga)
print("Luas Selimut: ", luas_selimut)
print("Luas Permukaan: ", luas_permukaan)
print("Volume: ", volume)