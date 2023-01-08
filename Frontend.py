from tkinter import *
import Backend


### PLAYERS FRONTEND ###
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END,selected_tuple[0])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[1])
    e3.delete(0, END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END,selected_tuple[3])
    e5.delete(0, END)
    e5.insert(END,selected_tuple[4])
    e6.delete(0, END)
    e6.insert(END,selected_tuple[5])
    e7.delete(0, END)
    e7.insert(END,selected_tuple[6])
    e8.delete(0, END)
    e8.insert(END,selected_tuple[7])
    e9.delete(0, END)
    e9.insert(END,selected_tuple[8])
    e10.delete(0, END)
    e10.insert(END,selected_tuple[9])
    e11.delete(0, END)
    e11.insert(END,selected_tuple[10])
    e12.delete(0, END)
    e12.insert(END,selected_tuple[11])


def view_command():
    list1.delete(0, END)
    for row in Backend.view_player():
        list1.insert(END, row)


def search_command():
    list1.delete(0,END)
    for row in Backend.search_player(team_id_text.get(), first_name_text.get(),
                                     last_name_text.get(), age_text.get(), salary_text.get(),
                                     position_text.get(), weight_text.get(), height_text.get(),
                                     avr_point_text.get(), avr_asist_text.get(), avr_rebound_text.get()):
        list1.insert(END, row)


def add_command():
    Backend.insert_player(team_id_text.get(), first_name_text.get(),
                          last_name_text.get(), age_text.get(), salary_text.get(),
                          position_text.get(), weight_text.get(), height_text.get(),
                          avr_point_text.get(), avr_asist_text.get(), avr_rebound_text.get())

    list1.delete(0, END)
    view_command()


def delete_command():
    Backend.delete_player(selected_tuple[0])
    view_command()


def update_command():
    Backend.update_player(selected_tuple[0], team_id_text.get(), first_name_text.get(),
                          last_name_text.get(), age_text.get(), salary_text.get(),
                          position_text.get(), weight_text.get(), height_text.get(),
                          avr_point_text.get(), avr_asist_text.get(), avr_rebound_text.get())


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

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=6, column=3)

b2 = Button(window, text="Search", width=12, command=search_command)
b2.grid(row=7, column=3)

b3 = Button(window, text="Add", width=12, command=add_command)
b3.grid(row=8, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=9, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=10, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=11, column=3)


### TEAMS FRONTEND ###

def get_selected_row_team(event):
    global selected_tuple_team
    index=list1_t.curselection()[0]
    selected_tuple_team = list1_t.get(index)
    e1_t.delete(0, END)
    e1_t.insert(END, selected_tuple_team[0])
    e2_t.delete(0, END)
    e2_t.insert(END, selected_tuple_team[1])
    e3_t.delete(0, END)
    e3_t.insert(END, selected_tuple_team[3])
    e4_t.delete(0, END)
    e4_t.insert(END, selected_tuple_team[3])
    e5_t.delete(0, END)
    e5_t.insert(END, selected_tuple_team[4])


def view_command_team():
    list1_t.delete(0, END)
    for row in Backend.view_team():
        list1_t.insert(END, row)


def search_command_team():
    list1_t.delete(0, END)
    for row in Backend.search_team(captain_id_text.get(), coach_id_text.get(),
                                     team_name_text.get(), city_text.get()):
        list1_t.insert(END, row)


def add_command_team():
    Backend.insert_team(captain_id_text.get(), coach_id_text.get(),
                          team_name_text.get(), city_text.get())

    list1_t.delete(0, END)
    view_command_team()


def delete_command_team():
    Backend.delete_team(selected_tuple_team[0])
    view_command_team()


def update_command_team():
    Backend.update_team(selected_tuple_team[0], captain_id_text.get(), coach_id_text.get(),
                          team_name_text.get(), city_text.get())


team_windows = Tk()
team_windows.wm_title('Teams')

l1_t = Label(team_windows, text="Team_id")
l1_t.grid(row=0, column=0)

