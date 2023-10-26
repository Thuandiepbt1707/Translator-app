from tkinter import *
from textblob import TextBlob
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

root=Tk()
root.title("Translate - 207CT47832 - Ngọ Văn Long")
root.geometry("460x580")
root.iconphoto(False, PhotoImage(file="Google_Translate_logo.svg.png"))

LangValue = list(LANGUAGES.values())
LangKey = LANGUAGES.keys()

title=ttk.Label(root, text="Translator", font=("Robot", 30))
title.grid(row=0)

seclect_from = ttk.Combobox(root, values=LangValue, state="r")
seclect_from.grid(column=0, row=1,  padx=20, pady=10)
seclect_from.set("english")

icon_to = ttk.Label(root,text=">>>")
icon_to.grid(column=1, row=1, padx=15, pady=10)

seclect_to = ttk.Combobox(root, values=LangValue, state="r")
seclect_to.grid(column=3, row=1,  padx=20, pady=10)
seclect_to.set("vietnamese")

input_from = Text()
input_from.place(x=10, y=100, width=440, height=200)

input_to = Text()
input_to.place(x=10, y=310, width=440, height=200)

def Translate():
    global LANGUAGES
    lang_in = seclect_from.get()
    lang_out = seclect_to.get()
    input1 = input_from.get(1.0,END)
    if (input1):
        for i,j in LANGUAGES.items():
            if (j == lang_in):
                Lang_in = i
        for i,j in LANGUAGES.items():
            if (j == lang_out):
                Lang_out = i
        word = TextBlob(input1)
        # Lang_in = word.detect_language()
        text_late = word.translate(from_lang=str(Lang_in), to=str(Lang_out))
        input_to.delete(1.0, END)
        input_to.insert(END,text_late)
def Clear():
    input_from.delete(1.0,END)   
    input_to.delete(1.0,END)   

Trans_btn = ttk.Button(root, text="Translate", command=Translate)
Trans_btn.place(x=10, y=520, width=215, height=45)

Clear_btn = ttk.Button(root, text="Clear all", command=Clear)
Clear_btn.place(x=235, y=520, width=215, height=45)

root.mainloop()
