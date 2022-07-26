import random
import wikipedia
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector

class Dir_win:
    def __init__(self,root):
        '''initializes all the necessary widgets onto the Tk'''
        self.root = root
        self,root.title('Directors Information')
        self.root.geometry('1150x540+205+180')
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("Main_Images/movies.ico")

        self.var_dir_id = StringVar()
        x = random.randint(100,999)
        self.var_dir_id.set(x)

        self.var_dir_name = StringVar()
        self.var_dir_phone = StringVar()

        #-------------------------Title-------------------------
        lbl_title= Label(self.root,text='Director Details',font='Castellar 25 bold',fg='burlywood2',bg='black',relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1140,height=35)

        # -------------------------Label Frame-------------------
        lbl_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='Director Details',padx=2,font='times 14 bold italic')
        lbl_frame.place(x=5,y=38,width=420,height=500)

        # ----------labels and Entry fields---------------

        dir_id = Label(lbl_frame,text='Director ID',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        dir_id.grid(row=0,column=0,sticky=W)

        ent_id = ttk.Entry(lbl_frame,textvariable=self.var_dir_id,width=22,font="times 12",state='readonly')
        ent_id.grid(row=0,column=4)

        dir_name = Label(lbl_frame,text='Name',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        dir_name.grid(row=1,column=0,sticky=W)

        ent_dir_name = ttk.Entry(lbl_frame,textvariable=self.var_dir_name,width=22,font="times 12")
        ent_dir_name.grid(row=1,column=4)

        dir_phone = Label(lbl_frame,text='Phone No',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        dir_phone.grid(row=2,column=0,sticky=W)

        ent_dir_phone = ttk.Entry(lbl_frame,textvariable=self.var_dir_phone,width=22,font="times 12")
        ent_dir_phone.grid(row=2,column=4)

                #----------------Images for Buttons---------------
        img_add=Image.open("Main_Images/add.jpg")
        img_add= img_add.resize((94,50),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img_add)

        img_update=Image.open("Main_Images/update.jpg")
        img_update= img_update.resize((94,50),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(img_update)

        img_delete=Image.open("Main_Images/delete.jpg")
        img_delete= img_delete.resize((94,50),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(img_delete)

        img_reset=Image.open("Main_Images/reset.jpg")
        img_reset= img_reset.resize((94,50),Image.ANTIALIAS)
        self.img4=ImageTk.PhotoImage(img_reset)

        img_search=Image.open("Main_Images/search.png")
        img_search= img_search.resize((68,30),Image.ANTIALIAS)
        self.img_search=ImageTk.PhotoImage(img_search)

        #------------------------ Buttons Frame and Buttons
        btn_frame = Frame(lbl_frame,bd = 2, relief=RIDGE)
        btn_frame.place(x=0,y=350,width=413,height=50)

        Add_btn=Button(btn_frame,image=self.img1,command=self.add_data,bg='white',bd=3,relief=RIDGE)
        Add_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,image=self.img2,command=self.update,bg='white',bd=3,relief=RIDGE)
        Update_btn.grid(row=0,column=1)

        Reset_btn=Button(btn_frame,image=self.img4,command=self.reset,bg='white',bd=3,relief=RIDGE)
        Reset_btn.grid(row=0,column=2)

        Delete_btn=Button(btn_frame,image=self.img3,command=self.remove_director,bg='white',bd=3,relief=RIDGE)
        Delete_btn.grid(row=0,column=3)

        btnAbout = Button(lbl_frame,text='About Director',command=self.about_director,width=7,font='arial 16 bold',bg = 'blue',fg = 'white')
        btnAbout.place(x=100,y=120,width=150,height=30)

        self.ent_aboutDirector = Text(lbl_frame,width=22,font="times 12")
        self.ent_aboutDirector.place(x=10,y=160,width=380,height=175)

        # ---------------------Table Frame--------------------------
        table_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='View Details',padx=2,font='times 14 bold italic')
        table_frame.place(x=430,y=38,width=720,height=500,)

        # --------------------------------Search By Label-------------------------
        lbl_search =Label(table_frame,bd = 2,relief=RIDGE,text='Search By',font='times 12 bold',bg='red',fg='white')
        lbl_search.grid(row=0,column=0,sticky=W)


        # ------------------------------Search Combobox and Entry for Specific Search-----------------------
        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame,textvariable = self.search_var,font='arial 12 bold',width=18,state='readonly')
        combo_search['values'] = ('director_id','director_name')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=15)

        self.txt_search = StringVar()
        ent_search = ttk.Entry(table_frame,textvariable = self.txt_search,width=22,font="times 12")
        ent_search.grid(row=0,column=2,padx=10)

        
        # -----------------------------Search annd Show All Buttons-------------------------
        btnSearch = Button(table_frame,image=self.img_search,command=self.search,width=85,height=40,bd=0)
        btnSearch.grid(row=0,column=3)

        btnShowAll = Button(table_frame,text='Show All',width=7,command=self.fetch_data,height=1,font='arial 16 bold',bg = 'blue',fg = 'white')
        btnShowAll.grid(row=0,column=6)
        

        # --------------------------Show Data Table----------------------------
        table_data =LabelFrame(table_frame,bd = 2,relief=RIDGE)
        table_data.place(x=0,y=45,width=680,height=400)

        # ------------------------Scroll Bar-------------------------
        Scrollbar_x = ttk.Scrollbar(table_data,orient=HORIZONTAL)
        Scrollbar_y = ttk.Scrollbar(table_data,orient=VERTICAL)
        
        # -------------------------Treeview--------------------------
        self.director_details_table = ttk.Treeview(table_data,columns=('id','Name','phone'),xscrollcommand=Scrollbar_x.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_x.config(command=self.director_details_table.xview)
        Scrollbar_y.config(command=self.director_details_table.yview)

        # ---------------------Table Heading-----------------------------
        self.director_details_table.heading('id',text='Director Id')
        self.director_details_table.heading('Name',text='Name')
        self.director_details_table.heading('phone',text='Phone')
        self.director_details_table['show']  ='headings'

        # ----------------------Adjusting the Column Width-------------------
        self.director_details_table.column('id',width=70)
        self.director_details_table.column('Name',width=200)
        self.director_details_table.column('phone',width=70)


        self.director_details_table.pack(fill=BOTH,expand=1)
        self.director_details_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    def add_data(self):
        ''' Adds new Directors to the Movie Database '''
        if self.var_dir_name.get()=='':
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_dir_name.get().isdigit():
             messagebox.showerror("Error","The name field must be a valid name",parent=self.root)
        elif not self.var_dir_phone.get().isdigit() or len(self.var_dir_phone.get())<10 and len(self.var_dir_phone.get())>10:
             messagebox.showerror("Error","Enter a valid phone number(The phno must atleast have 10 digits and it must not exceed 10 digits)",parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('INSERT INTO DIRECTOR VALUES(%s,%s,%s)',(self.var_dir_id.get(),
                                                                                self.var_dir_name.get(),
                                                                                self.var_dir_phone.get(),
                                                                            ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('Success','Director added sucessfully',parent=self.root)
            except Exception as e:
                messagebox.showwarning('Warning',f'Something went wrong !{e}',parent=self.root)
            add_data = messagebox.askyesno('Movie Database System','Do you Want to add more Directors',parent = self.root)
            if add_data > 0:
                self.reset()
            else: pass
            self.reset()

    def remove_director(self):
        ''' Removes a selected Row/Tuple fromm the table as well as in the database '''
        if self.var_dir_name.get() == '':
            messagebox.showerror('Error','Please enter the Director Name field...!',parent=self.root)
        else:
            remove_director = messagebox.askyesno("Director Database System","Do You Want to Delete This Director's Data ?",parent = self.root)
            if remove_director > 0:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                Del_query = "DELETE FROM DIRECTOR WHERE director_id=%s"
                value = (self.var_dir_id.get(),)                        
                my_cursor.execute(Del_query,value)
                messagebox.showinfo("Success","Director's Data Removed Successfully....!",parent=self.root)
            else:
                if not remove_director:
                    return
            connection.commit()
            self.fetch_data()
            connection.close()
            self.reset()

    def reset(self):
        ''' Used for resetting the values a selected record '''
        x = random.randint(100,999)
        self.var_dir_id.set(x)
        self.var_dir_name.set(''),
        self.var_dir_phone.set('')

    def fetch_data(self):
        ''' Fetches the data present in the Director Table '''
        try:
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            my_cursor.execute('SELECT * FROM DIRECTOR')
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.director_details_table.delete(*self.director_details_table.get_children())
                for i in rows:
                    self.director_details_table.insert('',END,values=i)
            connection.commit()
            connection.close()
        except Exception as e:
            messagebox('Error',e)
            
    def search(self):
        '''Searches a particular Item in the table'''
        try:
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            search_value = self.txt_search.get()
            if search_value == '':
                messagebox.showwarning('Warn','Please enter text in the Search box !',parent = self.root)
            my_cursor.execute("select * from Director where "+str(self.search_var.get())+" like '%"+search_value+"%'")
            rows = my_cursor.fetchall()
            if len(rows) == 0:
                messagebox.showerror('Error','The search object does not exits 😢',parent = self.root)
            else:
                self.director_details_table.delete(*self.director_details_table.get_children())
                for i in rows:
                    self.director_details_table.insert('',END,values=i)
                    connection.commit()
            connection.close()
        except Exception as e:
            messagebox.showerror('Error',e,parent = self.root)

    
    def update(self):
        ''' Used for updating the fields/attribute values in a table'''
        if self.var_dir_name.get() == '' or self .var_dir_phone.get() == '':
            messagebox.showerror('Error','Please enter the values in all fields...!',parent=self.root)
        elif self.var_dir_name.get().isdigit():
            messagebox.showerror('Error','Director Name cannot be a number',parent = self.root)
        else:
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            my_cursor.execute('UPDATE DIRECTOR SET director_name = %s, director_phone = %s WHERE director_id =%s',(
                                                                                                    self.var_dir_name.get(),
                                                                                                    self.var_dir_phone.get(),
                                                                                                    self.var_dir_id.get()
                                                                                                ))
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo('UPDATE','Director Data Updated Successfully....!',parent=self.root)
            self.reset()

    def get_cursor(self,event=''):
        ''' Helps in show the data in the table Present in GUI window''' 
        cursor_row = self.director_details_table.focus()
        content = self.director_details_table.item(cursor_row)
        row = content['values']
        self.var_dir_id.set(row[0])
        self.var_dir_name.set(row[1]),
        self.var_dir_phone.set(row[2])

    def about_director(self):
        '''Gives a brief information about the director'''
        try:
            self.ent_aboutDirector.delete(1.0,END)
            director=self.var_dir_name.get()
            self.ent_aboutDirector.insert(INSERT, wikipedia.summary(str(director)))
        except Exception as e:
            messagebox.showerror('Page Not Found\n',e,parent = self.root)

if __name__=='__main__':
    root=Tk()
    obj = Dir_win(root)
    root.mainloop()