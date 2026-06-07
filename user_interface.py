from cProfile import label
from tkinter import *
from tkinter import BooleanVar
from tkinter.ttk import Progressbar
from turtledemo.clock import clockface
from turtledemo.penrose import start

from PythonStart.multithread import count
from classworks.filepahs import file

#SOME MODULES NEED TO BE IMPORTED AGAIN BECAUSE THEY ARE SUB MODULES
#EXAMPLE COLORCHOOSER,MESSAGEBOX


#widgets=GUI elements such as button, textbox,labels,images
#Window=serves as a container to hold or contain widgets

#window1=Tk()
#window1.geometry("500x400")
#window1.title("Eyiram Agbo")
#pic1=PhotoImage(file="screenshot.png")
#window1.iconphoto(True,pic1)
#window1.config(background="green")
#window1.mainloop()
#Label:is an area widget that has hold texts and/or an image within a window


#window2=Tk()
#window2.geometry("500x500")
#window2.title("Skipper")
#pic2=PhotoImage(file="Screenshot (1).png")
#window2.iconphoto(True,pic2)
#window2.config(background="black")
#label=Label(window2,
#            text="Skipper",
#            font=("Arial",30,"italic")
#            ,fg="red",
#            bg="white"
#            ,relief=RAISED
#            ,bd=8
#            ,padx=10
#            ,pady=10
#            ,image=pic2
#            ,compound="top"
#            )

#label.pack()
#window2.mainloop()


#count=0
#def click():
#    global count
#    count+=1
#    print(count)

#button=Button(window3,text="Click"
#              ,command=click
#              ,font=("Arial",10)
#              ,fg="red",
#              bg="green"
#              ,activebackground="green"
#              ,activeforeground="red",
#              state=ACTIVE,
#              image=pic4,
#              compound="top")
#button.pack()
#label=Label(window3,text="Asare"
#            ,font=("Arial",20,"bold")
#            ,bg="red"
#            ,fg="blue"
#            ,relief=RAISED
#            ,bd=5
#            ,padx=30
#            ,pady=30
#             ,image=(pic3,
#            compound="top")
#count=0
#def click():
#    global count
#    count+=1
#    print(count)
#button=Button(window3,
#              text="Like"
#              ,font=("Arial",12,"bold")
#              ,bg="blue"
#              ,fg="white"
#              ,image=pic4
#              ,compound="top"
#              ,command=click)
#button.pack()
#label.pack()
#Entry widget
#def submit():
#    username=entry.get()
#    print(f"Hello {username}")
#    entry.config(state=DISABLED)
#def delete():
#        entry.delete(0,END)
#def backspace():
#    entry.delete(len(entry.get())-1,END)
#entry=Entry(window3
#            ,font=("Arial",10)
#            ,fg="blue"
#            ,bg="white"
#            ,show="*")
#entry.insert(0,"Name")
#button=Button(window3
#              ,text="Submit"
#              ,command=submit
#              )
#button2=Button(window3
#              ,text="Delete"
#              ,command=delete
#               )
#button3=Button(window3
#              ,text="Backspace"
#              ,command=backspace
#               )

#entry.pack(side="left")
#button.pack(side="right")
#button2.pack(side="right")
#button3.pack(side="right")
#def submit():
#    username=entry.get()
#    print(username)
#    entry.config(state=DISABLED)

#def delete():
#    entry.delete(0,END)

#def backspace():
#    entry.delete(len(entry.get())-1,END)
#entry=Entry(window3,
#            font=("Roman",12)
#            ,fg="red"
#            ,bg="white"
#            ,show="a"
#            )
#button1=Button(window3,
#              text="Submit"
#              ,command=submit)
#button2=Button(window3,
#              text="Delete"
#              ,command=delete)
#button3=Button(window3,
#              text="backspace"
#              ,command=backspace)
#entry.pack(side="right")
#button1.pack(side="left")
#button2.pack(side="left")
#button3.pack(side="left")

