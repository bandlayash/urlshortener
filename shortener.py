import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("URL Shortener")
root.configure(bg="#49A")
url = StringVar()
url_addy = StringVar()

def urlshortener():
    urlAddy = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urlAddy)
    url_addy.set(url_short)

def copyurl():
    url_short = url_addy.get()
    pyperclip.copy(url_short)

f1 = ("poppins", 24, "bold underline")
f2 = ("poppins", 18, "bold")
f3 = ("poppins", 12, "normal")

Label(root, text="URL Shortener", font = f1, fg = "white", bg="#49A").pack(pady = 10)
Label(root, text = "Enter URL Below: ", font = f3, fg = "white", bg="#49A").pack(pady = 9)
Entry(root, textvariable = url).pack(pady = 5)
Button(root, text="Generate", command = urlshortener).pack(pady = 7)
Entry(root, textvariable = url_addy).pack(pady = 5)
Button(root, text="Copy", command = copyurl).pack(pady = 5) 
Label(root, text = "Enjoy!", font = f2, fg = "white", bg="#49A").pack(pady = 3)

root.mainloop()