l2_t = Label(team_windows, text="Captain_id")
l2_t.grid(row=0, column=2)

l3_t = Label(team_windows, text="Coach_id")
l3_t.grid(row=1, column=0)

l4_t = Label(team_windows, text="Team_name")
l4_t.grid(row=1, column=2)

l5_t = Label(team_windows, text="City")
l5_t.grid(row=2, column=0)


team_id_text = StringVar()
e1_t = Entry(team_windows, textvariable=team_id_text)
e1_t.grid(row=0, column=1)

captain_id_text = StringVar()
e2_t = Entry(team_windows, textvariable=captain_id_text)
e2_t.grid(row=0, column=3)

coach_id_text = StringVar()
e3_t = Entry(team_windows, textvariable=coach_id_text)
e3_t.grid(row= 1, column=1)

team_name_text = StringVar()
e4_t = Entry(team_windows, textvariable=team_name_text)
e4_t.grid(row= 1, column=3)

city_text = StringVar()
e5_t = Entry(team_windows, textvariable=city_text)
e5_t.grid(row=2, column=1)


list1_t = Listbox(team_windows, height=6, width=35)
list1_t.grid(row=6, column=0, rowspan=6, columnspan=2)

sb1_t = Scrollbar(team_windows)
sb1_t.grid(row=6, column=2, rowspan=6)

list1_t.configure(yscrollcommand=sb1_t.set)
sb1_t.configure(command=list1_t.yview)

list1_t.bind('<<ListboxSelect>>', get_selected_row_team)

b1_t = Button(team_windows, text="View all", width=12, command=view_command_team)
b1_t.grid(row=6, column=3)

b2_t = Button(team_windows, text="Search", width=12, command=search_command_team)
b2_t.grid(row=7, column=3)

b3_t = Button(team_windows, text="Add", width=12, command=add_command_team)
b3_t.grid(row=8, column=3)

b4_t = Button(team_windows, text="Update", width=12, command=update_command_team)
b4_t.grid(row=9, column=3)

b5_t = Button(team_windows, text="Delete", width=12, command=delete_command_team)
b5_t.grid(row=10, column=3)

b6_t = Button(team_windows, text="Close", width=12, command=team_windows.destroy)
b6_t.grid(row=11, column=3)


### STAFF FRONTEND ###

def get_selected_row_staff(event):
    global selected_tuple_staff
    index = staff_list1.curselection()[0]
    selected_tuple_staff = staff_list1.get(index)
    e1_s.delete(0, END)
    e1_s.insert(END, selected_tuple_staff[0])
    e2_s.delete(0, END)
    e2_s.insert(END, selected_tuple_staff[1])
    e3_s.delete(0, END)
    e3_s.insert(END, selected_tuple_staff[3])
    e4_s.delete(0, END)
    e4_s.insert(END, selected_tuple_staff[3])
    e5_s.delete(0, END)
    e5_s.insert(END, selected_tuple_staff[4])
    e6_s.delete(0, END)
    e6_s.insert(END, selected_tuple_staff[5])
    e7_s.delete(0, END)
    e7_s.insert(END, selected_tuple_staff[6])


def view_command_staff():
    staff_list1.delete(0, END)
    for row in Backend.view_staff():
        staff_list1.insert(END, row)


def search_command_staff():
    staff_list1.delete(0, END)
    for row in Backend.search_staff(staff_team_id_text.get(), staff_role_text.get(),
                                    staff_first_name_text.get(), staff_last_name_text.get(), staff_salary_text.get(),
                                    staff_sex_tex.get()):
        staff_list1.insert(END, row)


def add_command_staff():
    Backend.insert_staff(staff_team_id_text.get(), staff_role_text.get(),
                         staff_first_name_text.get(), staff_last_name_text.get(), staff_salary_text.get(),
                         staff_sex_tex.get())

    staff_list1.delete(0, END)
    view_command_staff()


def delete_command_staff():
    Backend.delete_staff(selected_tuple_staff[0])
    view_command_staff()