#CheckBoxes
#x=BooleanVar()
#def display():
#    if(x.get()):
#        print("You agree")
#    else:
#        print("You dont agree")
#checkbutton=Checkbutton(window3,
#                        text="I agree to something"
#                        ,variable=x
#                        ,onvalue=True
#                        ,offvalue=False
#                        ,command=display
#                        ,font=("Arial",12)
#                        ,fg="green"
#                        ,bg="red"
#                        ,activeforeground="green",
#                        activebackground="red"
#                        ,pady=5
#                        ,padx=5
#                        ,image=pic4
#                        ,compound="right")


#checkbutton.pack()

#RADIOBUTTON
#food=["Pizza","Rice","Jollof"]
#def order():
#    if x.get()==0:
#        print("You ordered pizza")
#    elif x.get()==1:
#        print("You ordered Rice")
#    elif x.get() == 2:
#        print("You ordered Jollof")
#x=IntVar()
#for i in range(len(food)):
#    radiobutton = Radiobutton(window3,
#                              text=food[i]
#                              ,variable=x
#                              ,value=i
#                              ,padx=5,
#                              pady=5,
#                              font=("Roman",12)
#                              ,indicatoron=0,
#                              width=20
#                              ,command=order)
#    radiobutton.pack(anchor=W)
#SCALE
#def submit():
#    print(f"The temperature is {scale.get()} degree celcius")
#scale=Scale(window3,
#           from_=0
#            ,to=50
#            ,length=300
#            ,orient="vertical"
#            ,font=("Arial",20)
#            ,tickinterval=10
#            ,showvalue=0
#            ,troughcolor="#69EAFE"
#            ,fg="#FF1C00",
#            bg="black"
#            ,
#            )
#scale.set(37)
#scale.config(state=ACTIVE)
#button=Button(window3,
#              text="Submit"
#              ,command=submit)
#scale.pack()
#button.pack()
#def submit():
#    print(f"You are {scale.get()} years old")
#scale=Scale(window3,
#            from_=15
#            ,to=40
#            ,length=200
#            ,orient="vertical"
#            ,tickinterval=5
#            ,showvalue=0
#            ,troughcolor = "#69EAFE"
#            ,fg="pink"
#            ,bg="black"
#            ,font=("Roman" ,18)
#            ,width=20
#)
#scale.set(25)
#button=Button(window3,
#              text="Submit"
#              ,command=submit)
#scale.pack()
#button.pack()

#ListBox
#listbox=Listbox(window3,
#                bg='#f7ffde'
#                ,font=("Constantia",20)
#                ,width=10
#                ,selectmode=MULTIPLE
#                )
#listbox.pack()
#listbox.insert(1,"Jollof")
#listbox.insert(2,"Waakye")
#listbox.insert(3,"Rice")
#listbox.insert(4,"Banku")
#listbox.insert(5,"Yam")
#listbox.insert(5,"Bobo")
#listbox.config(height=listbox.size())
#def submit():
#   item= listbox.get(listbox.curselection())
#   print(f"You have ordered {item}")#

#def add():
#    listbox.insert(listbox.size(),entry.get())
#    listbox.config(height=listbox.size())


#def delete():
#    listbox.delete(listbox.curselection())
#    listbox.config(height=listbox.size())

#button=Button(window3,text="Submit"
#              ,command=submit)
#button.pack()

#entry=Entry(window3,)
#entry.pack()

#button1=Button(window3,text="Add"
#              ,command=add)
#button1.pack()

#button2=Button(window3,text="Delete"
#              ,command=delete)
#button2.pack()


#listbox=Listbox(window3,
#                font=("Arial",16,"bold")
#                ,width=20,
#                bg="blue"
#                ,fg="white"
#                ,selectmode=MULTIPLE)
#listbox.insert(1,"Wake up")
#listbox.insert(2,"Wash dishes")
#listbox.insert(3,"Watch youtube")
#listbox.insert(4,"Eat breakfast")
#listbox.insert(5,"Make Dinner")
#listbox.config(height=listbox.size())
#listbox.pack()


