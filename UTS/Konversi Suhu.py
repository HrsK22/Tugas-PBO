import tkinter as tk
from tkinter import ttk

def konversi_suhu():
    try:
        suhu_awal = float(entry_suhu_awal.get())
    except ValueError:
        hasil_label.config(text="Masukkan nilai.")
        return

    unit_input = input_unit_var.get()
    unit_output = output_unit_var.get()

    if unit_input == unit_output:
        hasil_label.config(text="Pilih unit berbeda.")
        return

    if unit_input == "Celcius":
        suhu_celcius = suhu_awal
    elif unit_input == "Fahrenheit":
        suhu_celcius = (suhu_awal - 32) * 5/9
    elif unit_input == "Kelvin":
        suhu_celcius = suhu_awal - 273.15
    elif unit_input == "Reamur":
        suhu_celcius = suhu_awal * 5/4

    if unit_output == "Celcius":
        hasil = suhu_celcius
    elif unit_output == "Fahrenheit":
        hasil = (suhu_celcius * 9/5) + 32
    elif unit_output == "Kelvin":
        hasil = suhu_celcius + 273.15
    elif unit_output == "Reamur":
        hasil = suhu_celcius * 4/5

    hasil_label.config(text=f"{hasil:.2f} {unit_output}")

def clear_input():
    entry_suhu_awal.delete(0, tk.END)
    hasil_label.config(text="Hasil Konversi:")

root = tk.Tk()
root.title("Konversi Suhu")
root.geometry("270x250")
root.configure(bg="skyblue")

entry_suhu_awal_label = tk.Label(root, text="Suhu Awal:", bg="skyblue")
entry_suhu_awal_label.grid(row=0, column=0, padx=10, pady=5, sticky="W")
entry_suhu_awal = tk.Entry(root)
entry_suhu_awal.grid(row=0, column=1, padx=10, pady=5, sticky="W")

entry_suhu_awal_label = tk.Label(root, text="Unit Suhu Awal:", bg="skyblue")
entry_suhu_awal_label.grid(row=1, column=0, padx=10, pady=5, sticky="W")

input_unit_var = tk.StringVar()
input_unit_dropdown = ttk.Combobox(root, textvariable=input_unit_var, values=["Celcius", "Fahrenheit", "Kelvin", "Reamur"])
input_unit_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="W")
input_unit_dropdown.current(0)
input_unit_dropdown.configure(width=10)

entry_suhu_konversi_label = tk.Label(root, text="Suhu Konversi:", bg="skyblue") 
entry_suhu_konversi_label.grid(row=2, column=0, padx=10, pady=5, sticky="W")

output_unit_var = tk.StringVar()
output_unit_dropdown = ttk.Combobox(root, textvariable=output_unit_var, values=["Celcius", "Fahrenheit", "Kelvin", "Reamur"])
output_unit_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky="W")
output_unit_dropdown.current(1)
output_unit_dropdown.configure(width=10)

konversi_button = tk.Button(root, text="Konversi", command=konversi_suhu, bg="green", fg="white")
konversi_button.grid(row=3, column=0, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_input, bg="red", fg="white") 
clear_button.grid(row=3, column=1, pady=10)

hasil_label = tk.Label(root, text="Hasil Konversi:", bg="skyblue")
hasil_label.grid(row=4, column=0, pady=5)

root.mainloop()
