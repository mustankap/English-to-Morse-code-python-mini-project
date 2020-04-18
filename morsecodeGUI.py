from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, '')
# print(CONFIG_PATH)


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

# create database
conn = sqlite3.connect('conversiondata.db')
# create cursor on database
c = conn.cursor()

c.execute(
    ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='con' ''')

# if the count is 1, then table exists
if c.fetchone()[0] != 1:
    c.execute('''CREATE TABLE con(letter text NOT NULL, PRIMARY KEY(letter))''')
    x = ('A = '+morse('a'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('B = '+morse('b'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('C = '+morse('c'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('D = '+morse('d'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('E = '+morse('e'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('F = '+morse('f'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('G = '+morse('g'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('H = '+morse('h'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('I = '+morse('i'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('J = '+morse('j'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('K = '+morse('k'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('L = '+morse('l'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('M = '+morse('m'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('N = '+morse('n'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('O = '+morse('o'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('P = '+morse('p'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('Q = '+morse('q'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('R = '+morse('r'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('S = '+morse('s'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('T = '+morse('t'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('U = '+morse('u'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('V = '+morse('v'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('W = '+morse('w'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('X = '+morse('x'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('Y = '+morse('y'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('Z = '+morse('z'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('1 = '+morse('1'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('2 = '+morse('2'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('3 = '+morse('3'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('4 = '+morse('4'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('5 = '+morse('5'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('6 = '+morse('6'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('7 = '+morse('7'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('8 = '+morse('8'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('9 = '+morse('9'),)
    c.execute("INSERT INTO con VALUES(?)", x)
    x = ('0 = '+morse('0'),)
    c.execute("INSERT INTO con VALUES(?)", x)
else:
    print("con EXISTS!!!")


c.execute(
    ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='todd' ''')
# if the count is 1, then table exists
if c.fetchone()[0] != 1:
    c.execute('''CREATE TABLE todd(letter text NOT NULL, PRIMARY KEY(letter))''')
else:
    print("todd EXISTS!!!")

# commit the database
conn.commit()


# added photo
# can put many such variables in a list for image viewer
my_image = ImageTk.PhotoImage(Image.open(CONFIG_PATH + "mo2.jpg"))
my_label = Label(image=my_image)
my_label.grid(row=3, columnspan=2)


def ref():
    e1.insert(0, "")


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
        k = (s+d,)
        if len(s+d) > 0:
            c.execute('INSERT INTO todd VALUES(?)', k)
    else:
        t = ""
        for i in s:
            t += morse(i)
        e1.insert(0, t)
        k = (s+t,)
        if len(s+t) > 0:
            c.execute('INSERT INTO todd VALUES(?)', k)


def showtodd():
    c.execute("SELECT * FROM todd")
    rows = c.fetchall()
    return rows


def showcon():
    c.execute("SELECT * FROM con")
    rows = c.fetchall()
    return rows

# new window for seeing conversion table


def tab():
    top = Toplevel()
    global tab_pic
    top.iconbitmap('moiconic_xoU_icon.ico')
    tab_pic = ImageTk.PhotoImage(Image.open(
        "resize- c1587066260336897184convtab.jpg"))
    lab = Label(top, image=tab_pic).grid(row=0)

    bac_but = Button(top, text="back", bg="#58BFF0", padx="10",
                     pady="10", command=top.destroy).grid(row=1)

    return


# title
my_label0 = Label(root, text="   The Morse Code Converter",
                  fg="#482EB9", font=('Times', 30), padx=50)
my_label0.grid(row=0, column=0)
# instruction to user
mylabel1 = Label(
    root, text="          ENTER YOUR SENTENCE (ENGLISH/MORSE) :", padx=60, pady=20)
mylabel1.grid(row=1)

# enter the english sentence
e1 = Entry(root, bg="#DCF9F9", fg="#3C057E", width=50,
           borderwidth=1, font=('Times', 19))
# check every character from string s that matches with the database
e1.grid(row=2, column=0, padx=15, pady=10)

# button to open another window
ct = Button(root, text="SEE THE CONVERSION TABLE:",
                       command=tab, bg="#58BFF0", padx="10", pady="10")
ct.grid(row=4, column=0)

# convert button
cv = Button(root, text="CONVERT",
                       command=convert, bg="#58BFF0", padx="10", pady="10")
cv.grid(row=5, column=0, columnspan=2)

# removeconnection
conn.close()

root.bind_all('<Key>', key)

root.mainloop()
