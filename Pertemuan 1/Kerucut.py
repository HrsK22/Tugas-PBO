print("Aplikasi Menghitung Luas dan volume kerucut")
print("-----------------------------------------------------")

"""
Keterangan:
L = Luas permukaan kerucut
r = Jari-jari
t = Tinggi
s = Garis pelukis
phi = 3,14
"""

# Atur Nilai
print("Masukkan Nilai")
phi = 3.14
r = float(input("Jari - jari: "))
s = float(input("Garis Pelukis: "))
t = float(input("Tinggi: "))
print("phi:", phi)
print("-----------------------------------------------------")

# Rumus
luas_selimut = phi * r * s
luas_permukaan = (phi * r * s) + (phi * r**2)
volume = 1/3 * phi * t

# Output
print("Hasil Perhitungan")
print("Luas Selimut:", luas_selimut)
print("Luas Permukaan:", luas_permukaan)
print("Volume:", volume)