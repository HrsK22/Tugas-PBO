import tkinter as tk
from tkinter import ttk, scrolledtext
from googletrans import Translator

def translate_text():
    try:
        text_to_translate = entry.get()
        selected_language_name = destination_language.get()

        languages_info = {'Inggris': 'en', 'Sunda': 'su', 'Jawa': 'jw'}
        selected_language_code = languages_info.get(selected_language_name)

        if selected_language_code:
            translator = Translator()
            translated_text = translator.translate(text_to_translate, src='id', dest=selected_language_code).text

            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, translated_text + "\n")
        else:
            print("Kode bahasa tidak valid.")

    except Exception as e:
        print("Terjadi kesalahan:", e)


def set_style():
    style = ttk.Style()
    style.configure("TButton", padding=5, font=('Helvetica', 12))

root = tk.Tk()
root.title("Translator Bahasa")
root.minsize(width=400, height=300)
root.configure(bg="dark blue")

entry = tk.Entry(root, font=('Helvetica', 14))
entry.pack(pady=10)

languages_info = {'en': 'Inggris', 'su': 'Sunda', 'jw': 'Jawa'}
languages = list(languages_info.values())
destination_language = ttk.Combobox(root, values=languages, state="readonly", font=('Helvetica', 12))

destination_language.set('Inggris')
selected_language_code = [code for code, lang in languages_info.items() if lang == destination_language.get()][0]

destination_language.pack(pady=10)


translate_button = tk.Button(root, text="Terjemahkan", command=translate_text, bg="light blue", font=('Helvetica', 12))
translate_button.pack(pady=10)

# Result Text Widget
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, font=('Helvetica', 12))
result_text.pack(pady=10)

# Apply Style
set_style()

root.mainloop()
