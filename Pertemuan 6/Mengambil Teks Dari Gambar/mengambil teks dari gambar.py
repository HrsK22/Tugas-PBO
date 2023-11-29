import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import pytesseract

class TextFromImageApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text from Image App")

        self.image_path = None

        self.create_widgets()

    def create_widgets(self):
        # Frame utama
        main_frame = ttk.Frame(self.root, padding=(20, 10))
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        open_button = ttk.Button(main_frame, text="Buka Gambar", command=self.buka_gambar_dialog)
        open_button.grid(column=0, row=0, pady=10)

        extract_button = ttk.Button(main_frame, text="Ekstrak Teks", command=self.ekstrak_teks)
        extract_button.grid(column=0, row=1, pady=5)

        # Frame untuk menampilkan gambar
        image_frame = ttk.Frame(main_frame, padding=(0, 10))
        image_frame.grid(column=0, row=2)

        self.label = ttk.Label(image_frame)
        self.label.grid(column=0, row=0)

        # Frame untuk menampilkan teks
        text_frame = ttk.Frame(main_frame, padding=(0, 10))
        text_frame.grid(column=0, row=3)

        self.text_display = tk.Text(text_frame, height=10, width=50, wrap="word")
        self.text_display.grid(column=0, row=0)

    def buka_gambar_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)

    def ekstrak_teks(self):
        if self.image_path:
            image = Image.open(self.image_path)
            text = pytesseract.image_to_string(image)
            self.text_display.delete(1.0, tk.END) 
            self.text_display.insert(tk.END, text)

    def display_image(self, image_path):
        img = Image.open(image_path)
        img.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(img)
        self.label.configure(image=photo)
        self.label.image = photo

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TextFromImageApp()
    app.run()
