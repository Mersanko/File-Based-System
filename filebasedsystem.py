from tempfile import NamedTemporaryFile
import shutil
import csv
import getpass
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os


class CRUDL():
    def __init__(self):
        self.list_to_be_display = []
        self.list_for_del = []
        self.list_for_search = []
        self.create_ID = ""
        self.create_ID1 = []
        self.update_ID = []
        self.update_name =[]
        self.update_course = []
        self.update_year_level = []
        self.delete_parameter = []
        self.csv_space_remover = []
        self.search_row = []
        self.ID_for_delete = []
        self.ID_for_update = []





    def login(self):

            user = username.get()
            pw = password.get()
            if user=="mersan" and pw=="mersanko1":
                window.destroy()
                SDM.SDM_GUI()
            elif user=="" and pw=="":

                SDM.empty()
            else:
                SDM.invalid()

    def invalid(self):
        messagebox.showinfo("Error","Incorrect Username or Password")

    def empty(self):
        messagebox.showinfo("Error","Please Enter Account Info")

    def exitt(self):
        exit()

    def csv_blank_row_remover(self):
        x = []
        with open('crudlrevise.csv','r') as read_file:
            student_data_reader = csv.reader(read_file)
            for row in student_data_reader:
                if len(row)!=0:
                    x.append(row)
        with open('crudlrevise.csv','w') as write_file:
            student_data_writer = csv.writer(write_file)
            student_data_writer.writerows(x)




    def SDM_GUI(self):

            def csv_blank_row_remover():
                x = []
                with open('crudlrevise.csv','r') as read_file:
                    student_data_reader = csv.reader(read_file)
                    for row in student_data_reader:
                        if len(row)!=0:
                            x.append(row)
                with open('crudlrevise.csv','w') as write_file:
                    student_data_writer = csv.writer(write_file)
                    student_data_writer.writerows(x)

            def search_row():
                x = entry_for_search.get()
                with open('crudlrevise.csv','r') as csvfile:
                    student_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    for row in student_data_reader:
                        SDM.search_row.append(row)

                checkernum=0
                for e in SDM.search_row:
                    if len(e)!=0:
                        if str(e[0])==x or str(e[1])==x or str(e[2])==x or str(e[3])==x:
                            checkernum+=1
                if checkernum==0:
                    messagebox.showinfo("Error","Data doesn't exist")
                else:
                    for i in SDM.search_row:
                        if len(i)!=0:
                            if str(i[0])==x or str(i[1])==x or str(i[2])==x or str(i[3])==x :
                                SDM.list_for_search.append(i)




                for b in SDM.list_for_search:
                    treeview.insert("","end",values=b)


            def search_button():
                entry_ID = entry_for_search.get()
                SDM.list_for_search.clear()
                SDM.search_row.clear()
                for i in treeview.get_children():
                    treeview.delete(i)
                if entry_for_search=="":
                    messagebox.showinfo("Error","Insufficient data entry")
                    entry_for_search.focus()
                else:
                    search_row()
                    entry_for_search.focus()

            def clear_entry():
                SDM.list_to_be_display.clear()
                SDM.list_for_del.clear()
                SDM.list_for_search.clear()
                SDM.update_name.clear()
                SDM.update_course.clear()
                SDM.update_year_level.clear()
                SDM.delete_parameter.clear()
                entry_for_name.delete(0,'end')
                entry_for_course.delete(0,'end')
                entry_for_year_level.delete(0,'end')
                for i in treeview.get_children():
                    treeview.delete(i)
                entry_for_name.focus()


            def create_row():
                SDM.list_to_be_display.clear()
                SDM.list_for_del.clear()
                SDM.list_for_search.clear()
                SDM.update_name.clear()
                SDM.update_course.clear()
                SDM.update_year_level.clear()
                SDM.delete_parameter.clear()
                id = []
                x = []
                counter = 0
                with open ('crudlrevise.csv','r') as csv_file:
                    csv_data_reader = csv.reader(csv_file)
                    for i in csv_data_reader:
                        if len(i)!=0:
                            x.append(i)
                    for e in x:
                        counter+=1
                if counter>0 and counter<10:
                    id.append("2020-000"+str(counter))
                if counter>=10 and counter<100:
                    id.append("2020-00"+str(counter))
                if counter>=100 and counter<1000:
                    id.append("2020-0"+str(counter))
                if counter>=1000 and counter<10000:
                    id.append("2020-"+str(counter))



                stdnt_Name= entry_for_name.get()
                stdnt_Course = entry_for_course.get()
                stdnt_Year_level = entry_for_year_level.get()

                with open('crudlrevise.csv','a') as csvfile:
                    student_data_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    #student_data_writer.writerow(['ID number', 'Name', 'Course','Year level']
                    student_data_writer.writerow([id[0],str(stdnt_Name), str(stdnt_Course),str(stdnt_Year_level)])
                    with open('crudlrevise.csv','r') as csvfile:
                        student_data_reader1 = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                id.clear()
                x.clear()
                read_row()
            def read_row():
                for i in treeview.get_children():
                    treeview.delete(i)
                SDM.list_to_be_display.clear()
                SDM.list_for_search.clear()
                SDM.update_name.clear()
                SDM.update_course.clear()
                SDM.update_year_level.clear()
                SDM.delete_parameter.clear()
                SDM.list_to_be_display.clear()
                with open('crudlrevise.csv','r') as csvfile:
                    student_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    for row in student_data_reader:
                        SDM.list_to_be_display.append(row)
                count =0
                tuples = []
                for i in SDM.list_to_be_display:
                    if len(i)!=0:
                        if count==0:
                            count+=1
                        elif count!=0 and (i[0])!="" and  (i[0])!="" and  (i[0])!="":
                            index = 0
                            row_data = (i[0],i[1],i[2],i[3])
                            tuples.append(row_data)
                for row in tuples:
                    treeview.insert("", index, values=row)
                    index = index + 1



            def CurSelet1(evt):
                SDM.ID_for_delete.clear()
                SDM.ID_for_update.clear()
                entry_for_name.delete(0,END)
                entry_for_course.delete(0,END)
                entry_for_year_level.delete(0,END)

                curItem = treeview.focus()
                values=treeview.item(curItem)['values']
                SDM.ID_for_delete.append(values[0])
                SDM.ID_for_update.append(values[0])
                entry_for_name.insert(0,values[1])
                entry_for_course.insert(0,values[2])
                entry_for_year_level.insert(0,values[3])
                entry_for_name.focus()

            def update_row():
                SDM.list_to_be_display.clear()
                SDM.list_for_del.clear()
                SDM.list_for_search.clear()
                SDM.update_ID.clear()
                SDM.update_name.clear()
                SDM.update_course.clear()
                SDM.update_year_level.clear()
                SDM.delete_parameter.clear()
                stud_ID = SDM.ID_for_update[0]
                stud_name = entry_for_name.get()
                stud_course = entry_for_course.get()
                stud_year= entry_for_year_level.get()
                SDM.update_ID.append(stud_ID)
                SDM.update_name.append(stud_name)
                SDM.update_course.append(stud_course)
                SDM.update_year_level.append(stud_year)
                filename = 'crudlrevise.csv'
                tempfile = NamedTemporaryFile(mode='w', delete=False)

                fields = ['ID', 'Name', 'Course', 'Year']

                with open(filename, 'r') as csvfile, tempfile:
                    reader = csv.DictReader(csvfile, fieldnames=fields)
                    writer = csv.DictWriter(tempfile, fieldnames=fields)
                    for row in reader:
                        if row['ID'] == str(SDM.update_ID[0]):
                            row['Name'], row['Course'], row['Year'] = SDM.update_name[0],SDM.update_course[0],SDM.update_year_level[0]
                        row = {'ID': row['ID'], 'Name': row['Name'], 'Course': row['Course'], 'Year': row['Year']}
                        writer.writerow(row)

                shutil.move(tempfile.name, filename)
                clear_entry()
                read_row()
            def delete_button():
                MsgBox = tk.messagebox.askquestion ('Deleting data','Are you sure you want to delete this data',icon = 'warning')
                if MsgBox == 'yes':
                    delete_row()
                    csv_blank_row_remover()
                    entry_for_name.focus()
                else:
                    tk.messagebox.showinfo('Transaction Cancelled','You will now return to the application screen')


            def delete_row():
                x=SDM.ID_for_delete[0]
                selected_items = treeview.selection()
                for selected_item in selected_items:
                    treeview.delete(selected_item)
                    with open('crudlrevise.csv','r') as read_file:
                        student_data_reader = csv.reader(read_file)
                        for row in student_data_reader:
                            SDM.list_for_del.append(row)
                        for i in SDM.list_for_del:
                            if len(i)!=0:
                                if i[0]==x:
                                    SDM.list_for_del.remove(i)

                    with open('crudlrevise.csv','w') as write_file:
                        student_data_writer = csv.writer(write_file)
                        student_data_writer.writerows(SDM.list_for_del)

                clear_entry()
                read_row()

            def create_button():
                sn= entry_for_name.get()
                sc= entry_for_course.get()
                syl = entry_for_year_level.get()
                with open('crudlrevise.csv','r') as csvfile:
                    student_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    for row in student_data_reader:
                        SDM.search_row.append(row)

                checkernum=0
                for e in SDM.search_row:
                    if len(e)!=0:
                        if str(e[1])==sn and str(e[2])==sc and str(e[3])==syl:
                            checkernum+=1
                if checkernum>0:
                    messagebox.showinfo("Error","Data already existed")
                elif sn=="" or sc=="" or syl=="":
                    messagebox.showinfo("Error","Insufficient data entry")
                else:
                    create_row()
                    entry_for_name.delete(0,'end')
                    entry_for_course.delete(0,'end')
                    entry_for_year_level.delete(0,'end')
                    messagebox.showinfo("Successful Transaction","Data is added successfully!")
                    entry_for_name.focus()

            def clear_search_entry():
                entry_for_search.delete(0,'end')
                entry_for_search.focus()

            def update_button():
                stdnt_Name= entry_for_name.get()
                stdnt_Course = entry_for_course.get()
                stdnt_Year_level = entry_for_year_level.get()
                if stdnt_Name=="" or stdnt_Course=="" or stdnt_Year_level==""or SDM.update_ID == "" :
                    messagebox.showinfo("Error","Insufficient data entry")
                else:
                    MsgBox = tk.messagebox.askquestion ('Updating data','Are you sure you want to update this data',icon = 'warning')
                    if MsgBox == 'yes':
                        update_row()
                        entry_for_name.delete(0,'end')
                        entry_for_course.delete(0,'end')
                        entry_for_year_level.delete(0,'end')
                        messagebox.showinfo("Successful Transaction","Data is updated successfully!")
                        entry_for_name.focus()
                    else:
                        tk.messagebox.showinfo('Transaction Cancelled','You will now return to the application screen')

            window1 =Tk()
            search = StringVar()
            Name = StringVar()
            Course = StringVar()
            Year_level = StringVar()
            window1.geometry('950x600')
            window1.title("Manage data")


            label_for_name = Label(window1, text="Student Name:",font=("Arial",10))
            label_for_name.place(x=0,y=0)
            entry_for_name= Entry(window1,bd=5,width=25,textvar=Name)
            entry_for_name.place(x=120,y=0)

            label_for_course = Label(window1, text="Student Course:",font=("Arial",10))
            label_for_course.place(x=0,y=30)
            entry_for_course = Entry(window1,bd=5,textvar=Course)
            entry_for_course.place(x=120,y=30)

            label_for_year_level = Label(window1, text="Student YrLvl:",font=("Arial",10))
            label_for_year_level.place(x=0,y=60)
            entry_for_year_level= Entry(window1,bd=5,width=10,textvar=Year_level)
            entry_for_year_level.place(x=120,y=60)

            label_for_search = Label(window1, text="Search Engine",font=("Arial",10))
            label_for_search.place(x=400,y=0)
            entry_for_search = Entry(window1,bd=5,text=search)
            entry_for_search.place(x=380,y=20)
            clear_button_for_search = Button(window1,text="X",width=2,bg='red',fg='black',command=clear_search_entry)
            clear_button_for_search.place(x=510,y=20)



            button_search = Button(window1,text="Search",width=12,bg='blue',fg='black',command=search_button)
            button_search.place(x=400,y=55)
            button_view_data = Button(window1,text="View Data", width=12,bg='yellow',fg='black',command=read_row)
            button_view_data.place(x=25,y=160)
            button_add_data = Button(window1,text="Add Data", width=12,bg='green',fg='white', command=create_button)
            button_add_data.place(x=25,y=190)
            button_update_data= Button(window1,text="Update", width=12,bg='orange',fg='black', command=update_button)
            button_update_data.place(x=25,y=220)
            button_delete_data = Button(window1,text="Delete Data", width=12,bg='red',fg='white', command=delete_button)
            button_delete_data.place(x=25,y=250)
            button_clear_entry = Button(window1,text="Clear",width=12,bg='white',fg='black',command=clear_entry)
            button_clear_entry.place(x=25,y=280)





            treeview = ttk.Treeview(window1,height=20,selectmode='browse')
            ysb = ttk.Scrollbar(window1, orient='vertical', command=treeview.yview)
            ysb.place(x=930,y=120,height=425)
            treeview.configure(yscrollcommand=ysb.set)
            treeview.bind('<ButtonRelease-1>', CurSelet1)
            treeview.place(x=120,y=120)
            treeview["columns"] = ["Student ID", "Student Name","Student Course","Student Year Level"]
            treeview["show"] = "headings"
            treeview.heading("Student ID", text="Student ID")
            treeview.heading("Student Name", text="Student Name")
            treeview.heading("Student Course", text="Student Course")
            treeview.heading("Student Year Level", text="Student Year Level")

            img = ImageTk.PhotoImage(Image.open("ccslg.jpg"))
            panel = Label(window1, image = img)
            panel.place(x=600,y=5)
            ccslabel = Label(window1, text="College of Computer Studies",fg="blue",font=("Arial Bold",10))
            ccslabel.place(x=720,y=40)

            window1.mainloop()

