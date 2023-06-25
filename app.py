from asyncio.windows_events import NULL
import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title("Password Manager")
root.geometry('200x200')
root.resizable(width=False, height=False)

def retrievepassword():
    kw = keyword.get()
    sf = savefor.get()

    storage = open('storage.txt', 'r')
    lines = storage.readlines()
    count = 0
    for line in lines:
        rec = line.strip('\n').split(', ')
        if kw == rec[1] and sf == rec[2]:
            result.config(text=rec[0])
            break
        else:
            result.config(text="No record found")
            count+=1
        
        if not line:
            break

def storepassword():
    pw = password.get()
    kw = keyword.get()
    sf = savefor.get()
    
    if pw != '' or kw != '' or sf != '':
        with open('storage.txt', 'a') as file_object:    
            # Append text at file
            file_object.write(f"{pw}, {kw}, {sf}")
            file_object.write("\n")
        result.config(text="Password Saved")
    else:
        result.config(text="Fill out form")

pw_label = tk.Label(root, text="Password: ")
pw_label.pack()
password = tk.Entry(root, show="*", width=15)
password.pack()

kw_label = tk.Label(root, text="Keyword: ")
kw_label.pack()
keyword = tk.Entry(root, width=15)
keyword.pack()

sf_label = tk.Label(root, text="Save For: ")
sf_label.pack()
savefor = tk.Entry(root, width=15)
savefor.pack()

save = tk.Button(root, text="Save", command=storepassword)
save.pack()

retrieve = tk.Button(root, text="Retrieve", command=retrievepassword)
retrieve.pack()

result = tk.Label(root, text="-Result Here-")
result.pack()

root.mainloop()