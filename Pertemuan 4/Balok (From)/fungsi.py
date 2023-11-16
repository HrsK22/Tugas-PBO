def hitung_luas(p, l, t):
    try:
        p = float(p)
        l = float(l)
        t = float(t)
        L = round(((2 * p * l) + (2 * p * t) + (2 * l * t)), 2)
        return L
    except ValueError:
        return "Masukkan angka"

def hitung_volume(p, l, t):
    try:
        p = float(p)
        l = float(l)
        t = float(t)
        V = round((p * l * t), 2)
        return V
    except ValueError:
        return "Masukkan angka"