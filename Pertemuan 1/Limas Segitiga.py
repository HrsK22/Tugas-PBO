print("Aplikasi Menghitung Luas dan Volume Limas Segitiga")
print("-----------------------------------------------------")

""""
Keterangan:
a = Luas alas
t = Tinggi
T = Tinggi Limas
LS = Luas Segitiga
"""

# Atur Nilai:
print("Masukkan Nilai")
LS_1 = float(input("Luas Segitiga 1: "))
LS_2 = float(input("Luas Segitiga 2: "))
LS_3 = float(input("Luas Segitiga 3: "))
LS_4 = float(input("Luas Segitiga 4: "))
a = float(input("Luas Alas: "))
t = float(input("Tinggi: "))
T = float(input("Tinggi Limas: "))
print("-----------------------------------------------------")

# Rumus
luas = LS_1 + LS_2 + LS_3 + LS_4
volume = 1/6 * a * t * T

# output
print("Hasil Perhitungan")
print("Luas Limas Segitiga:", luas)
print("Volume Limas Segitiga:", volume)