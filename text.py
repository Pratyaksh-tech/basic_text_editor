from tkinter import *
from tkinter import filedialog , colorchooser , messagebox , font
from tkinter.font import Font
from tkinter import ttk
import os
from PIL import ImageTk , Image


root = Tk()
root.title("ABCD")
root.geometry("900x700")

main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu)
file_menu2 = Menu(main_menu)
file_menu3 = Menu(main_menu)
file_menu4 = Menu(main_menu)

sub1 = Menu(file_menu , tearoff=False)
sub2 = Menu(file_menu2 , tearoff=False)
sub3 = Menu(file_menu3 , tearoff=False)
sub4 = Menu(file_menu4 , tearoff=False)



main_menu.add_cascade(label="File" , menu=sub1)
main_menu.add_cascade(label="Edit" , menu=sub2)
main_menu.add_cascade(label="View" , menu=sub3)
main_menu.add_cascade(label="Help" , menu=sub4)


new_i = Image.open('new.png')
new_i2 = Image.open('save.png')
new_i3 = Image.open('open.png')
new_i4 = Image.open('exit.png')

resize_new1 = new_i.resize((20 , 20) , Image.ANTIALIAS)
resize_new2 = new_i2.resize((20 , 20) , Image.ANTIALIAS)
resize_new3 = new_i3.resize((20 , 20) , Image.ANTIALIAS)
resize_new4 = new_i4.resize((20 , 20) , Image.ANTIALIAS)

new_c = ImageTk.PhotoImage(resize_new1)
new_c2 = ImageTk.PhotoImage(resize_new2)
new_c3 = ImageTk.PhotoImage(resize_new3)
new_c4 = ImageTk.PhotoImage(resize_new4)

def opengl():
    op = filedialog.askopenfilename(initialdir='/c/' , title="Select File" , filetypes=(("txt files" , "*.txt") , ("all files" , "*.*")))
    try:
       with open(op , 'r') as t:
    	   tex.delete(1.0 , END)
    	   tex.insert(1.0 , t.read())
    except FileNotFoundError:
         return

def save():
    global op
    try:
        url = filedialog.asksaveasfile(mode='w' , defaultextension='.txt' , filetypes=(("txt files" , "*.txt") , ("all files" , "*.*")))
        cont2 = tex.get(1.0 , END)
        url.write(cont2)
        url.close()

    except:
        pass

def new_f():
	tex.delete(1.0 , END)

sub1.add_command(label="New.." , image=new_c , compound=LEFT , accelerator='ctrl+N' , command=new_f)
sub1.add_command(label="Save" , image=new_c2 , compound=LEFT , accelerator='ctrl+A' , command=save)
sub1.add_command(label="Open" , image=new_c3 , compound=LEFT , accelerator='ctrl+V' , command=opengl)
sub1.add_command(label="Exit" , image=new_c4 , compound=LEFT , accelerator='ctrl+H' , command=root.quit)

change = 'Arial'
change2 = 10

def fon(event=None):
	global change
	change = box.get()
	tex.config(font=(change , change2))

def fon2(event=None):
	global change2
	change2 = box2.get()
	tex.config(font=(change , change2))

fame = font.families()

box = ttk.Combobox(root , value=fame , state='readonly' , font=(23) , width=15)
box.set("Choose Font")
box.place(x=4 , y=7)

box2 = ttk.Combobox(root , value=[10 , 22 , 43 , 54 , 65 , 76 , 87 , 98] , state='readonly' , font=(23) , width=13)
box2.set("Choose Size")
box2.place(x=170 , y=7)

fg = Image.open('fore.png')
resize_newfg = fg.resize((40 , 33) , Image.ANTIALIAS)
new_fg = ImageTk.PhotoImage(resize_newfg)


def change():
	color = colorchooser.askcolor()[1]
	tex.config(fg=color)

left = Image.open('left.png')
resize_left = left.resize((40 , 33) , Image.ANTIALIAS)
new_left = ImageTk.PhotoImage(resize_left)

right = Image.open('right.png')
resize_right = right.resize((40 , 33) , Image.ANTIALIAS)
new_right = ImageTk.PhotoImage(resize_right)

center = Image.open('center.png')
resize_center = center.resize((40 , 33) , Image.ANTIALIAS)
new_center = ImageTk.PhotoImage(resize_center)

os = Image.open('os.png')
resize_os = os.resize((40 , 33) , Image.ANTIALIAS)
new_os = ImageTk.PhotoImage(resize_os)

moon = Image.open('moon.png')
resize_moon = moon.resize((40 , 33) , Image.ANTIALIAS)
new_moon = ImageTk.PhotoImage(resize_moon)

sun = Image.open('day.png')
resize_day = sun.resize((40 , 33) , Image.ANTIALIAS)
new_day = ImageTk.PhotoImage(resize_day)

def left():
    what = tex.get(1.0 , END)
    tex.tag_config('left' , justify=LEFT)
    tex.delete(1.0 , END)
    tex.insert(INSERT , what , 'left')

def center():
    what = tex.get(1.0 , END)
    tex.tag_config('center' , justify=CENTER)
    tex.delete(1.0 , END)
    tex.insert(INSERT , what , 'center')

def right():
    what = tex.get(1.0 , END)
    tex.tag_config('right' , justify=RIGHT)
    tex.delete(1.0 , END)
    tex.insert(INSERT , what , 'right')



def os():
    root2 = Tk()
    root2.title("ABCD")
    root2.geometry("800x600")

    moonNo = Image.open('folder.png')
    resize_moonNo = moonNo.resize((40 , 33) , Image.ANTIALIAS)
    new_moonNo = ImageTk.PhotoImage(resize_moonNo)

    btn1 = ttk.Button(root2, text="Folder", image=new_moonNo)
    btn1.pack(pady=10, padx=10)

    mainloop()

root.config(bg="SystemButtonFace")
def night():
    btn_ni['bg'] = "#373737"
    btn_os.config(bg="black")
    tex.config(bg="#373737")
    sub1.config(bg="#373737")
    root.config(bg="black")

def day():
    btn_ni['bg'] = "SystemButtonFace"
    btn_os.config(bg="SystemButtonFace")
    tex.config(bg="white")
    sub1.config(bg="SystemButtonFace")
    root.config(bg="SystemButtonFace")


btn_fg = ttk.Button(root , image=new_fg , command=change)
btn_fg.place(x=320 , y=6)

btn_left = ttk.Button(root , image=new_left , command=left)
btn_left.place(x=380 , y=6)

btn_center = ttk.Button(root , image=new_center , command=center)
btn_center.place(x=440 , y=6)

btn_right = ttk.Button(root , image=new_right , command=right)
btn_right.place(x=500 , y=6)

btn_os = Button(root , image=new_os , command=os , borderwidth=0)
btn_os.place(x=580 , y=8)

btn_ni = Button(root , image=new_moon , command=night , bg=None)
btn_ni.place(x=650 , y=6)

btn_da = Button(root , image=new_day , command=day , bg=None)
btn_da.place(x=720 , y=6)

box.bind("<<ComboboxSelected>>" , fon)
box2.bind("<<ComboboxSelected>>" , fon2)

tex = Text(root)
tex.config(wrap='word' , relief=FLAT)

scroll = Scrollbar(tex)
tex.focus_set()
scroll.pack(fill=Y , side=RIGHT)
tex.pack(fill=BOTH , expand=True , pady=55)
scroll.config(command=tex.yview)

tex.config(yscrollcommand=scroll.set)


mainloop()
