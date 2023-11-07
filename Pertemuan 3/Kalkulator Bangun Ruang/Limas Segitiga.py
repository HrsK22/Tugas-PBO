import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    LS_1 = float(txtluas_segitiga1.get())
    LS_2 = float(txtluas_segitiga2.get())
    LS_3 = float(txtluas_segitiga3.get())
    LS_4 = float(txtluas_segitiga4.get())
    a = float(txttinggi.get())
    t = float(txttinggi.get())
    T = float(txttinggi_limas.get())
    
    L = round(LS_1 + LS_2 + LS_3 + LS_4,2)
    txtluas.delete(0,END)
    txtluas.insert(END,L)

def hitung_volume():
    LS_1 = float(txtluas_segitiga1.get())
    LS_2 = float(txtluas_segitiga2.get())
    LS_3 = float(txtluas_segitiga3.get())
    LS_4 = float(txtluas_segitiga4.get())
    a = float(txttinggi.get())
    t = float(txttinggi.get())
    T = float(txttinggi_limas.get())
    
    V = round(1/6*a*t*T,2)
    txtvolume.delete(0,END)
    txtvolume.insert(END,V)
    
def hitung():
    hitung_luas()
    hitung_volume()
    
# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Limas Segitiga")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Luas Segitiga 1
luas_segitiga1 = Label(frame, text="Luas Segitiga 1:")
luas_segitiga1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Segitiga 1
txtluas_segitiga1 = Entry(frame)
txtluas_segitiga1.grid(row=0, column=1)

# Label Luas Segitiga 2
luas_segitiga2 = Label(frame, text="Luas Segitiga 2:")
luas_segitiga2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Segitiga 2
txtluas_segitiga2 = Entry(frame)
txtluas_segitiga2.grid(row=1, column=1)

# Label Luas Segitiga 3
luas_segitiga3 = Label(frame, text="Luas Segitiga 3:")
luas_segitiga3.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Segitiga 2
txtluas_segitiga3 = Entry(frame)
txtluas_segitiga3.grid(row=2, column=1)

# Label Luas Segitiga 4
luas_segitiga4 = Label(frame, text="Luas Segitiga 4:")
luas_segitiga4.grid(row=3, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Segitiga 4
txtluas_segitiga4 = Entry(frame)
txtluas_segitiga4.grid(row=3, column=1)

# Label Luas Alas
luas_alas = Label(frame, text="Luas Alas:")
luas_alas.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Alas
txtluas_alas = Entry(frame)
txtluas_alas.grid(row=4, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=5, column=1)

# Label Tinggi Limas
tinggi_limas = Label(frame, text="Tinggi Limas:")
tinggi_limas.grid(row=6, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi Limas
txttinggi_limas = Entry(frame)
txttinggi_limas.grid(row=6, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Luas
luas = Label(frame, text="Luas:")
luas.grid(row=8, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas
txtluas = Entry(frame)
txtluas.grid(row=8, column=1)

# Output Volume
volume = Label(frame, text="Volume:")
volume.grid(row=9, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas
txtvolume = Entry(frame)
txtvolume.grid(row=9, column=1)

app.mainloop()