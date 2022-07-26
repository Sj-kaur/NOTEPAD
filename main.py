from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension= ".txt", filetypes=[("All Files", "*.*"),("Text Documents","*.txt")])
    
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f = open(file,'r')
        TextArea.insert(1.0,f.read())
        f.close()
    


def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + "- Notepad")
            tmsg.showinfo("FYI","File Saved")

    else:
        f = open(file,'w')
        f.write(TextArea.get(1.0,END))
        f.close()
        tmsg.showinfo("FYI","File Saved")
    
def undo():
    TextArea.edit_undo()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def delete():
    TextArea.delete(0.0,END)

def help():
    tmsg.showinfo("Help","Please visit - Notepad.md for more information")

def feedback():
    value = tmsg.askquestion("Notepad Feedback","Please tell us... Was your experince good?")
    if value == "yes":
        msg = "Thankyou for your feedback 😊"
    else:
        msg = "Sorry for inconvenience 😓, we'll try to resolve the problem soon!"
    tmsg.showinfo("Feedback", msg)

def aboutNotepad():
    tmsg.showinfo("Notepad","Notepad by Simarjeet Kaur(26-07-2022) ")


if __name__ == "__main__":
    root = Tk()
    root.geometry("1000x500")
    root.wm_iconbitmap("C:\SIMAR\Photos/notepad.ico")
    root.title("Untitled - Notepad")

    TextArea = Text(root,font= "Lucida 13 ")
    TextArea.pack(fill=BOTH,expand=True)
    file = None
    
    scrollbar = Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT , fill=Y)
    TextArea.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command= TextArea.yview)

    Menubar = Menu(root)

    FileMenu = Menu(Menubar,tearoff= 0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label = "Open File", command= openFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Save", command=save)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command =  quit)
    Menubar.add_cascade(label="File",menu=FileMenu)

    EditMenu = Menu(Menubar, tearoff=0)
    EditMenu.add_command(label="Undo",command= undo)
    EditMenu.add_separator()
    EditMenu.add_command(label="Cut",command= cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    EditMenu.add_command(label="Delete", command=delete)
    Menubar.add_cascade(label="Edit",menu=EditMenu)

    HelpMenu = Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="View Help",command= help)
    HelpMenu.add_command(label="Feedback",command= feedback)
    HelpMenu.add_separator()
    HelpMenu.add_command(label="About Notepad",command= aboutNotepad)
    Menubar.add_cascade(label="Help",menu=HelpMenu)

    root.config(menu=Menubar)


    root.mainloop()