#def submit():
#    duties=[]
#    for i in listbox.curselection():
#        duties.insert(i,listbox.get(i))
#    for i in duties:
#        print(i)
#def add():
#    listbox.insert(listbox.size(),entry.get())
#    listbox.config(height=listbox.size())

#def delete():
#    for i in reversed(listbox.curselection()):
#        listbox.delete(i)
#    listbox.config(height=listbox.size())

#submitbutton=Button(window3
#                    ,text="Submit"
#                    ,command=submit)

#submitbutton.pack()
#entry=Entry(window3,)
#entry.pack()

#addbutton=Button(window3
#                    ,text="Add"
#                    ,command=add)
#addbutton.pack()

#deletebutton=Button(window3
#                    ,text="Delete"
#                    ,command=delete)
#deletebutton.pack()

#MESSAGEBOXES

from tkinter import messagebox
#def click():
     #    messagebox.showinfo(title="This is a messageBox"
    #                    ,message="You are doing great")
#   while(True):
#       messagebox.showwarning(title="Warning"
 #                             , message="You have a virus")
# messagebox.showerror(title="Error"
#                      ,message="Something went wrong")
#   if messagebox.askokcancel(title="ok cancel"
#                       ,message="Do u want?"):
#    print("You did a thing")
#   else:
#    print("You cancelled the thing")
    #if messagebox.askretrycancel(title="ask cancel"
     #                         ,message="Do you want to do it"):
     #   print("You retried a thing")
    #else:
    #    print("You cancelled a thing")
#    if messagebox.askyesno(title="yes or no"
#                        ,message='Do you like cake?'):
#        print("I like cake")
#    else:
#        print("I do not like cake")
#     answer=messagebox.askquestion(title="questions"
#                               ,message="Do you like drinking?")
#     if answer=="yes":
#         print("I like drinking too")
#     else:
#         print("Why do you not like drinking?")
#       answer=messagebox.askyesnocancel(title="ask no cancel"
#                                 ,message="Do you like coding?"
#                                 ,icon="error"      )
#       if (answer==True):
#         print("You should take it seriously")
#       elif (answer==False):
#           print("You should and like it")
#       else:
#           print("Please answer the question")
#button=Button(window3,
#              text="Click"
#              ,command=click
#              )
#button.pack()

#def click():
#    messagebox.showinfo(title="Show information"
#                        ,message="How are you doing?")
#    messagebox.showerror(title="Show error"
#                    , message="This is an error")
#     messagebox.showwarning(title="Show warning"
#                    , message="You have a virus?")
#      if messagebox.askokcancel(title="ok and cancel"
#                    , message="How are you doing?"):
#          print("I am good")
#      else:
#          print("Find something to make yourself feel better")
#       answer=messagebox.askquestion(title="questions"
#                    , message="How are you doing?")
#       if answer=="yes":
#           print("I am doing well")
#       else:
#           print("Not too much into this")
#       answer=messagebox.askyesnocancel(title="Ask yes no cancel"
#                    , message="Do you like women?")
#       if (answer==True):
#           print("That is my guy")
#       elif (answer==False):
#           print('Whoa you are a suspect')
#       else:
#           print("Dude just answer the question")

#button=Button(window3
#              ,text="Click"
#              ,command=click)
#button.pack()

#COLORCHOOSER
from tkinter import colorchooser #submodel
#def click():
#   color= colorchooser.askcolor()
#   hexacol=color[1]
#   window3.config(bg=hexacol)
#button=Button(window3,text="click"
#              ,command=click)
#button.pack()
#def click():
#    color=colorchooser.askcolor()
#    hexcolor=color[1]
#    button.config(fg=hexcolor)
#    window3.config(bg=hexcolor)
#button=Button(window3
#              ,text="click"
#              ,command=click)
#button.pack(side="left")


#TEXTAREA
#textarea=Text(window3,
#              bg="light yellow",
#              font=("Ink Free",12),
#              width=40,
#              height=10,
#              pady=5
#              ,padx=5,
#             fg="purple")
#textarea.pack()
#def submit():
#    input=textarea.get("1.0",END)
#    print(input)
#button=Button(window3
#              ,text="Submit"
#              ,command=submit)
#button.pack()

