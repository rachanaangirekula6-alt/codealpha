import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    source = source_language.get()
    target = target_language.get()

    try:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror(
            "Translation Error",
            f"Could not translate the text.\n\n{e}"
        )

def copy_text():
    translated = output_text.get("1.0", tk.END).strip()

    if translated:
        root.clipboard_clear()
        root.clipboard_append(translated)
        root.update()
        messagebox.showinfo("Copied", "Translated text copied!")

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x600")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)

tk.Label(
    root,
    text="Source Language:",
    font=("Arial", 12)
).pack()

source_language = ttk.Combobox(
    root,
    values=[
        "auto",
        "en",
        "te",
        "hi",
        "ta",
        "kn",
        "ml",
        "fr",
        "de",
        "es",
        "it",
        "ja",
        "ko",
        "zh"
    ],
    state="readonly",
    width=30
)
source_language.set("auto")
source_language.pack(pady=8)

tk.Label(
    root,
    text="Enter Text:",
    font=("Arial", 12)
).pack()

input_text = tk.Text(
    root,
    height=7,
    width=70,
    font=("Arial", 12)
)
input_text.pack(pady=10)

tk.Label(
    root,
    text="Target Language:",
    font=("Arial", 12)
).pack()

target_language = ttk.Combobox(
    root,
    values=[
        "en",
        "te",
        "hi",
        "ta",
        "kn",
        "ml",
        "fr",
        "de",
        "es",
        "it",
        "ja",
        "ko",
        "zh"
    ],
    state="readonly",
    width=30
)
target_language.set("te")
target_language.pack(pady=8)

translate_button = tk.Button(
    root,
    text="Translate",
    command=translate_text,
    font=("Arial", 12, "bold"),
    padx=25,
    pady=8
)
translate_button.pack(pady=15)

tk.Label(
    root,
    text="Translated Text:",
    font=("Arial", 12)
).pack()

output_text = tk.Text(
    root,
    height=7,
    width=70,
    font=("Arial", 12)
)
output_text.pack(pady=10)

copy_button = tk.Button(
    root,
    text="Copy Translation",
    command=copy_text,
    font=("Arial", 11),
    padx=20,
    pady=6
)
copy_button.pack(pady=10)

root.mainloop()