import tkinter as tk
from tkinter import Label, Entry, Button, Text, END

class JadwalKuliahApp:
    def __init__(self, master):
        self.master = master
        master.title("Jadwal Kuliah App")
        master.geometry("400x500")
        master.configure(bg="#f0f0f0")

        self.label_judul = Label(master, text="Jadwal Kuliah", font=("Arial", 16, "bold"), bg="#f0f0f0")
        self.label_judul.pack(pady=10)

        self.txt_hari = Entry(master, bg="lightgray", fg="black", font=("Arial", 12))
        self.txt_hari.pack(pady=5)

        self.txt_jadwal = Text(master, height=10, width=40, wrap=tk.WORD, bg="lightgray", fg="black", font=("Arial", 12))
        self.txt_jadwal.pack(pady=10)
        self.txt_jadwal.config(state=tk.DISABLED)

        self.btn_tambah = Button(master, text="Tambah Jadwal", command=self.tambah_jadwal, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.btn_tambah.pack(pady=10)

        self.btn_tampilkan = Button(master, text="Tampilkan Jadwal", command=self.tampilkan_jadwal, bg="#008CBA", fg="white", font=("Arial", 12, "bold"))
        self.btn_tampilkan.pack(pady=10)

    def tambah_jadwal(self):
        hari = self.txt_hari.get().capitalize()
        jadwal = self.txt_jadwal.get("1.0", END)

        if hari and jadwal:
            with open("jadwal.txt", "a") as file:
                file.write(f"{hari}:\n{jadwal}\n\n")
            self.txt_hari.delete(0, END)
            self.txt_jadwal.delete(1.0, END)
            self.txt_jadwal.config(state=tk.DISABLED)
        else:
            tk.messagebox.showwarning("Peringatan", "Isi semua kolom terlebih dahulu!")

    def tampilkan_jadwal(self):
        self.txt_jadwal.config(state=tk.NORMAL)
        self.txt_jadwal.delete(1.0, END)
        try:
            with open("jadwal.txt", "r") as file:
                jadwal = file.read()
            self.txt_jadwal.insert(tk.END, jadwal)
        except FileNotFoundError:
            tk.messagebox.showinfo("Info", "File jadwal tidak ditemukan.")
        self.txt_jadwal.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = JadwalKuliahApp(root)
    root.mainloop()
