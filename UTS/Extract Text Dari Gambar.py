from tkinter import Tk, Button, Label, filedialog, Text, Scrollbar
from PIL import Image, ImageTk
import pytesseract

current_image_path = ""

def ekstrak_teks_dari_gambar(jalur_gambar):
    gambar = Image.open(jalur_gambar)

    teks = pytesseract.image_to_string(gambar)

    return teks

def buka_dialog_file():
    global current_image_path
    jalur_file = filedialog.askopenfilename(filetypes=[("File gambar", "*.png;*.jpg;*.jpeg;*.gif")])
    if jalur_file:
        current_image_path = jalur_file
        tampilkan_gambar(jalur_file)

def ekstrak_dan_tampilkan_teks():
    global current_image_path
    if current_image_path:
        teks_diekstrak = ekstrak_teks_dari_gambar(current_image_path)

        textbox_teks.delete(1.0, "end")
        textbox_teks.insert("end", teks_diekstrak)

def tampilkan_gambar(jalur_gambar):
    gambar = Image.open(jalur_gambar)
    gambar.thumbnail((300, 300))
    foto = ImageTk.PhotoImage(gambar)

    label_gambar.config(image=foto)
    label_gambar.image = foto

root = Tk()
root.title("Extract Text Dari Gambar")
root.minsize(width=500, height=400)
root.configure(bg="light pink")


tombol_buka = Button(root, text="Buka Gambar", command=buka_dialog_file, bg="violet", fg="black", font=('Helvetica', 12))
tombol_buka.pack(pady=10)

label_gambar = Label(root, bg="light pink")
label_gambar.pack()

tombol_ekstrak_teks = Button(root, text="Ekstrak Teks", command=ekstrak_dan_tampilkan_teks, bg="violet", fg="black", font=('Helvetica', 12))
tombol_ekstrak_teks.pack(pady=10)

textbox_teks = Text(root, wrap="word", height=10, width=60)
textbox_teks.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(root, command=textbox_teks.yview, orient="vertical")
scrollbar.pack(side="right", fill="y")

textbox_teks.config(yscrollcommand=scrollbar.set)

root.mainloop()