def update_command_staff():
    Backend.update_staff(selected_tuple_staff[0], staff_team_id_text.get(), staff_role_text.get(),
                         staff_first_name_text.get(), staff_last_name_text.get(), staff_salary_text.get(),
                         staff_sex_tex.get())


staff_window = Tk()
staff_window.wm_title('Staff')

l1_s = Label(staff_window, text="Staff_id")
l1_s.grid(row=0, column=0)

l2_s = Label(staff_window, text="Team_id")
l2_s.grid(row=0, column=2)

l3_s = Label(staff_window, text="Role")
l3_s.grid(row=1, column=0)

l4_s = Label(staff_window, text="First_name")
l4_s.grid(row=1, column=2)

l5_s = Label(staff_window, text="Last_name")
l5_s.grid(row=2, column=0)

l6_s = Label(staff_window, text="Salary")
l6_s.grid(row=2, column=2)

l7_s = Label(staff_window, text="Sex")
l7_s.grid(row=3, column=0)

staff_id_text = StringVar()
e1_s = Entry(staff_window, textvariable=staff_id_text)
e1_s.grid(row=0, column=1)

staff_team_id_text = StringVar()
e2_s = Entry(staff_window, textvariable=staff_team_id_text)
e2_s.grid(row=0, column=3)

staff_role_text = StringVar()
e3_s = Entry(staff_window, textvariable=staff_role_text)
e3_s.grid(row=1, column=1)

staff_first_name_text = StringVar()
e4_s = Entry(staff_window, textvariable=staff_first_name_text)
e4_s.grid(row=1, column=3)

staff_last_name_text = StringVar()
e5_s = Entry(staff_window, textvariable=staff_last_name_text)
e5_s.grid(row=2, column=1)

staff_salary_text = StringVar()
e6_s = Entry(staff_window, textvariable=staff_salary_text)
e6_s.grid(row=2, column=3)

staff_sex_tex = StringVar()
e7_s = Entry(staff_window, textvariable=staff_sex_tex)
e7_s.grid(row=3, column=1)

staff_list1 = Listbox(staff_window, height=6, width=35)
staff_list1.grid(row=6, column=0, rowspan=6, columnspan=2)

staff_sb1 = Scrollbar(staff_window)
staff_sb1.grid(row=6, column=2, rowspan=6)

staff_list1.configure(yscrollcommand=staff_sb1.set)
staff_sb1.configure(command=staff_list1.yview)

staff_list1.bind('<<ListboxSelect>>', get_selected_row_staff)

b1_s = Button(staff_window, text="View all", width=12, command=view_command_staff)
b1_s.grid(row=6, column=3)

b2_s = Button(staff_window, text="Search", width=12, command=search_command_staff)
b2_s.grid(row=7, column=3)

b3_s = Button(staff_window, text="Add", width=12, command=add_command_staff)
b3_s.grid(row=8, column=3)

b4_s = Button(staff_window, text="Update", width=12, command=update_command_staff)
b4_s.grid(row=9, column=3)

b5_s = Button(staff_window, text="Delete", width=12, command=delete_command_staff)
b5_s.grid(row=10, column=3)

b6_s = Button(staff_window, text="Close", width=12, command=staff_window.destroy)
b6_s.grid(row=11, column=3)


### DEPENDET FRONTEND ###

