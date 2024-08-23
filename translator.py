from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title('Language Translator')

# Set the window to full-screen
root.state('zoomed')  # For Windows

# Main frame
frame1 = Frame(root, relief=RIDGE, borderwidth=5, bg='#8AAAE5')
frame1.pack(fill=BOTH, expand=True)

# Heading
Label(frame1, text='Language Translator', font=("Helvetica", 30, "bold"), fg="black", bg="#8AAAE5").pack(pady=(20, 10), anchor='n')

def translate():
    lang_1 = text_entry1.get(1.0, "end-1c")
    cl = choose_language.get()

    if lang_1 == '':
        messagebox.showerror("Language Translator", "Enter the text")
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(lang_1, dest=cl)
        text_entry2.insert('end', output.text)

def clear():
    text_entry1.delete(1.0, "end")
    text_entry2.delete(1.0, "end")

# Combobox for language selection
a = tk.StringVar()
auto_select = ttk.Combobox(frame1, width=30, textvariable=a, state="readonly", font=('verdana', 12, 'bold'))
auto_select['values'] = ('Auto Select',)
auto_select.place(relx=0.09, rely=0.15)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(frame1, width=30, textvariable=l, state='readonly', font=('verdana', 12, 'bold'))
choose_language['values'] = (
    "Afrikaans", "Akan", "Albanian", "Amharic", "Arabic", "Armenian", "Assamese", "Aymara", "Azerbaijani", "Bambara",
    "Bangla", "Basque", "Belarusian", "Bhojpuri", "Bosnian", "Bulgarian", "Burmese", "Catalan", "Cebuano", "Central Kurdish",
    "Chinese (Simplified)", "Chinese (Traditional)", "Corsican", "Croatian", "Czech", "Danish", "Divehi", "Dogri", "Dutch",
    "English", "Esperanto", "Estonian", "Ewe", "Filipino", "Finnish", "French", "Galician", "Ganda", "Georgian", "German",
    "Goan Konkani", "Greek", "Guarani", "Gujarati", "Haitian Creole", "Hausa", "Hawaiian", "Hebrew", "Hindi", "Hmong",
    "Hungarian", "Icelandic", "Igbo", "Iloko", "Indonesian", "Irish", "Italian", "Japanese", "Javanese", "Kannada", "Kazakh",
    "Khmer", "Kinyarwanda", "Korean", "Krio", "Kurdish", "Kyrgyz", "Lao", "Latin", "Latvian", "Lingala", "Lithuanian",
    "Luxembourgish", "Macedonian", "Maithili", "Malagasy", "Malay", "Malayalam", "Maltese", "Manipuri (Meitei Mayek)",
    "Māori", "Marathi", "Mizo", "Mongolian", "Nepali", "Northern Sotho", "Norwegian", "Nyanja", "Odia", "Oromo", "Pashto",
    "Persian", "Polish", "Portuguese", "Punjabi", "Quechua", "Romanian", "Russian", "Samoan", "Sanskrit", "Scottish Gaelic",
    "Serbian", "Shona", "Sindhi", "Sinhala", "Slovak", "Slovenian", "Somali", "Southern Sotho", "Spanish", "Sundanese",
    "Swahili", "Swedish", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Tigrinya", "Tsonga", "Turkish", "Turkmen",
    "Ukrainian", "Urdu", "Uyghur", "Uzbek", "Vietnamese", "Welsh", "Western Frisian", "Xhosa", "Yiddish", "Yoruba", "Zulu"
)
choose_language.place(relx=0.6, rely=0.15)
choose_language.current(0)

# Text entry boxes
text_entry1 = Text(frame1, width=50, height=15, borderwidth=5, relief=RIDGE, font=("verdana", 15))
text_entry1.place(relx=0.05, rely=0.25)

text_entry2 = Text(frame1, width=50, height=15, borderwidth=5, relief=RIDGE, font=("verdana", 15))
text_entry2.place(relx=0.55, rely=0.25)

# Buttons
btn_frame = Frame(frame1, bg='#8AAAE5')
btn_frame.place(relx=0.05, rely=0.75)

btn1 = Button(btn_frame, text="Translate", command=translate, relief=RAISED, borderwidth=2, font=("verdana", 15, "bold"), bg='#FFFFFF', fg="black", cursor="hand2")
btn1.pack(side=LEFT, padx=10)

btn2 = Button(btn_frame, text="Clear", command=clear, relief=RAISED, borderwidth=2, font=("verdana", 15, "bold"), bg='#FFFFFF', fg="black", cursor="hand2")
btn2.pack(side=LEFT, padx=10)

root.mainloop()
