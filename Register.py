from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        '''initializes all the necessary widgets onto the Tk'''
        self.root = root
        self.root.geometry("503x431+400+200")
        self.root.configure(bg = "#FFFFFF")
        self.root.resizable(False, False)
        self.root.wm_iconbitmap("Main_Images/movies.ico")
        
        self.uname = StringVar()
        self.password_var = StringVar()
        self.answer_var = StringVar()

        canvas = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 431,
            width = 503,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
            )
        canvas.place(x = 0, y = 0)

        self.bg_img = PhotoImage(file = "Main_Images/register_background.png")
        self.background = canvas.create_image(
            251.5, 215.5,
            image=self.bg_img
            )

        self.entry0_img = PhotoImage(file = "Main_Images/register_img_textBox0.png")
        self.entry0_bg = canvas.create_image(
            336.0, 265.5,
            image = self.entry0_img
            )

        entry0 = Entry(
            self.root,
            textvariable = self.uname,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0
            )

        entry0.place(
            x = 224.0, y = 107,
            width = 224.0,
            height = 23
            )

        self.entry1_img = PhotoImage(file = "Main_Images/register_img_textBox0.png")
        self.entry1_bg = canvas.create_image(
            336.0, 217.5,
            image = self.entry1_img
            )

        entry1 = Entry(
            self.root,
            textvariable = self.password_var,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0
            )

        entry1.place(
            x = 224.0, y = 157,
            width = 224.0,
            height = 23
            )

        self.entry2_img = PhotoImage(file = "Main_Images/register_img_textBox0.png")
        self.entry2_bg = canvas.create_image(
            336.0, 169.5,
            image = self.entry2_img
            )
        self.Quest_var = StringVar()
        combo_Quest = ttk.Combobox(self.root,textvariable = self.Quest_var,font='arial 12 bold',width=18,state='readonly')
        combo_Quest['values'] = ("Who's your best friend","What's your pet name","What's your favourite teacher name","What's your nickname")
        combo_Quest.current(0)
        combo_Quest.place(x = 224.0, y = 205,width = 224.0,height = 23)

        self.entry3_img = PhotoImage(file = "Main_Images/register_img_textBox0.png")
        self.entry3_bg = canvas.create_image(
            336.0, 119.5,
            image = self.entry3_img
            )

        entry3 = Entry(
            self.root,
            textvariable=self.answer_var,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0
            )

        entry3.place(
            x = 224.0, y = 253,
            width = 224.0,
            height = 23
            )

        self.img0 = PhotoImage(file = "Main_Images/register.png")
        b0 = Button(
            self.root,
            image = self.img0,
            borderwidth = 0,
            bg='light pink',
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat"
            )

        b0.place(
            x = 195, y = 328,
            width = 114,
            height = 26
            )

    def btn_clicked(self):
        if self.uname.get()==' ' or self.password_var.get()=='' or self.answer_var.get()=='':
            messagebox.showerror('Failed','All entries need to be filled...!',parent = self.root)
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('INSERT INTO USER VALUES(%s,%s,%s,%s)',(self.uname.get(),
                                                                        self.password_var.get(),
                                                                        self.Quest_var.get(),
                                                                        self.answer_var.get()
                                                                            ))
                self.uname.set('')
                self.password_var.set('')
                self.Quest_var.set('')
                self.answer_var.set('')
                connection.commit()
                connection.close()
                messagebox.showinfo('Success',"Registered Successfully...!",parent = self.root)
            except Exception as e:
                messagebox.showerror('Failed',e)

                
if __name__=='__main__':
    root=Tk()
    obj = Register(root)
    root.mainloop()

