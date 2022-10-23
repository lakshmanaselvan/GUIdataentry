from tkinter import *
from tkinter import ttk
from db import Database
from tkinter import messagebox

db = Database("students.db")

def getData(event):
    selected_row = tv.focus()
    Data = tv.item(selected_row)
    global row
    row = Data["values"]
    name.set(row[1])
    age.set(row[2])
    dob.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END, row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        
        tv.insert("",END,values=row)

def add():
    if txtname.get()=="" or txtage.get()=="" or txtdob.get()=="" or txtemail.get()=="" or combogender.get()=="" or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error in input","Please Fill All The Details")
        return
    db.insert(txtname.get(), txtage.get(), txtdob.get(), txtemail.get(), combogender.get(), txtcontact.get(), txtaddress.get(1.0,END))
    messagebox.showinfo("Success","Record Inserted")
    clear()
    displayAll()
    
def update():
    if txtname.get()=="" or txtage.get()=="" or txtdob.get()=="" or txtemail.get()=="" or combogender.get()=="" or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error in input","Please Fill All The Details")
        return
    db.update(row[0],txtname.get(), txtage.get(), txtdob.get(), txtemail.get(), combogender.get(), txtcontact.get(), txtaddress.get(1.0,END))
    messagebox.showinfo("Success","Record Updated")
    clear()
    displayAll()

def delete():
    db.remove(row[0])
    clear()
    displayAll()

def clear():
    name.set("")
    age.set("")
    dob.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtaddress.delete(1.0,END)





root=Tk()
root.title("Students Management System")
root.geometry("1366x768+0+0")
root.configure(bg="#2c3e50")
root.state("zoomed")

name=StringVar()
age=StringVar()
dob=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()




#eframe
entries_frame=Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame, text="Students Management System",font=("Calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)

lblname=Label(entries_frame,text="Name",font=("Calibri",16),bg="#535c68",fg="white")
lblname.grid(row=1,column=0,padx=10,pady=10, sticky="w")
txtname=Entry(entries_frame,textvariable=name,font=("Calibri",16),width=30)
txtname.grid(row=1,column=1,padx=10,pady=10, sticky="w")

lblage=Label(entries_frame,text="Age",font=("Calibri",16),bg="#535c68",fg="white")
lblage.grid(row=1,column=2,padx=10,pady=10, sticky="w")
txtage=Entry(entries_frame,textvariable=age,font=("Calibri",16),width=30)
txtage.grid(row=1,column=3,padx=10,pady=10, sticky="w")

lbldob=Label(entries_frame,text="D.O.B",font=("Calibri",16),bg="#535c68",fg="white")
lbldob.grid(row=2,column=0,padx=10,pady=10, sticky="w")
txtdob=Entry(entries_frame,textvariable=dob,font=("Calibri",16),width=30)
txtdob.grid(row=2,column=1,padx=10,pady=10, sticky="w")

lblemail=Label(entries_frame,text="Email",font=("Calibri",16),bg="#535c68",fg="white")
lblemail.grid(row=2,column=2,padx=10,pady=10, sticky="w")
txtemail=Entry(entries_frame,textvariable=email,font=("Calibri",16),width=30)
txtemail.grid(row=2,column=3,padx=10,pady=10, sticky="w")

lblgender=Label(entries_frame,text="Gender",font=("Calibri",16),bg="#535c68",fg="white")
lblgender.grid(row=3,column=0,padx=10,pady=10, sticky="w")
combogender=ttk.Combobox(entries_frame,font=("Calibri",16),width=28,textvariable=gender,state="r")
combogender["values"]=('Male','Female')
combogender.grid(row=3,column=1,padx=10,sticky="w")

lblcontact=Label(entries_frame,text="Contact",font=("Calibri",16),bg="#535c68",fg="white")
lblcontact.grid(row=3,column=2,padx=10,pady=10, sticky="w")
txtcontact=Entry(entries_frame,textvariable=contact,font=("Calibri",16),width=30)
txtcontact.grid(row=3,column=3,padx=10,pady=10, sticky="w")

lbladdress=Label(entries_frame,text="Address",font=("Calibri",16),bg="#535c68",fg="white")
lbladdress.grid(row=4,column=0,padx=10,pady=10, sticky="w")
txtaddress=Text(entries_frame,width=85,height=3,font=("Calibri",16))
txtaddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

#button
btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")
btn_add=Button(btn_frame,command=add, bd=0,bg="#2980b9",text="ADD_DETAILS",width=15,font=("Calibri",16,"bold"),fg="white")
btn_add.grid(row=0,column=0,padx=10)
btn_update=Button(btn_frame,command=update, bd=0,bg="orange",text="UPDATE_DETAILS",width=15,font=("Calibri",16,"bold"),fg="white")
btn_update.grid(row=0,column=1,padx=10)
btn_delete=Button(btn_frame,command=delete, bd=0,bg="red",text="DELETE_DETAILS",width=15,font=("Calibri",16,"bold"),fg="white")
btn_delete.grid(row=0,column=3,padx=10)
btn_clear=Button(btn_frame,command=clear, bd=0,bg="dark red",text="CLEAR_DETAILS",width=15,font=("Calibri",16,"bold"),fg="white")
btn_clear.grid(row=0,column=4,padx=10)

#table frame
tree_frame = Frame(root, bg="#ffffff")
tree_frame.place(x=0,y=425, width=1980, height=500)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 14))
tv=ttk.Treeview(tree_frame,column=(1,2,3,4,5,6,7,8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=1)
tv.heading("2", text="Name")
tv.column("2", width=5)
tv.heading("3", text="Age")
tv.column("3", width=2)
tv.heading("4", text="D.O.B")
tv.column("4", width=5)
tv.heading("5", text="Email")
tv.column("5", width=5)
tv.heading("6", text="Gender")
tv.column("6", width=5)
tv.heading("7", text="Contact")
tv.column("7", width=5)
tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)



displayAll()
root.mainloop()