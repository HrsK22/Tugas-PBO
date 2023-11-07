import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    r = float(txtjarijari.get())
    phi = 3.14
    
    L = (4*phi*r**2)
    txtluas.delete(0,END)
    txtluas.insert(END,L)
    
def hitung_volume():
    r = float(txtjarijari.get())
    phi = 3.14
    
    V = (4/3*phi*r**3)
    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

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