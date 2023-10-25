print("Aplikasi Menghitung Luas dan Volume Limas Segiempat")
print("-----------------------------------------------------")

"""
Keterangan:
LS_1-4 = Luas Sisi
LS_5 = Luas Persegi
La = Luas Alas
t = Tinggi
"""

# Atur Nilai
print("Masukkan Nilai")
LS_1 = float(input("Luas Sisi 1: "))
LS_2 = float(input("Luas Sisi 2: "))
LS_3 = float(input("Luas Sisi 3: "))
LS_4 = float(input("Luas Sisi 4: "))
LS_5 = float(input("Luas Persegi: "))
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
