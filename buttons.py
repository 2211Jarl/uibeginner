from tkinter import *
from tkinter.messagebox import askyesno
import sqlite3


ws=Tk()
ws.title("Sending email")

bg = PhotoImage(file = "zanger.png")

canvas1 = Canvas( ws, width = 1920, height = 1080)

canvas1.pack(fill = "both", expand = True)

canvas1.create_image( 0, 0, image = bg, anchor = "nw")

canvas1.create_text( 
    900, 100, 
    text = "Hello Zangers!!!",
    font=('Roboto', 60, 'bold'),
    fill="light green"
    )

#Create a db
conn=sqlite3.connect('address_book.db')
#create cursor
c=conn.cursor()
#create table
'''c.execute(""" CREATE TABLE addresses(
        first_name text, 
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer)""")
'''

conn.commit()

def popup():
    askyesno("ALERT!!","Confirm Email?")

def submit():
    #clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    pin.delete(0, END)

"""Label(
    ws,
    text='Hello \n Zangers!!!',
    font=('Georgia', 20),
    padx=10,
    pady=10,
    bg='#116562',
    fg='yellow'
    ).pack(expand=True)"""

def send_email():
    root=Tk()
    emailtxt=Text(root, height=20, width=40)
    emailtxt.pack()
    sendbtn=Button(root, text="Send", font=("Roboto"), command=popup)
    sendbtn.pack()
    root.mainloop()


button1=Button(
            ws,
            text='Send Email',
            font=('Roboto', 15,),
            padx=7,
            pady=7,
            bg='#116562',
            fg='yellow',
            activebackground='#4a7abc',
            activeforeground='white',
            command=send_email
            )

button1_canvas=canvas1.create_window( 850, 550, 
                                       anchor = "nw",
                                       window = button1)

lbl = Label(ws, text = "")
lbl.pack()


#creating Textboxes
f_name=Entry(ws ,width=30)
canvas1.create_window(1000, 230, window=f_name )
l_name=Entry(ws,width=30)
canvas1.create_window(1000, 270, window=l_name )
address=Entry(ws,width=30)
canvas1.create_window(1000, 310, window=address )
city=Entry(ws,width=30)
canvas1.create_window(1000, 350, window=city )
state=Entry(ws,width=30)
canvas1.create_window(1000, 390, window=state )
pin=Entry(ws,width=30)
canvas1.create_window(1000, 430, window=pin )
enter_email= Entry(ws,width=30)


#Labels
f_name_label=canvas1.create_text(800, 230, text = "First Name" , font=('Roboto',25,'bold'), fill="light blue")
#canvas1.create_window(100, 230, window=f_name_label)
l_name_label=canvas1.create_text(800, 270, text = "Last Name", font=('Roboto',25,'bold'), fill="light blue")
#canvas1.create_window(100, 250, window=l_name_label)
ad_label=canvas1.create_text(800, 310, text = "Address    ", font=('Roboto',25,'bold'), fill="light blue")
#canvas1.create_window(100, 270, window=ad_label)
city_label=canvas1.create_text(800, 350, text = "City            ", font=('Roboto',25,'bold'), fill="light blue")
#canvas1.create_window(100, 290, window=city_label)
state_label=canvas1.create_text(800, 390, text = "State          ", font=('Roboto',25,'bold'), fill="light blue")
#canvas1.create_window(100, 310, window=state_label)
pin_label=canvas1.create_text(800, 430, text = "Pincode     ", font=('Roboto',25,'bold'), fill="light blue")
#canvas1.create_window(100, 330, window=pin_label)

#input text box for sending email
"""inputtxt = Text(ws,
                   height = 20,
                   width = 40)
        
inputtxt_canvas=canvas1.create_window(750, 550,
                                       anchor="nw",
                                       window=inputtxt)"""

#submit button
submit_btn=Button(ws,
            text='Add record to database?',
            font=('Roboto', 15),
            padx=3,
            pady=3,
            bg='#116562',
            fg='yellow',
            activebackground='#4a7abc',
            activeforeground='white',
            command=submit)
#submit_btn.grid(row=6, column=0, columnspan=2, pady=300, padx=100, ipadx= 200)

submit_btn_canvas=canvas1.create_window( 780, 480, 
                                       anchor = "nw",
                                       window = submit_btn)

conn.close()
ws.mainloop()