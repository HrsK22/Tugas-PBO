import tkinter as tk
from tkinter import filedialog
import pygame.mixer #Menggunakan library pygame

def putar_mp3():
    global lagu_sedang_diputar
    jalur_file = filedialog.askopenfilename(filetypes=[("File MP3", "*.mp3")])
    if jalur_file:
        pygame.mixer.init()
        pygame.mixer.music.load(jalur_file)
        pygame.mixer.music.play()
        lagu_sedang_diputar = jalur_file
        perbarui_keterangan_lagu()

def pause_mp3():
    pygame.mixer.music.pause()

def play_mp3():
    pygame.mixer.music.unpause()

def berhenti_mp3():
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    root.quit()

def perbarui_keterangan_lagu():
    keterangan_lagu.config(text="Lagu: " + lagu_sedang_diputar)

# Variabel global
lagu_sedang_diputar = ""

# Buat jendela tkinter
root = tk.Tk()
root.title("Pemutar MP3")
root.minsize(width=400, height=300)

# Buat dan letakkan label judul
label_judul = tk.Label(root, text="Pemutar MP3", font=("Helvetica", 16))
label_judul.pack(pady=10)

# Buat dan letakkan tombol putar
tombol_putar = tk.Button(root, text="Putar MP3", command=putar_mp3)
tombol_putar.pack(pady=10)

# Buat dan letakkan tombol jeda
tombol_jeda = tk.Button(root, text="Pause", command=pause_mp3)
tombol_jeda.pack(pady=10)

# Buat dan letakkan tombol lanjutkan
tombol_lanjutkan = tk.Button(root, text="Play", command=play_mp3)
tombol_lanjutkan.pack(pady=10)

# Buat dan letakkan tombol keluar
tombol_keluar = tk.Button(root, text="Keluar", command=berhenti_mp3)
tombol_keluar.pack(pady=10)

# Buat dan letakkan label keterangan lagu
keterangan_lagu = tk.Label(root, text="Lagu: -", font=("Helvetica", 12))
keterangan_lagu.pack(pady=5)

# Mulai loop tkinter
root.mainloop()
