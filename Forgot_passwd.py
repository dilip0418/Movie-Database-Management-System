import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Forgot_Pass:
    def __init__(self,root):
        '''initializes all the necessary widgets onto the Tk'''
        self.root = root
        self.root.geometry("503x493+400+100")
        self.root.configure(bg = "#FFFFFF")
        self.root.resizable(False, False)
        self.root.wm_iconbitmap("Main_Images/movies.ico")

        self.var_uname = StringVar()
        self.var_passwd = StringVar()
        self.var_answer = StringVar()
        self.var_passwd1 = StringVar()

        canvas = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 493,
            width = 503,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = "Main_Images/forgot_background.png")
        self.background = canvas.create_image(
            251.5, 246.5,
            image=self.background_img)

        self.entry0_img = PhotoImage(file = "Main_Images/forgot_img_textBox0.png")
        self.entry0_bg = canvas.create_image(
            337.0, 316.5,
            image = self.entry0_img)

        username = Entry(
            self.root,
            bd = 0,
            textvariable=self.var_uname,
            bg = "#ffffff",
            highlightthickness = 0)

        username.place(
            x = 225.0, y = 107,
            width = 224.0,
            height = 23)

        self.question_entry_img = PhotoImage(file = "Main_Images/forgot_img_textBox0.png")
        self.entry1_bg = canvas.create_image(
            336.0, 265.5,
            image = self.question_entry_img)

        self.Quest_var = StringVar()
        combo_Quest = ttk.Combobox(self.root,textvariable = self.Quest_var,font='arial 12 bold',width=18,state='readonly')
        combo_Quest['values'] = ("Who's your best friend","What's your pet name","What's your favourite teacher name","What's your nickname")
        combo_Quest.current(0)
        combo_Quest.place(x = 224.0, y = 157,width = 224.0,height = 23)

        self.answer_entry_img = PhotoImage(file = "Main_Images/forgot_img_textBox0.png")
        self.entry2_bg = canvas.create_image(
            336.0, 217.5,
            image = self.answer_entry_img)

        answer = Entry(
            self.root,
            bd = 0,
            textvariable = self.var_answer,
            bg = "#ffffff",
            highlightthickness = 0)

        answer.place(
            x = 224.0, y = 205,
            width = 224.0,
            height = 23)

        self.entry3_img = PhotoImage(file = "Main_Images/forgot_img_textBox0.png")
        self.entry3_bg = canvas.create_image(
            336.0, 169.5,
            image = self.entry3_img)

        new_passwd = Entry(
            self.root,
            bd = 0,
            textvariable = self.var_passwd,
            bg = "#ffffff",
            highlightthickness = 0)

        new_passwd.place(
            x = 224.0, y = 253,
            width = 224.0,
            height = 23)

        self.entry4_img = PhotoImage(file = "Main_Images/forgot_img_textBox0.png")
        self.entry4_bg = canvas.create_image(
            336.0, 119.5,
            image = self.entry4_img)

        confirm_passwd = Entry(
            self.root,
            bd = 0,
            textvariable=self.var_passwd1,
            bg = "#ffffff",
            highlightthickness = 0)

        confirm_passwd.place(
            x = 224.0, y = 304,
            width = 224.0,
            height = 23)

        self.confirm_img = PhotoImage(file = "Main_Images/confirm.png")
        confirm_btn = Button(
            self.root,
            image = self.confirm_img,
            borderwidth = 0,
            bg='light blue',
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        confirm_btn.place(
            x = 195, y = 405,
            width = 114,
            height = 26)

    def btn_clicked(self):
        '''used for confirm'''
        if self.var_uname.get()=='':
            messagebox.showerror('Error','Username field is empty.....!',parent = self.root)
        elif self.var_answer.get()=='':
            messagebox.showerror('Error','answer field is empty.....!',parent = self.root)
        elif self.var_passwd.get() != self.var_passwd1.get():
            messagebox.showerror('Error','New password and confirm password must be same.....!',parent = self.root)
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('UPDATE USER SET password = %s WHERE username =%s',(
                                                                                self.var_passwd1.get(),
                                                                                self.var_uname.get()
                                                                                ))
                self.var_passwd1.set('')
                self.var_answer.set('')
                self.var_uname.set('')
                self.var_passwd.set('')
                connection.commit()
                connection.close()
                messagebox.showinfo('UPDATE','Password changed Successfully....!',parent=self.root)
            except Exception as e:
                messagebox.showwarning('Warning',f'Something went wrong !{e}',parent=self.root)


if __name__=='__main__':
    root=Tk()
    obj = Forgot_Pass(root)
    root.mainloop()
