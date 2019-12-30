
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
from tkinter.messagebox import askretrycancel
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
#///////////search//////////////
from wikipedia import wikipedia


def get_me():
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except:
        answer.insert(INSERT, "please check your internet connection or check your spelling")


#//////////////////////////////////////////////////
def newFile(event=""):
    global file
    root.title("Untitled - Info-Book")
    file = None
    TextArea.delete(1.0, END)


def openFile(event=""):
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile(event=""):
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def saveas():

    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp(event=""):
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))
def Undo():
    print(TextArea.edit_undo())
def about():
    showinfo("Notepad", "Note Pade (beta version)-0.00x1\n"
                        "Developed by VISHAL KUMAR\n"
                        "Contact-vishalkumar0579@gmail.com")
def rate():
    value = askquestion("Rate us","Did you had a good experience")
    if value == "yes":
        showinfo("Rate us","Great!! Rate us App store")
    else:
        showinfo("Rate us","Tell us what went wrong, contact us through our servers")
def guide(event=""):
    top = Toplevel()
    top.title("Guide")
    top.geometry("540x530")
    l = Label(top, text="Steps To GUIDE your self:-\n"
                        "\n"
                        "1)Menu-File-open = to open file\n\n"
               "2)Menu-Fiel-New = to create a new file\n\n"
               "3)Menu-File-save =to save file\n\n"
               "4)Menu-File-exit =to exit\n\n"
               "5)Menu-Edit-copy =to copy file\n\n"
               "6)Menu-Edit-cut =to cut file\n\n"
               "7)Menu-Edit-paste =to paste file\n\n"
               "8)Menu-Edit-undo =to Undo file\n\n"
                        "9)Menu-Edit-Redu =to save file\n\n"
                        "10)Menu-Help-About note pade = give information about notepade\n\n"
                        "11)Menu-Help-Rate us =to Rate the applicatio\n\n"
                        "12)Menu-Help-Report =to report any difficulties\n\n"
                        "13)Menu-Help-Guide =to guide the user\n",font=12,bg="light grey")
    l.pack(side=TOP)
def report():
    ans = askretrycancel("connecting to server", "wait while we establish connection with the main server")
    if ans:
        s = simpledialog.askstring("Your Report", "Tell us the difficulties you faced")
        print(s)
    else:
        showinfo("Report","Servers is busy.Please try again later")



if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Info-Book")
    # root.wm_iconbitmap("download3.ico")
    root.geometry("444x488")

    #Add TextArea
    TextArea = Text(root, font="lucida 13",undo=True)
    file = None
    TextArea.pack(expand=True, fill=BOTH,)
#///////////////////////////////////////////////////////////////////


    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    root.bind('<Control-n>', newFile)
    FileMenu.add_command(label="New   (ctrl+n)", command=newFile)

    #To Open already existing file
    root.bind('<Control-o>', openFile)
    FileMenu.add_command(label="Open   (ctrl+o)", command = openFile)

    # To save the current file
    root.bind('<Control-s>', saveFile)
    FileMenu.add_command(label = "Save   (ctrl+s)", command = saveFile)
    FileMenu.add_command(label="Save as", command=saveas)
    FileMenu.add_separator()
    root.bind('<Control-q>', quitApp)
    FileMenu.add_command(label = "Exit  (ctrl+q)", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut   (ctrl+x)", command=cut)
    EditMenu.add_command(label = "Copy  (ctrl+c)", command=copy)
    EditMenu.add_command(label = "Paste  (ctrl+p)", command=paste)
    EditMenu.add_command(label = "Undo   (ctrl+z)", command=Undo)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    HelpMenu.add_command(label="Rate Us", command=rate)
    HelpMenu.add_command(label="Report", command=report)
    root.bind('<Control-g>', guide)
    HelpMenu.add_command(label="Guide   (ctrl+g)", command=guide)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    # ////////////////////////////////////////////////////
    topframe = Frame(root,pady=10)
    entry = Entry(topframe, border=2)
    entry.pack(side=LEFT, padx=5, pady=5)

    b = Button(topframe, text="search", command=get_me)
    b.pack()

    topframe.pack(side=TOP, pady=10)

    bottomframe = Frame(root, height=10, width=10)

    scroll = Scrollbar(bottomframe)
    scroll.pack(side=RIGHT, fill=Y)
    answer = Text(bottomframe, wrap=WORD, pady=10, width=100, height=100,yscrollcommand=scroll.set)
    scroll.config(command=answer.yview)
    answer.pack(fill=BOTH)
    bottomframe.pack(side=BOTTOM)
    # ////////////////////////////////////////////////////

    root.mainloop()