#FILEDIALOGUE
from tkinter import filedialog
#def openfile():
#    filepath=filedialog.askopenfilename(initialdir="C:\\Users\\Abgo Eyiram Asare\\PythonProjecthelloworld\\PythonStart"
#                                        ,title="Openfile"
#                                        ,filetypes=(("Python files","*.py"),
#                                        ("All files","*.*")))
#    file=open(filepath,"r")
#    print(file.read())
#    file.close()
#button=Button(window3
#              ,text="open"
#              ,command=openfile
#              )
#button.pack()
#def openfile():
#    filepath=filedialog.askopenfilename(
#        initialdir="C:\\Users\\Abgo Eyiram Asare\\PycharmProjects\\PythonStart"
#        , title="Openfile"
#        ,filetypes=(("Python files","*.py"),
#                    ("All files","*.*")))
#    file=open(filepath,"r")
#    print(file.read())
#    file.close()
#def savefile():
#    filepath=filedialog.asksaveasfile(initialdir="C:\\Users\\Abgo Eyiram Asare\\PycharmProjects\\PythonStart",
#                                          defaultextension=".txt",
#                                          filetypes=[("Text files",".txt"),
#                                                     ("Python Files",".py"),
#                                                     ("Music Files",".mp3"),
#                                                     ("Video Files", ".mp4"),
#                                                     ("HTML Files", ".html"),
#                                                     ("pdf Files", ".pdf"),
#                                                     ("All files",".*")])
#    if filepath is None:
#        return
#    filetext=str(text.get(1.0,END))
#    #filetext=input("I am texting something")
#    filepath.write(filetext)
#    filepath.close()


window3=Tk()
window3.geometry("400x400")
window3.title("Skipper")
pic3=PhotoImage(file="Screenshot (1).png")
window3.iconphoto(True,pic3)
window3.config(bg="black")
#Button creation
pic4=PhotoImage(file="like (1).png")
#button=Button(window3,
#              text="Save",
#              command=savefile
#              )
#button.pack()
#text=Text(window3,)
#text.pack()
#def savefile():
#    filepath=filedialog.asksaveasfile(initialdir="C:\\Users\\Abgo Eyiram Asare\\Desktop\\works",
#        defaultextension=".txt",
#        filetypes=[("Text files",".txt"),
#                   ("Python files",".py"),
#                   ("PDF files",".pdf"),
#                   ("Music files",".mp3"),
#                   ("Html files",".html")
#        ]
#    )
#    filetext=text.get(1.0,END)
#    filepath.write(filetext)
#    file.close()

#button=Button(window3,
#              text="Save",
#              command=savefile)
#button.pack()
#text=Text(window3)
#text.pack()

#MENUBAR
#def openfile():
#    print("I am opening a file")

#def savefile():
#    print("I am saving a file")

#menubar=Menu(window3)
#window3.config(menu=menubar)
#filemenu=Menu(menubar,tearoff=0,font=("MV Boli",10))
#menubar.add_cascade(label="File",menu=filemenu)
#filemenu.add_command(label="Open" ,command=openfile)
#filemenu.add_command(label="Save",command=savefile)
#filemenu.add_separator()
#filemenu.add_command(label="Exit",command=quit)
#def copy():
#    print("You have copied some text")

#def paste():
#    print("You have paste some text")

#def cut():
#    print("You have cut some text")

#editmenu=Menu(menubar,tearoff=0,font=("MV Boli",10))
#menubar.add_cascade(label="Edit",menu=editmenu)
#editmenu.add_command(label="Copy",command=copy,image=pic4,compound="left")
#editmenu.add_command(label="Paste",command=paste)
#editmenu.add_command(label="Cut",command=cut)

#def openfile():
#    print("This is for opening a file")

#def savefile():
#    print("This is for saving a file")

