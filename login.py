import mysql.connector
from tkinter import *
from tkinter import messagebox
from movie import Movie
from Register import Register
from Forgot_passwd import Forgot_Pass

class log_win:
    '''Used for creating a Login Page'''
    def __init__(self,root):
        '''initializes all the necessary widgets onto the Tk'''
        self.root = root
        self.root.title('Login Window')
        self.root.geometry('1105x709+170+0')
        self.root.configure(bg = "#eed9c0")
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("Main_Images/movies.ico")

        self.username = StringVar()
        self.password = StringVar()
        canvas = Canvas(
                self.root,
                bg = "#eed9c0",
                height = 739,
                width = 1155,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
        )
        canvas.place(x=0,y=0)

        self.bg_img = PhotoImage(file = "Main_Images/login_background.png")
        self.bg = canvas.create_image(
            526.5,368.0,
            image = self.bg_img
        )

        self.usr_img = PhotoImage(file = "Main_Images/login_img_textBox0.png")
        self.usr_name_bg = canvas.create_image(
            900.5,394.5,
            image = self.usr_img
        )

        self.usr_entry = Entry(
            bd = 0,
            bg = '#ffffff',
            textvariable=self.username,
            highlightthickness=0
        )
        self.usr_entry.place(
            x =750.0,y = 283,
            width = 303.0,
            height = 53
        )

        self.passwd_img = PhotoImage(file ="Main_Images/login_img_textBox0.png")
        self.passwd_bg = canvas.create_image(
            901.5,310.5,
            image = self.passwd_img
        )

        self.passwd_entry = Entry(
            bd = 0,
            show = '*',
            textvariable = self.password,
            bg = '#ffffff',
            highlightthickness = 0
        )

        self.passwd_entry.place(
            x = 749.0, y = 367,
            width = 303.0,
            height = 53
        )


        self.img0 = PhotoImage(file = "Main_Images/Submit.png")
        
        Submit = Button(
            image = self.img0,
            borderwidth=0,
            highlightthickness=0,
            bg = '#eed9c0',
            command=self.submit,
            relief= 'flat'
        )
        Submit.place(
            x = 801, y = 482,
            width = 157,
            height = 40
        )

        new_usr = Button(
            text = 'New User',
            bg = "#eed9c0",
            font = 'Castellar 10 bold',
            fg = 'red',
            borderwidth=0,
            highlightthickness=0,
            command=self.new_usr,
            relief= 'flat'
        )
        new_usr.place(
            x = 670, y = 562,
            width = 107,
            height = 40
        )
        
        forgot_passwd = Button(
        text = 'Forgot Password',
        bg = "#eed9c0",
        font = 'Castellar 10 bold',
        fg = 'red',
        borderwidth=0,
        highlightthickness=0,
        command=self.forgot_passwd,
        relief= 'flat'
        )

        forgot_passwd.place(
            x = 680, y = 605,
            width = 157,
            height = 40
        )

    def submit(self):
        '''Redirects the user to the main window of the apllication'''
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror('Error','All entries need to be filled...!',parent = self.root)
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('SELECT username, password FROM USER WHERE USERNAME=%s AND PASSWORD=%s',(self.username.get(),self.password.get()))
                rows = my_cursor.fetchone()
                if rows != None:
                    self.username.set('')
                    self.password.set('')
                    messagebox.showinfo('Success','Successfully logged in...!',parent = self.root)
                    self.new_win0 = Toplevel(self.root)
                    self.app0 = Movie(self.new_win0)
                else:
                    messagebox.showerror('Failed',f'Invalid username or password\nPlease Try again by entering correct one.....!',parent = self.root)
                connection.commit()
                connection.close()
            except Exception as e:
                messagebox.showerror('Failed',e)

    def new_usr(self):
        '''Redirects the control to the New register Page'''
        self.new_win2 = Toplevel(self.root)
        self.app1 = Register(self.new_win2)
    
    def forgot_passwd(self):
        '''Redirects the control to the Forgot Password Page'''
        self.new_win2 = Toplevel(self.root)
        self.app2 = Forgot_Pass(self.new_win2)

if __name__=='__main__':
    root=Tk()
    obj = log_win(root)
    root.mainloop()