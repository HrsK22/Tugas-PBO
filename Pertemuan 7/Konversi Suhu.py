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
    elif unit_input == "Rankine":
        suhu_celcius = (suhu_awal - 491.67) * 5/9

    if unit_output == "Celcius":
        hasil = suhu_celcius
    elif unit_output == "Fahrenheit":
        hasil = (suhu_celcius * 9/5) + 32
    elif unit_output == "Kelvin":
        hasil = suhu_celcius + 273.15
    elif unit_output == "Reamur":
        hasil = suhu_celcius * 4/5
    elif unit_output == "Rankine":
        hasil = (suhu_celcius + 273.15) * 9/5

    hasil_label.config(text=f"{hasil:.2f} {unit_output}")

def clear_input():
    entry_suhu_awal.delete(0, tk.END)
    hasil_label.config(text="Hasil Konversi:")

# Membuat GUI
app = tk.Tk()
app.title("Konversi Suhu")
app.geometry("270x250")


# Entry untuk nilai suhu awal
entry_suhu_awal_label = tk.Label(app, text="Suhu Awal:")
entry_suhu_awal_label.grid(row=0, column=0, padx=10, pady=5, sticky="W")
entry_suhu_awal = tk.Entry(app)
entry_suhu_awal.grid(row=0, column=1, padx=10, pady=5, sticky="W")

# Label Unit Awal
entry_suhu_awal_label = tk.Label(app, text="Unit Suhu Awal:")
entry_suhu_awal_label.grid(row=1, column=0, padx=10, pady=5, sticky="W")

# Dropdown untuk unit input
input_unit_var = tk.StringVar()
input_unit_dropdown = ttk.Combobox(app, textvariable=input_unit_var, values=["Celcius", "Fahrenheit", "Kelvin", "Reamur", "Rankine"])
input_unit_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="W")
input_unit_dropdown.current(0)
input_unit_dropdown.configure(width=10)

# Label Suhu Konversi
entry_suhu_konversi_label = tk.Label(app, text="Suhu Konversi:")
entry_suhu_konversi_label.grid(row=2, column=0, padx=10, pady=5, sticky="W")

# Dropdown untuk unit output
output_unit_var = tk.StringVar()
output_unit_dropdown = ttk.Combobox(app, textvariable=output_unit_var, values=["Celcius", "Fahrenheit", "Kelvin", "Reamur", "Rankine"])
output_unit_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky="W")
output_unit_dropdown.current(1)
output_unit_dropdown.configure(width=10)

# Tombol untuk konversi dan reset
konversi_button = tk.Button(app, text="Konversi", command=konversi_suhu)
konversi_button.grid(row=3, column=0, pady=10)

clear_button = tk.Button(app, text="Clear", command=clear_input)
clear_button.grid(row=3, column=1, pady=10)

# Label untuk hasil konversi
hasil_label = tk.Label(app, text="Hasil Konversi:")
hasil_label.grid(row=4, column=0, pady=5)

# Menjalankan aplikasi
app.mainloop()
