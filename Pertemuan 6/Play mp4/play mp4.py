import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

def play_video():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        video = VideoFileClip(file_path)
        video.preview()

root = tk.Tk()
root.title("MP4 Player")

# Tambahkan warna latar belakang dan padding pada root window
root.configure(bg='#E6E6FA')
root.geometry('300x200')

# Gaya tombol untuk memberikan tampilan yang lebih menarik
button_style = {'font': ('Helvetica', 12, 'bold'), 'bg': '#4CAF50', 'fg': 'white', 'activebackground': '#45a049'}

play_button = tk.Button(root, text="Play Video", command=play_video, **button_style)
play_button.pack(pady=20)

# Tambahkan label atau judul untuk aplikasi
title_label = tk.Label(root, text="Simple MP4 Player", font=('Helvetica', 16, 'bold'), bg='#E6E6FA')
title_label.pack(pady=10)

root.mainloop()