#menubar=Menu(window3)
#window3.config(menu=menubar)
#filemenu=Menu(menubar,tearoff=0,font=("Sans Seriff",10))
#menubar.add_cascade(label="File",menu=filemenu)
#filemenu.add_command(label="Open",command=openfile)
#filemenu.add_command(label="Save",command=savefile)
#filemenu.add_separator()
#filemenu.add_command(label="Exit",command=quit)

#def movefile():
#    print("This is for moving a file")

#def pullfile():
#    print("This is for pulling a file")

#def pushfile():
#    print("This is for pushing a file")
#editmenu=Menu(menubar,tearoff=0,font=("Sans Seriff",10))
#menubar.add_cascade(label="Edit",menu=editmenu)
#editmenu.add_command(label="Move",command=movefile)
#editmenu.add_command(label="Pull",command=pullfile)
#editmenu.add_command(label="Push",command=pushfile)

#def save():
#    filepath=filedialog.asksaveasfile(initialdir="C:\\Users\\Abgo Eyiram Asare\\Desktop\\data",
#                                       defaultextension=".txt",
#                                      filetypes=[("Text files",".txt"),
#                                                 ("Python files",".py"),
#                                                 ("Html Files",".html"),
#                                                 ("Audio files",".mp3"),
#                                                 ("All files",".*")])
#    filetext=str(text.get(1.0,END))
#    filepath.write(filetext)
#    filepath.close()

#button=Button(window3,
#              text="Save",
#              command=save)
#button.pack()
#text=Text(window3)
#text.pack()

#def open():
#    pass
#menubar=Menu(window3)
#window3.config(menu=menubar)
#filemenu=Menu(menubar,tearoff=0)
#menubar.add_cascade(label="File",menu=filemenu)
#filemenu.add_command(label="Open",command=open)
#filemenu.add_command(label="Save",command=open)
#filemenu.add_command(label="Exit",command=open)

#FRAMES
#frame=Frame(window3,bg="pink",bd=5,relief=SOLID)
#frame.pack(side="bottom")
#button1=Button(frame,
#              text="W",
#              font=("Consolas",20),
#              width=3)
#button1.pack(side="top")
#button2=Button(frame,
#              text="A",
#              font=("Consolas",20),
#              width=3)
#button2.pack(side="left")
#button3=Button(frame,
#              text="S",
#              font=("Consolas",20),
#              width=3)
#button3.pack(side="left")
#button4=Button(frame,
#              text="D",
#              font=("Consolas",20),
#              width=3)
#button4.pack(side="left")

#NEW WINDOWS
#def create_window():
#    new_window=Tk()
#    window3.destroy()
#Button(window3,text="Create window",command=create_window).pack()

#TABS

from tkinter import ttk

#notebook=ttk.Notebook(window3)
#tab1=Frame(notebook)
#tab2=Frame(notebook)
#notebook.add(tab1,text="First tab")
#notebook.add(tab2,text="second tab")
#notebook.pack(expand=True,fill="both")
#Label(tab1,text="Hello this is my first tab",width=20,height=10).pack()
#Label(tab2,text="Hello this is my second tab",width=20,height=10).pack()

#GRID GEOMETRY
#titlelabel=Label(window3,text="Enter your information",font="Roman").grid(row=0,column=0,columnspan=2)

#firstnamelabel=Label(window3,text="First Name :",width=30,bg="red").grid(row=1,column=0)
#fNameEntry=Entry(window3).grid(row=1,column=1)

#lastnamelabel=Label(window3,text="last Name :",bg="green").grid(row=2,column=0)
#lNameEntry=Entry(window3).grid(row=2,column=1)

#emaillabel=Label(window3,text="Email :",bg="blue",width=50).grid(row=3,column=0)
#emailEntry=Entry(window3).grid(row=3,column=1)

#submitbutton=Button(window3,text="Submit").grid(row=4,column=0,columnspan=2)

#notebook=ttk.Notebook(window3)
#tab1=Frame(notebook)
#tab2=Frame(notebook)
#notebook.add(tab1,text="First Tab")
#notebook.add(tab2,text='Second tab')
#notebook.pack()
#from tkinter import *
#from tkinter.ttk import  *
#import time

