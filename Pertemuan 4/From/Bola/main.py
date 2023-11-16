import tkinter as tk
from tkinter import Tk,Frame,Label,Entry,Button,END,W
from fungsi import hitung_luas, hitung_volume


# Create tkinter object
app = Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Bola")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Jari - Jari
jarijari = Label(frame, text="Jari - Jari:")
jarijari.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Jari - Jari
txtjarijari = Entry(frame)
txtjarijari.grid(row=0, column=1)

# Button
def hitung():
    hasil_luas = hitung_luas(txtjarijari.get())
    hasil_volume = hitung_volume(txtjarijari.get())
    txtluas.delete(0,END)
    txtluas.insert(END,hasil_luas)
    txtvolume.delete(0,END)
    txtvolume.insert(END,hasil_volume)

hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# Output Luas
luas = Label(frame, text="Luas:")
luas.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas
txtluas = Entry(frame)
txtluas.grid(row=2, column=1)

# Output Volume
volume = Label(frame, text="Volume:")
volume.grid(row=3, column=0, sticky=W, padx=5, pady=5)
# Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=3, column=1)

app.mainloop()