from tkinter import *
import Backend

window = Tk()
window.wm_title('Players')

l1 = Label(window, text="Player_id")
l1.grid(row=0, column=0)

l2 = Label(window, text="Team_id")
l2.grid(row=0, column=2)

l3 = Label(window, text="First_name")
l3.grid(row=1, column=0)

l4 = Label(window, text="Last_name")
l4.grid(row=1, column=2)

l5 = Label(window, text="Age")
l5.grid(row=2, column=0)

l6 = Label(window, text="Salary")
l6.grid(row=2, column=2)

l7 = Label(window, text="Position")
l7.grid(row=3, column=0)

l8 = Label(window, text="Weight")
l8.grid(row=3, column=2)

l9 = Label(window, text="Height")
l9.grid(row=4, column=0)

l10 = Label(window, text="Avr_point")
l10.grid(row=4, column=2)

l11 = Label(window, text="Avr_asist")
l11.grid(row=5, column=0)

l12 = Label(window, text="Avr_rebound")
l12.grid(row=5, column=2)


id_text = StringVar()
e1 = Entry(window, textvariable=id_text)
e1.grid(row=0 , column=1)

team_id_text = StringVar()
e2 = Entry(window, textvariable=team_id_text)
e2.grid(row=0 , column=3)

first_name_text = StringVar()
e3 = Entry(window, textvariable=first_name_text)
e3.grid(row= 1, column=1)

last_name_text = StringVar()
e4 = Entry(window, textvariable=last_name_text)
e4.grid(row= 1, column=3)

age_text = StringVar()
e5 = Entry(window, textvariable=age_text)
e5.grid(row=2 , column=1)

salary_text = StringVar()
e6 = Entry(window, textvariable=salary_text)
e6.grid(row=2 , column=3)

position_text = StringVar()
e7 = Entry(window, textvariable=position_text)
e7.grid(row=3 , column=1)

weight_text = StringVar()
e8 = Entry(window, textvariable=weight_text)
e8.grid(row=3 , column=3)

height_text = StringVar()
e9 = Entry(window, textvariable=height_text)
e9.grid(row=4 , column=1)

avr_point_text = StringVar()
e10 = Entry(window, textvariable=avr_point_text)
e10.grid(row=4 , column=3)

avr_asist_text = StringVar()
e11 = Entry(window, textvariable=avr_asist_text)
e11.grid(row=5 , column=1)

avr_rebound_text = StringVar()
e12 = Entry(window, textvariable=avr_rebound_text)
e12.grid(row=5 , column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=6, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=6, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text="View all", width=12)
b1.grid(row=6, column=3)

b2 = Button(window, text="Search", width=12)
b2.grid(row=7, column=3)

b3 = Button(window, text="Add", width=12)
b3.grid(row=8, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=9, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=10, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=11, column=3)

window.mainloop()