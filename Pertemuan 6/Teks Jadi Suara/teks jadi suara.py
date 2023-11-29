from gtts import gTTS
import os
import tkinter as tk
from tkinter import ttk

def convert_to_speech():
    text = text_entry.get()
    if text:
        language = language_var.get()
        speech = gTTS(text=text, lang=language, slow=False)
        speech.save("output.mp3")
        os.system("start output.mp3")
    else:
        result_label.config(text="Masukkan teks terlebih dahulu.")

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Text to Speech Converter")

# Label dan Entry untuk memasukkan teks
text_label = tk.Label(root, text="Masukkan Teks:")
text_label.pack(pady=10)
text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=10)

# Label untuk memilih bahasa
language_label = tk.Label(root, text="Pilih Bahasa:")
language_label.pack(pady=5)
languages = ['id', 'en']  # Contoh bahasa (dapat disesuaikan)
language_var = ttk.Combobox(root, values=languages, state="readonly")
language_var.set('id')  # Bahasa default
language_var.pack(pady=5)

# Tombol untuk mengonversi teks menjadi suara
convert_button = tk.Button(root, text="Konversi ke Suara", command=convert_to_speech)
convert_button.pack(pady=20)

# Label untuk menampilkan pesan hasil
result_label = tk.Label(root, text="")
result_label.pack()

# Menjalankan aplikasi
root.mainloop()
