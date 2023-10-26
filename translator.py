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

root.mainloop()