#def load():
#    task=10
#    x=0
#    while (x<task):
#        time.sleep(1)
#        bar['value'] += 10
#        x+=1
#        window3.update_idletasks()

#bar=Progressbar(window3,orient="horizontal",length=350)
#bar.pack(pady=10)

#button=Button(window3,text="Load",command=load).pack()

#def load():
#    GB=100
#    download=0
#    speed=2
#    while(download<GB):
#        time.sleep(0.50)
#        bar['value']+=(speed/GB)*100
#        download+=speed
#        percent.set(str(int((download/GB)*100))+"%")
#        text.set(str(download)+"/"+str(GB)+" GB completed")
#        window3.update_idletasks()

#bar=Progressbar(window3,length=350,orient="horizontal")
#bar.pack(pady=10)

#percent=StringVar()
#text=StringVar()

#label=Label(window3,textvariable=percent)
#label.pack()
#tasklabel=Label(window3,textvariable=text)
#tasklabel.pack()

#button=Button(window3,text="Load",command=load)
#button.pack()

#CANVAS for simple graphs,plots and images
#canvas=Canvas(window3,height=500,width=500)
#canvas.pack()
#canvas.create_line(0,0,500,500,fill="blue",width=5)
#canvas.create_line(0,500,500,0,fill="red",width=5)
#canvas.create_rectangle(50,50,250,350,fill="purple")
#points=[250,0,500,500,0,500,150,0,210,500]
#canvas.create_polygon(points,fill="yellow",outline='black',width=5)
#canvas.create_arc(0,0,500,500,style=PIESLICE,start=90,extent=180)
#canvas.create_oval(50,50,300,300)
#canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
#canvas.create_arc(0,0,500,500,fill="white",start=180,extent=180,width=10)
#canvas.create_oval(190,190,310,310,fill="white",width=10)

#KEY EVENTS
#def dosomething(event):
#    #print(f"You pressed {event.keysym}")
#    label.config(text=event.keysym)
#label=Label(window3,font=("Helvetica",100))
#label.pack()
#window3.bind("<Key>",dosomething)
#def down(event):
#    print(f"I am a Kobby")
#    label.config(text=event.keysym)
#window3.bind("<Key>",down)
#label=Label(window3,font=("Roman",100))
#label.pack()

#MOUSE EVENT
#def do(event):
#    print(f"mouse cordinates {event.x} ,{event.y}")
#window3.bind("<ButtonRelease>",do)
#window3.bind("<Enter>",do)
#window3.bind("<Leave>",do)
#window3.bind("<Motion>",do)
#Button-1=left

#def do(event):
#    total=0
#    print(f"I pressed {event.keysym}")
#    label.config(text=f"{event.x},{event.y}")
#   total=event.x +event.y
#   label2.config(text=f"{total}")
#window3.bind("<Motion>",do)
#label=Label(window3,font=("Sans Seriff",100))
#label.pack()
#label2=Label(window3,font=("Sans Seriff",100))
#label2.pack()

#DRAG AND DROP WIDGETS

#def drag(event):
#    widget=event.widget
#    widget.x=event.x
#    widget.y=event.y
#def drag2(event):#Motio n of the mouse
#    widget=event.widget
#    x=widget.winfo_x()-widget.x+event.x
#    y=widget.winfo_y()-widget.y+event.y
#    widget.place(x=x,y=y)

#label=Label(window3,width=10,bg="red",height=5)
#label.place(x=0,y=0)
#label.bind("<Button-1>",drag)
#label.bind("<B1-Motion>",drag2)


#label2=Label(window3,width=10,bg="green",height=5)
#label2.place(x=100,y=100)
#label2.bind("<Button-1>",drag)
#label2.bind("<B1-Motion>",drag2)

#def select(event):
#    widget=event.widget
#    widget.x=event.x
#    widget.y=event.y

#def move(event):
#    widget=event.widget
#    x=widget.winfo_x()-widget.x+event.x
#    y=widget.winfo_y()-widget.y + event.y
#    widget.place(x=x,y=y)

