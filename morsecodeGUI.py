from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, '')


def revmorse(t):
    if t == ".-":
        return 'a'
    elif t == "-...":
        return 'b'
    elif t == "-.-.":
        return 'c'
    elif t == "-..":
        return 'd'
    elif t == ".":
        return 'e'
    elif t == "..-.":
        return 'f'
    elif t == "--.":
        return 'g'
    elif t == "....":
        return 'h'
    elif t == "..":
        return 'i'
    elif t == ".---":
        return 'j'
    elif t == "-.-":
        return 'k'
    elif t == ".-..":
        return 'l'
    elif t == "--":
        return 'm'
    elif t == "-.":
        return 'n'
    elif t == "---":
        return 'o'
    elif t == ".--.":
        return 'p'
    elif t == "--.-":
        return 'q'
    elif t == ".-.":
        return 'r'
    elif t == "...":
        return 's'
    elif t == "-":
        return 't'
    elif t == "..-":
        return 'u'
    elif t == "...-":
        return 'v'
    elif t == ".--":
        return 'w'
    elif t == "-..-":
        return 'x'
    elif t == "-.--":
        return 'y'
    elif t == "--..":
        return 'z'
    elif t == ".----":
        return '1'
    elif t == "..---":
        return '2'
    elif t == "...--":
        return '3'
    elif t == "....-":
        return '4'
    elif t == ".....":
        return '5'
    elif t == "-....":
        return '6'
    elif t == "--...":
        return '7'
    elif t == "---..":
        return '8'
    elif t == "----.":
        return '9'
    elif t == "-----":
        return '0'
    else:
        return " "


def morse(a):
    if a == 'a' or a == 'A':
        return ".-   "
    elif a == 'b' or a == "B":
        return "-...   "
    elif a == 'c' or a == "C":
        return "-.-.   "
    elif a == 'd' or a == "D":
        return "-..   "
    elif a == 'e' or a == "E":
        return ".   "
    elif a == 'f' or a == "F":
        return "..-.   "
    elif a == 'g' or a == "G":
        return "--.   "
    elif a == 'h' or a == "H":
        return "....   "
    elif a == 'i' or a == "I":
        return "..   "
    elif a == 'j' or a == "J":
        return ".---   "
    elif a == 'k' or a == "K":
        return "-.-   "
    elif a == 'l' or a == "L":
        return ".-..   "
    elif a == 'm' or a == "M":
        return "--   "
    elif a == 'n' or a == "N":
        return "-.   "
    elif a == 'o' or a == "O":
        return "---   "
    elif a == 'p' or a == "P":
        return ".--.   "
    elif a == 'q' or a == "Q":
        return "--.-   "
    elif a == 'r' or a == "R":
        return ".-.   "
    elif a == 's' or a == "S":
        return "...   "
    elif a == 't' or a == "T":
        return "-   "
    elif a == 'u' or a == "U":
        return "..-   "
    elif a == 'v' or a == "V":
        return "...-   "
    elif a == 'w' or a == "W":
        return ".--   "
    elif a == 'x' or a == "X":
        return "-..-   "
    elif a == 'y' or a == "Y":
        return "-.--   "
    elif a == 'z' or a == "Z":
        return "--..   "
    elif a == '1':
        return ".----   "
    elif a == '2':
        return "..---   "
    elif a == '3':
        return "...--   "
    elif a == '4':
        return "....-   "
    elif a == '5':
        return ".....   "
    elif a == '6':
        return "-....   "
    elif a == '7':
        return "--...   "
    elif a == '8':
        return "---..   "
    elif a == '9':
        return "----.   "
    elif a == '0':
        return "-----   "
    elif a == ' ':
        return "        "
    else:
        return a


def key(event):
    if event.keysym == 'Return':
        convert()


# created root window
root = Tk()

# title of main window
root.title("The Morse Code Converter")
# icon added at top left corner
root.iconbitmap(CONFIG_PATH+'moiconic_xoU_icon.ico')
# icon added at top left corner

