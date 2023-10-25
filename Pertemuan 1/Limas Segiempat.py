print("Aplikasi Menghitung Luas dan Volume Limas Segiempat")
print("-----------------------------------------------------")

"""
Keterangan:
LS = Luas Sisi
La = Luas Alas
t = Tinggi
"""

# Atur Nilai
print("Masukkan Nilai")
LS_1 = float(input("Luas Segitiga 1: "))
LS_2 = float(input("Luas Segitiga 2: "))
LS_3 = float(input("Luas Segitiga 3: "))
LS_4 = float(input("Luas Segitiga 4: "))
LS_5 = float(input("Luas Segitiga 5: "))
La = float(input("Luas Alas: "))
t = float(input("Tinggi: "))
print("-----------------------------------------------------")

# Rumus
luas = LS_1 + LS_2 + LS_3 + LS_4 + LS_5
volume = 1/3 * La * t

# Output
print("Hasil Perhitungan")
print("Luas:", luas)
print("Volume:", volume)