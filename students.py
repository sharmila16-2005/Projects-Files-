from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x900+0+0")

        title = Label(self.root, text="Student Management System", bd=9, relief=GROOVE,
                      font=("times new roman", 50, "bold"), bg="lightgrey")
        title.pack(side=TOP, fill=X)

        # ===== Variables =====
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.trade_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ===== Manage Frame =====
        Manage_frame = Frame(self.root, bd=6, relief=RIDGE)
        Manage_frame.place(x=20, y=120, width=500, height=700)

        m_title = Label(Manage_frame, text="Manage Student", bg="lightgrey", fg='black', font=('times new roman', 45, 'bold'))
        m_title.grid(row=0, columnspan=2, pady=20)

        # ===== Student Input Fields =====
        # Roll No
        lbl_roll = Label(Manage_frame, text='Roll No:', bg='lightgrey', fg='black', font=('times new roman', 20, 'bold'))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky='w')
        txt_roll = Entry(Manage_frame, textvariable=self.Roll_No_var, font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        # Name
        lbl_name = Label(Manage_frame, text='Name:', bg='lightgrey', fg='black', font=('times new roman', 20, 'bold'))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')
        txt_name = Entry(Manage_frame, textvariable=self.name_var, font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        # Email
        lbl_email = Label(Manage_frame, text='Email:', bg='lightgrey', fg='black', font=('times new roman', 20, 'bold'))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky='w')
        txt_email = Entry(Manage_frame, textvariable=self.email_var, font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        # Gender
        lbl_gender = Label(Manage_frame, text='Gender:', bg='lightgrey', fg='black', font=('times new roman', 20, 'bold'))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky='w')
        combo_gender = ttk.Combobox(Manage_frame, textvariable=self.gender_var, font=("times new roman", 13, 'bold'), state='readonly')
        combo_gender['values'] = ('Male', 'Female', 'Other' )
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        # Trade
        lbl_trade = Label(Manage_frame, text='Trade:', bg='lightgrey', fg='black', font=('times new roman', 20, 'bold'))
        lbl_trade.grid(row=5, column=0, pady=10, padx=20, sticky='w')
        combo_trade = ttk.Combobox(Manage_frame, textvariable=self.trade_var, font=("times new roman", 13, 'bold'), state='readonly')
        combo_trade['values'] = ('Artificial Intelligence Programming Assistant', 'Computer Operator and Programming Assistant (COPA)', 
                                 'Stenographer & Secretarial Assistant (Hindi)','Dress Making', 'Basic Cosmetology', 'Secretarial Practice (English)', 'Technician Electronics System Design & Repair')
        combo_trade.grid(row=5, column=1, padx=20, pady=10)

        # Contact
        lbl_contact = Label(Manage_frame, text='Contact:', bg='lightgrey', fg='black', font=('times new roman', 20, 'bold'))
        lbl_contact.grid(row=6, column=0, pady=10, padx=20, sticky='w')
        txt_contact = Entry(Manage_frame, textvariable=self.contact_var, font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE)
        txt_contact.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        # DOB
        lbl_dob = Label(Manage_frame, text='D.O.B:', bg='lightgrey', fg='black', font=('times new roman', 20, 'bold'))
        lbl_dob.grid(row=7, column=0, pady=10, padx=20, sticky='w')
        txt_dob = Entry(Manage_frame, textvariable=self.dob_var, font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE)
        txt_dob.grid(row=7, column=1, pady=10, padx=20, sticky='w')

        # Address
        lbl_address = Label(Manage_frame, text='Address:', bg='lightgrey', fg='black', font=('times new roman', 20, 'bold'))
        lbl_address.grid(row=8, column=0, pady=10, padx=20, sticky='w')
        self.txt_address = Text(Manage_frame, width=30, height=3, font=("", 10))
        self.txt_address.grid(row=8, column=1, pady=10, padx=20, sticky='w')

        # ===== Buttons =====
        btn_frame = Frame(Manage_frame, bd=3, relief=RIDGE, bg='lightgrey')
        btn_frame.place(x=20, y=600, width=420)

        Button(btn_frame, text='Add', width=10, command=self.add_students).grid(row=0, column=0, pady=10, padx=10)
        Button(btn_frame, text='Update', width=10, command=self.update_data).grid(row=0, column=1, pady=10, padx=10)
        Button(btn_frame, text='Delete', width=10, command=self.delete_data).grid(row=0, column=2, pady=10, padx=10)
        Button(btn_frame, text='Clear', width=10, command=self.clear).grid(row=0, column=3, pady=10, padx=10)

        # ===== Detail Frame =====
        Detail_frame = Frame(self.root, bd=6, relief=RIDGE, bg='lightgrey')
        Detail_frame.place(x=550, y=120, width=925, height=700)

        Label(Detail_frame, text="Search By", bg="lightgrey", fg='black', font=('times new roman', 20, 'bold')).grid(row=0, column=0, pady=10, padx=20, sticky='w')
        combo_search = ttk.Combobox(Detail_frame, textvariable=self.search_by, font=("times new roman", 13, 'bold'), width=10, state='readonly')
        combo_search['values'] = ('roll_no', 'name', 'contact')
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_frame, textvariable=self.search_txt, font=('times new roman', 10, 'bold'), width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        Button(Detail_frame, text='Search', width=10, command=self.search_data).grid(row=0, column=3, pady=10, padx=10)
        Button(Detail_frame, text='Show All', width=10, command=self.fetch_data).grid(row=0, column=4, pady=10, padx=10)

        # ===== Table Frame =====
        Table_frame = Frame(Detail_frame, bd=4, relief=RIDGE, bg='lightgrey')
        Table_frame.place(x=10, y=70, width=870, height=580)

        scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(Table_frame, columns=("roll_no", "name", "email", "gender", "trade", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        for col in self.student_table["columns"]:
            self.student_table.heading(col, text=col.replace("_", " ").title())
            self.student_table.column(col, width=100)

        self.student_table["show"] = 'headings'
        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    # ====== CRUD Methods ======
    def add_students(self):
        con = None
        try:
            con = pymysql.connect(host="localhost", user="root", password="admin", database="sms2")
            cur = con.cursor()
            cur.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (
                self.Roll_No_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.trade_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_address.get('1.0', END).strip()
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success", "Record has been inserted")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
        finally:
            if con:
                con.close()

    def fetch_data(self):
        con = None
        try:
            con = pymysql.connect(host="localhost", user="root", password="admin", database="sms2")
            cur = con.cursor()
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
        finally:
            if con:
                con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.trade_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete('1.0', END)

    def update_data(self):
        con = None
        try:
            con = pymysql.connect(host="localhost", user="root", password="admin", database="sms2")
            cur = con.cursor()
            cur.execute("""UPDATE student SET name=%s, email=%s, gender=%s, trade=%s, contact=%s, dob=%s, address=%s WHERE roll_no=%s""", (
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.trade_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_address.get('1.0', END).strip(),
                self.Roll_No_var.get()
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success", "Record has been updated")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
        finally:
            if con:
                con.close()

    def delete_data(self):
        con = None
        try:
            con = pymysql.connect(host="localhost", user="root", password="admin", database="sms2")
            cur = con.cursor()
            cur.execute("DELETE FROM student WHERE roll_no=%s", (self.Roll_No_var.get(),))
            con.commit()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success", "Record has been deleted")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
        finally:
            if con:
                con.close()

    def search_data(self):
        con = None
        try:
            con = pymysql.connect(host="localhost", user="root", password="admin", database="sms2")
            cur = con.cursor()
            query = f"SELECT * FROM student WHERE {self.search_by.get()} LIKE %s"
            cur.execute(query, ('%' + self.search_txt.get() + '%',))
            rows = cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
        finally:
            if con:
                con.close()

# ===== Run =====
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