SDM = CRUDL()
SDM.csv_blank_row_remover()


if __name__=="__main__":
        window =Tk()
        window.geometry("300x300")
        window.title("Admin Login")
        username = StringVar()
        password = StringVar()

        img = ImageTk.PhotoImage(Image.open("msu.png"))
        panel = Label(window, image = img)
        panel.place(x=95,y=0)

        canvas = tk.Canvas(window)
        canvas.place(x=64,y=220)
        canvas_text = canvas.create_text(10, 10, text='', anchor=tk.NW)
        test_string = "Welcome to MSU_IIT SDM!"
        delta = 20
        delay = 0
        for i in range(len(test_string) + 1):
            s = test_string[:i]
            update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
            canvas.after(delay, update_text)
            delay += delta
        label1 = Label(window, text="Username:",width = 20,font=("bold",10))
        label1.place(x=30,y=110)
        entry_1 = Entry(window,bd=5,textvar=username)
        entry_1.place(x=80 , y=135)
        label2 = Label(window, text="Password:",width = 20,font=("bold",10))
        label2.place(x=30,y= 160)
        entry_2= Entry(window,bd=5,textvar=password,show="*")
        entry_2.place(x=80 ,y=185)

        button_login = Button(window,text="Login", width=12,bg='green',fg='white', command=SDM.login).place(x=55,y=250)
        button_quit = Button(window,text="Quit", width=12,bg='brown',fg='white', command=SDM.exitt).place(x=155,y=250)

        window.mainloop()