#label1=Label(window3,height=5,width=10,bg="red")
#label1.place(x=0,y=0)
#label1.bind("<Button-1>",select)
#label1.bind("<B1-Motion>",move)

#label2=Label(window3,height=5,width=10,bg="blue")
#label2.place(x=100,y=100)
#label2.bind("<Button-1>",select)
#label2.bind("<B1-Motion>",move)


#MOVING IMAGES ON A WINDOW
#def moveup(event):
 #   label.place(x=label.winfo_x(),y=label.winfo_y()-10)

#def movedown(event):
#    label.place(x=label.winfo_x(),y=label.winfo_y()+10)

#def moveleft(event):
#    label.place(x=label.winfo_x()-10,y=label.winfo_y())

#def moveright(event):
#    label.place(x=label.winfo_x()+10,y=label.winfo_y())

#label=Label(window3,image=pic4)
#label.place(x=0,y=0)
#window3.bind("<w>",moveup)
#window3.bind("<a>",moveleft)
#window3.bind("<s>",movedown)
#window3.bind("<d>",moveright)
#window3.bind("<Up>",moveup)
#window3.bind("<Left>",moveleft)
#window3.bind("<Right>",moveright)
#window3.bind("<Down>",movedown)


#MOVING IMAGES ON A CANVAS
#def move_up(event):
#    canvas.move(pic5,0,-10)
#def move_left(event):
#    canvas.move(pic5,-10,0)
#def move_down(event):
#    canvas.move(pic5, 0, 10)
#def move_right(event):
#    canvas.move(pic5, 10, 0)


#window3.bind("<w>",move_up)
#window3.bind("<a>",move_left)
#window3.bind("<s>",move_down)
#window3.bind("<d>",move_right)

#window3.bind("<Up>",move_up)
#window3.bind("<Left>",move_left)
#window3.bind("<Down>",move_down)
#window3.bind("<Right>",move_right)

#canvas=Canvas(window3,width=500,height=500)
#canvas.pack()
#pic5=canvas.create_image(0,0,image=pic4,anchor=NW)

#def move_up(event):
#   label.place(x=label.winfo_x(),y=label.winfo_y()-10)

#def move_left(event):
#   label.place(x=label.winfo_x()-10,y=label.winfo_y())

#def move_down(event):
#   label.place(x=label.winfo_x(),y=label.winfo_y()+10)

#def move_right(event):
#   label.place(x=label.winfo_x()+10,y=label.winfo_y())


#label=Label(window3,image=pic4)
#label.place(x=0,y=0)
#window3.bind("<Up>",move_up)
#window3.bind("<Left>",move_left)
#window3.bind("<Down>",move_down)
#window3.bind("<Right>",move_right)

#def move_up(event):
#    canvas.move(cavpic,0,-10)
#def move_down(event):
#    canvas.move(cavpic,0,10)
#def move_left(event):
#    canvas.move(cavpic,-10,0)
#def move_right(event):
#    canvas.move(cavpic,10,0)

#canvas=Canvas(window3,width=500,height=500,bg="green")
#canvas.pack()
#cavpic=canvas.create_image(0,0,image=pic4,anchor=NW)
#window3.bind("<Up>",move_up)
#window3.bind("<Down>",move_down)
#window3.bind("<Left>",move_left)
#window3.bind("<Right>",move_right)


import time
WIDTH=500
HEIGHT=500
xVelocity=4
yVelocity=2
canvas=Canvas(window3,width=WIDTH,height=HEIGHT)
canvas.pack()
my_image=canvas.create_image(0,0,image=pic4,anchor=NW)

image_width=pic4.width()
image_height=pic4.height()
while True:
    coordinates=canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0] >= (WIDTH - (image_width * 4)) or coordinates[0] < 0):
       xVelocity = xVelocity * -1

    if(coordinates[1] >= (HEIGHT - (image_height * 4)) or coordinates[1] < 0):
      yVelocity = yVelocity * -1
    canvas.move(my_image,xVelocity,yVelocity)
    window3.update()
    time.sleep(0.01)



window3.mainloop()