def get_selected_row_dependent(event):
    global selected_tuple_dependent
    index=list1_dependent.curselection()[0]
    selected_tuple_dependent = list1_dependent.get(index)
    e1_d.delete(0, END)
    e1_d.insert(END, selected_tuple_dependent[0])
    e2.delete(0, END)
    e2.insert(END, selected_tuple_dependent[1])
    e3.delete(0, END)
    e3.insert(END, selected_tuple_dependent[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple_dependent[3])
    e5.delete(0, END)
    e5.insert(END, selected_tuple_dependent[4])
    e6.delete(0, END)
    e6.insert(END, selected_tuple_dependent[5])


def view_command_dependent():
    list1_dependent.delete(0, END)
    for row in Backend.view_dependent():
        list1_dependent.insert(END, row)


def search_command_dependent():
    list1_dependent.delete(0, END)
    for row in Backend.search_dependent(depent_id_text.get(), dependent_first_name_text.get(),
                                        dependent_last_name_text.get(), relationship_text.get(), dependent_sex_text.get()):
        list1_dependent.insert(END, row)


def add_command():
    Backend.insert_dependent(depent_id_text.get(), dependent_first_name_text.get(),
                             dependent_last_name_text.get(), relationship_text.get(), dependent_sex_text.get())

    list1_dependent.delete(0, END)
    view_command_dependent()


def delete_command_dependent():
    Backend.delete_player(selected_tuple_dependent[0])
    view_command_dependent()


def update_command_dependent():
    Backend.update_player(selected_tuple_dependent[0], depent_id_text.get(), dependent_first_name_text.get(),
                          dependent_last_name_text.get(), relationship_text.get(), dependent_sex_text.get())


window_dependet = Tk()
window_dependet.wm_title('Dependents')

l1_d = Label(window_dependet, text="Dependent_id")
l1_d.grid(row=0, column=0)

l2_d = Label(window_dependet, text="Depent_id")
l2_d.grid(row=0, column=2)

l3_d = Label(window_dependet, text="First_name")
l3_d.grid(row=1, column=0)

l4_d = Label(window_dependet, text="Last_name")
l4_d.grid(row=1, column=2)

l5_d = Label(window_dependet, text="Relationship")
l5_d.grid(row=2, column=0)

l6_d = Label(window_dependet, text="Sex")
l6_d.grid(row=2, column=2)



id_text_dependent = StringVar()
e1_d = Entry(window_dependet, textvariable=id_text_dependent)
e1_d.grid(row=0, column=1)

depent_id_text = StringVar()
e2 = Entry(window_dependet, textvariable=depent_id_text)
e2.grid(row=0 , column=3)

dependent_first_name_text = StringVar()
e3 = Entry(window_dependet, textvariable=dependent_first_name_text)
e3.grid(row= 1, column=1)

dependent_last_name_text = StringVar()
e4 = Entry(window_dependet, textvariable=dependent_last_name_text)
e4.grid(row= 1, column=3)

relationship_text = StringVar()
e5 = Entry(window_dependet, textvariable=relationship_text)
e5.grid(row=2 , column=1)

dependent_sex_text = StringVar()
e6 = Entry(window_dependet, textvariable=dependent_sex_text)
e6.grid(row=2 , column=3)

list1_dependent = Listbox(window_dependet, height=6, width=35)
list1_dependent.grid(row=6, column=0, rowspan=6, columnspan=2)

sb1_dependent = Scrollbar(window_dependet)
sb1_dependent.grid(row=6, column=2, rowspan=6)

list1_dependent.configure(yscrollcommand=sb1_dependent.set)
sb1_dependent.configure(command=list1_dependent.yview)

list1_dependent.bind('<<ListboxSelect>>', get_selected_row_dependent)

b1_d = Button(window_dependet, text="View all", width=12, command=view_command_dependent)
b1_d.grid(row=6, column=3)

b2_d = Button(window_dependet, text="Search", width=12, command=search_command_dependent)
b2_d.grid(row=7, column=3)

b3_d = Button(window_dependet, text="Add", width=12, command=add_command)
b3_d.grid(row=8, column=3)

b4_d = Button(window_dependet, text="Update", width=12, command=update_command_dependent)
b4_d.grid(row=9, column=3)

b5_d = Button(window_dependet, text="Delete", width=12, command=delete_command_dependent)
b5_d.grid(row=10, column=3)

b6_d = Button(window_dependet, text="Close", width=12, command=window_dependet.destroy)
b6_d.grid(row=11, column=3)

window_dependet.mainloop()

staff_window.mainloop()

team_windows.mainloop()

window.mainloop()