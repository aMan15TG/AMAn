from tkinter import *
import random
import pyperclip
tk=Tk()
tk.geometry('300x300')
tk.configure(background='gray')
pswd=StringVar()
passlen=IntVar()
passlen.set(' ')
def password_generator():
    characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%^&*()_/.><'
    password=''
    if passlen.get()>=8:
        for i in range(passlen.get()):
            password+=random.choice(characters)
        pswd.set(password)
def copyclipboard():
    random_password = pswd.get()
    pyperclip.copy(random_password)
    Label(tk,text="Copied to Clipboard",bg="red").pack(pady=6)

Label(tk, text="Enter the number to get password \n (Minimum length should be 8)",bg='Blue',fg='white',font=("arial",20,"bold")).pack(pady=3)
Entry(tk, textvariable=passlen,width=20).pack(pady=3)
Label(tk, text="you get a strong Password)",bg='skyblue',fg='white',font=("arial",20,"bold")).pack(pady=4)

Button(tk, text="Generate Password", command=password_generator,bg='black',fg='white',font=("arial",20,"bold")).pack(pady=7)
Entry(tk, textvariable=pswd,width=20).pack(pady=3)
Button(tk, text="Copy to clipboard", command=copyclipboard,bg='black',fg='white',font=("arial",20,"bold")).pack()
Label(tk, text="IT is created by Aman Sharman)",bg='Blue',fg='white',font=("arial",30,"bold")).pack(pady=9)

tk.mainloop()