# create database
conn = sqlite3.connect('conversiondata.db')
# create cursor on database
c = conn.cursor()


c.execute(
    ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='todd' ''')
# if the count is 1, then table exists
if c.fetchone()[0] != 1:
    c.execute('''CREATE TABLE todd(letter text NOT NULL)''')
    c.commit()
else:
    print("todd EXISTS!!!")


# added photo

my_image = ImageTk.PhotoImage(Image.open(CONFIG_PATH + "coolmorse4.jpg"))
my_label = Label(image=my_image)
my_label.grid(row=4, columnspan=3)


def ref():
    e1.delete(0, END)


def convert():

    s = e1.get()
    e1.delete(0, END)
    if s[0] == '.' or s[0] == '-':
        t = ""
        d = ""
        n = len(s)
        i = 0
        while i < n:
            if s[i] == " ":
                k = 0
                while i < n and s[i] == " ":
                    k += 1
                    i += 1
                if k > 3:
                    d += " "
            else:
                while i < n and s[i] != " ":
                    t += s[i]
                    i += 1
                d += revmorse(t)
                t = ""
        e1.insert(0, d)
        k = (s+" = "+d,)
        if len(s+d) > 0:
            c.execute('INSERT INTO todd VALUES(?)', k)
            conn.commit()
    else:
        t = ""
        for i in s:
            t += morse(i)
        e1.insert(0, t)
        k = (s+" = "+t,)
        if len(s+t) > 0:
            c.execute('INSERT INTO todd VALUES(?)', k)
            conn.commit()


def showtodd():
    c.execute("SELECT * FROM todd")
    rows = c.fetchall()
    top2 = Toplevel()
    t = ""
    for i in rows:
        t += str(i)
        t += '\n'
    lo = Label(top2, text=t)
    lo.grid(row=0)
    bac_but = Button(top2, text="BACK", bg="#58BFF0", padx="10",
                     pady="10", command=top2.destroy).grid(row=1)


# new window for seeing conversion table
def tab():

    top = Toplevel()
    global tab_pic
    top.iconbitmap(CONFIG_PATH+'moiconic_xoU_icon.ico')
    tab_pic = ImageTk.PhotoImage(Image.open(CONFIG_PATH +
                                            "resize-1587066260336897184convtab.jpg"))
    lab = Label(top, image=tab_pic).grid(row=0)

    bac_but = Button(top, text="BACK", bg="#58BFF0", padx="10",
                     pady="10", command=top.destroy).grid(row=1)

    return


# title
my_label0 = Label(root, text="           The Morse Code Converter",
                  fg="#482EB9", font=('Times', 30))
my_label0.grid(row=0, column=0)
# instruction to user
mylabel1 = Label(
    root, text="                                   ENTER YOUR SENTENCE (ENGLISH/MORSE) :", pady=5)
mylabel1.grid(row=1, column=0)


# enter the english sentence
e1 = Entry(root, bg="#DCF9F9", fg="#3C057E",
           borderwidth=1, font=('Times', 19), width=51)
# check every character from string s that matches with the database
e1.grid(row=2, column=0, padx=5, pady=10, columnspan=2)

# convert button
cv = Button(root, text="CONVERT!", command=convert,
            bg="#58BFF0", height=1)
cv.grid(row=2, column=2, padx=5, pady=10)

button_frame = Frame(root, width=75)
button_frame.grid(row=5, column=0, padx=5, pady=10)

df = Label(button_frame, text="                 ")
ct = Button(button_frame, text='Cheat Sheet',
            command=tab, bg="#58BFF0", width=25)
ref = Button(button_frame, text='Refresh', command=ref, bg="#58BFF0", width=25)
his = Button(button_frame, text='History',
             command=showtodd, bg="#58BFF0", width=25)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)

df.grid(row=0, column=0)
ct.grid(row=0, column=1, sticky=E, padx=10)
ref.grid(row=0, column=2)
his.grid(row=0, column=3, sticky=W, padx=10)


root.bind_all('<Key>', key)

root.mainloop()
c.close()
conn.close()
