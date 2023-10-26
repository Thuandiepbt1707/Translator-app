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


Trans_btn = ttk.Button(root, text="Translate", command=Translate)
Trans_btn.place(x=10, y=520, width=215, height=45)

Clear_btn = ttk.Button(root, text="Clear all", command=Clear)
Clear_btn.place(x=235, y=520, width=215, height=45)

root.mainloop()
