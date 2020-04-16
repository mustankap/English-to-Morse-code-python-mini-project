from tkinter import *
from PIL import ImageTk,Image
import sqlite3
#created root window
root = Tk()
#title of main window
root.title("The Morse Code Converter")
#icon added at top left corner
root.iconbitmap('moiconic_xoU_icon.ico')

#create database
conn=sqlite3.connect('conversiondata.db')
#create cursor on database
c=conn.cursor()

c.execute("""CREATE TABLES codes(

letter text,
code,text


   
)



"""


)
#commit the database
conn.commit()



#added photo
my_image=ImageTk.PhotoImage(Image.open("mo2.jpg"))#can put many such variables in a list for image viewer
my_label=Label(image=my_image)
my_label.grid(row=3,columnspan=2)

def convert():
    #cook your dish here!
    return


#new window for seeing conversion table
def tab():
    top=Toplevel()
    global tab_pic
    top.iconbitmap('moiconic_xoU_icon.ico')
    tab_pic=ImageTk.PhotoImage(Image.open("resize-1587066260336897184convtab.jpg"))
    lab=Label(top,image=tab_pic).grid(row=0)

    bac_but = Button(top, text="back", bg="#58BFF0", padx="10", pady="10",command=top.destroy).grid(row=1)

    return




#title
my_label0=Label(root,text="   The Morse Code Converter",fg="#482EB9",font=('Times',30),padx=50)
my_label0.grid(row=0,column=0)
#instruction to user
mylabel1=Label(root,text="             ENTER YOUR SENTENCE TO CONVERT IT INTO MORSE CODE!!  :",padx=60,pady=20)
mylabel1.grid(row=1)

#enter the english sentence
e=Entry(root, bg="#DCF9F9", fg="#3C057E",width=50,borderwidth=1,font=('Times',19))
s = e.get()
#check every character from string s that matches with the database
e.grid(row=2,column=0,padx=15,pady=10)

#button to open another window
submit_button=Button(root,text="SEE THE CONVERSION TABLE:",command=tab,bg="#58BFF0",padx="10",pady="10")
submit_button.grid(row=4,column=0)

#convert button
submit_button=Button(root,text="CONVERT !",command=convert,bg="#58BFF0",padx="10",pady="10")
submit_button.grid(row=4,column=0)

#removeconnection
conn.close()
root.mainloop()
