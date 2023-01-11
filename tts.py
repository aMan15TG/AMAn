import pyttsx3
from gtts import gTTS
from tkinter import *
import os
speaker=pyttsx3.init()

def talk(text):
    speaker.say(text)
    speaker.runAndWait()

def tts():
    txt=(a1.get())
    str(txt)
    talk(txt)

root=Tk()
a=StringVar()
root.title("Text To Speech")
root.configure(bg="lightgreen")
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d"%(width,height))

x1=Label(root,text="Text To Speech Reconization",font=("solid",20,"bold"),bg="blue")
x1.grid(row=1,column=5)
x2=Label(root,text="Enter any text and i speak this text",font=("solid",20,"bold"),bg="green")
x2.grid(row=9,column=5)
a1=Entry(root,bg="skyblue",width=30,font=("arial",30,"bold"))
a1.grid(row=11,column=5)

def download():
    language = "en"
    obj1 = gTTS(text=a1.get(),
                 lang=language)
    obj1.save("convert.wav")
    os.system("convert.wav")


b1=Button(root,text="click to Talk",height=4,width=12,bd=5,font=("solid",8),activeforeground="orange",activebackground="green",command=tts)
c1=Button(root,text="click to download",height=4,width=18,bd=5,font=("solid",8),activeforeground="orange",activebackground="green",command=download)
b1.grid(row=30,column=4)
c1.grid(row=30,column=5)
root.mainloop()

