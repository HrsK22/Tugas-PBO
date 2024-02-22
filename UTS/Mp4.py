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
root.configure(bg='dark grey')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (300/2)
y = (screen_height/2) - (200/2)

root.geometry(f'300x200+{int(x)}+{int(y)}')

play_button = tk.Button(root, text="Play Video", command=play_video, bg='grey', fg='black', font=('Helvetica', 12))
play_button.pack(pady=50)

root.mainloop()
