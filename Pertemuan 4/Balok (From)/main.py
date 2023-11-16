import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, END, W
from fungsi import hitung_luas, hitung_volume

# Create tkinter object
app = Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Balok")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Panjang
panjang = Label(frame, text="Panjang:")
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Panjang
txtp = Entry(frame)
txtp.grid(row=0, column=1)

# Label Lebar
lebar = Label(frame, text="Lebar:")
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Lebar
txtl = Entry(frame)
txtl.grid(row=1, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txtt = Entry(frame)
txtt.grid(row=2, column=1)

# Button
def hitung():
    hasil_luas = hitung_luas(txtp.get(), txtl.get(), txtt.get())
    hasil_volume = hitung_volume(txtp.get(), txtl.get(), txtt.get())
    txtluas.delete(0, END)
    txtvolume.delete(0, END)
    txtluas.insert(END, hasil_luas)
    txtvolume.insert(END, hasil_volume)

hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas:")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Output Textbox Luas
txtluas = Entry(frame)
txtluas.grid(row=4, column=1)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Output Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=5, column=1)

app.mainloop()