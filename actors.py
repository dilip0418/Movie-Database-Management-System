import random
import wikipedia
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Act_win:
    def __init__(self,root):
        '''initializes all the necessary widgets onto the Tk'''
        self.root = root
        self.root.title('Actors Information')
        self.root.geometry('1150x540+205+180')
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("Main_Images/movies.ico")
        
        self.var_act_id = StringVar()
        x = random.randint(10000,99999)
        self.var_act_id.set(x)

        self.var_act_name = StringVar()
        self.var_act_gender = StringVar()

        #-------------------------Title-------------------------
        lbl_title= Label(self.root,text='Actor Details',font='Castellar 25 bold',fg='burlywood2',bg='black',relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1140,height=35)

        # -------------------------Label Frame-------------------
        lbl_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='Actor Details',padx=2,font='times 14 bold italic')
        lbl_frame.place(x=5,y=38,width=420,height=500)


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

        # ----------labels and Entry fields---------------

        act_id = Label(lbl_frame,text='Actor ID',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        act_id.grid(row=0,column=0,sticky=W)

        ent_id = ttk.Entry(lbl_frame,textvariable=self.var_act_id,width=22,font="times 12",state='readonly')
        ent_id.grid(row=0,column=4)

        act_name = Label(lbl_frame,text='Name',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        act_name.grid(row=1,column=0,sticky=W)

        ent_act_name = ttk.Entry(lbl_frame,textvariable=self.var_act_name,width=22,font="times 12")
        ent_act_name.grid(row=1,column=4)

        act_gender = Label(lbl_frame,text='GENDER',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        act_gender.grid(row=3,column=0,sticky=W)

        #------------------------- Combo Box for selecting type of movie--------------
        combo_gender = ttk.Combobox(lbl_frame,textvariable=self.var_act_gender,font='arial 12 bold',width=18,state='readonly')
        combo_gender['values'] = ('Male','Female','Others')
        combo_gender.current(0)
        combo_gender.grid(row=3,column=4)


        #------------------------ Buttons Frame and Buttons
        btn_frame = Frame(lbl_frame,bd = 2, relief=RIDGE)
        btn_frame.place(x=0,y=350,width=413,height=50)

        Add_btn=Button(btn_frame,image=self.img1,command=self.add_data,bg='white',bd=3,relief=RIDGE)
        Add_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,image=self.img2,command=self.update,bg='white',bd=3,relief=RIDGE)
        Update_btn.grid(row=0,column=1)

        Reset_btn=Button(btn_frame,image=self.img4,command=self.reset,bg='white',bd=3,relief=RIDGE)
        Reset_btn.grid(row=0,column=2)

        Delete_btn=Button(btn_frame,image=self.img3,command=self.remove_actor,bg='white',bd=3,relief=RIDGE)
        Delete_btn.grid(row=0,column=3)

        btnAbout = Button(lbl_frame,text='About Actor',command=self.about_actor,width=7,font='arial 16 bold',bg = 'blue',fg = 'white')
        btnAbout.place(x=100,y=120,width=150,height=30)

        self.ent_aboutActor = Text(lbl_frame,width=22,font="times 12")
        self.ent_aboutActor.place(x=10,y=160,width=380,height=175)
        

        # ---------------------Table Frame--------------------------
        table_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='View Details',padx=2,font='times 14 bold italic')
        table_frame.place(x=430,y=38,width=720,height=500,)

        # --------------------------------Search By Label-------------------------
        lbl_search =Label(table_frame,bd = 2,relief=RIDGE,text='Search By',font='times 12 bold',bg='red',fg='white')
        lbl_search.grid(row=0,column=0,sticky=W)


        # ------------------------------Search Combobox and Entry for Specific Search-----------------------
        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame,textvariable = self.search_var,font='arial 12 bold',width=18,state='readonly')
        combo_search['values'] = ('Act_name','Act_id')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=15)

        self.txt_search = StringVar()
        ent_search = ttk.Entry(table_frame,textvariable = self.txt_search,width=22,font="times 12")
        ent_search.grid(row=0,column=2,padx=10)

        
        # -----------------------------Search annd Show All Buttons-------------------------
        btnSearch = Button(table_frame,image=self.img_search,command=self.search,width=85,height=40,bd=0)
        btnSearch.grid(row=0,column=3)

        btnShowAll = Button(table_frame,text='show all',width=6,command=self.fetch_data,height=1,font='arial 16 bold',bg = 'blue',fg = 'white')
        btnShowAll.grid(row=0,column=7)
        

        # --------------------------Show Data Table----------------------------
        table_data =LabelFrame(table_frame,bd = 2,relief=RIDGE)
        table_data.place(x=0,y=45,width=680,height=400)

        # ------------------------Scroll Bar-------------------------
        Scrollbar_x = ttk.Scrollbar(table_data,orient=HORIZONTAL)
        Scrollbar_y = ttk.Scrollbar(table_data,orient=VERTICAL)
        
        # -------------------------Treeview--------------------------
        self.actor_detalails_table = ttk.Treeview(table_data,columns=('id','Name','gender'),xscrollcommand=Scrollbar_x.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_x.config(command=self.actor_detalails_table.xview)
        Scrollbar_y.config(command=self.actor_detalails_table.yview)

        # ---------------------Table Heading-----------------------------
        self.actor_detalails_table.heading('id',text='Actor Id')
        self.actor_detalails_table.heading('Name',text='Name')
        self.actor_detalails_table.heading('gender',text='Gender')
        self.actor_detalails_table['show']  ='headings'

        # ----------------------Adjusting the Column Width-------------------
        self.actor_detalails_table.column('id',width=70)
        self.actor_detalails_table.column('Name',width=200)
        self.actor_detalails_table.column('gender',width=70)


        self.actor_detalails_table.pack(fill=BOTH,expand=1)
        self.actor_detalails_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()


    def add_data(self):
        ''' Adds new Actors to the Movie Database '''
        if self.var_act_name.get()=='' or self.var_act_gender.get() == '':
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_act_name.get().isdigit():
             messagebox.showerror("Error","The name field must be a valid name",parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('INSERT INTO ACTOR VALUES(%s,%s,%s)',(self.var_act_id.get(),
                                                                                self.var_act_name.get(),
                                                                                self.var_act_gender.get(),
                                                                            ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('Success','Actor added sucessfully',parent=self.root)
            except Exception as e:
                messagebox.showwarning('Warning',f'Something went wrong !{e}',parent=self.root)
            add_data = messagebox.askyesno('Movie Database System','Do you Want to add one more Actor',parent = self.root)
            if add_data > 0:
                self.reset()
            else: pass

    def fetch_data(self):
        ''' Fetches the data present in the Actor Table '''
        try:
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            my_cursor.execute('SELECT * FROM ACTOR')
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.actor_detalails_table.delete(*self.actor_detalails_table.get_children())
                for i in rows:
                    self.actor_detalails_table.insert('',END,values=i)
            connection.commit()
            connection.close()
        except Exception as e:
            messagebox.showerror('Error',e,parent = self.root)
            
    def get_cursor(self,event=''):
        ''' Helps in show the data in the table Present in GUI window''' 
        cursor_row = self.actor_detalails_table.focus()
        content = self.actor_detalails_table.item(cursor_row)
        row = content['values']
        self.var_act_id.set(row[0])
        self.var_act_name.set(row[1]),
        self.var_act_gender.set(row[2])

    def update(self):
        ''' Used for updating the fields/attribute values in a table'''
        if self.var_act_name.get() == '':
            messagebox.showerror('Error','Please enter the Actor Name field...!',parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('UPDATE ACTOR SET Act_name = %s, Act_gender = %s WHERE Act_id =%s',(
                                                                                                        self.var_act_name.get(),
                                                                                                        self.var_act_gender.get(),
                                                                                                        self.var_act_id.get()
                                                                                                    ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('UPDATE','Actor Data Updated Successfully....!',parent=self.root)
            except Exception as e:
                messagebox.showerror('Error',e,parent = self.root)

    def remove_actor(self):
        ''' Removes a selected Row/Tuple fromm the table '''
        if self.var_act_name.get() == '':
            messagebox.showerror('Error','Please enter the Actor Name field...!',parent=self.root)
        else:
            remove_actor = messagebox.askyesno("Actor Database System","Do You Want to Delete This Actor's Data ?",parent = self.root)
            try:
                if remove_actor > 0:
                    connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                    my_cursor = connection.cursor()
                    Del_query = "DELETE FROM ACTOR WHERE Act_id=%s"
                    value = (self.var_act_id.get(),)                        
                    my_cursor.execute(Del_query,value)
                    messagebox.showinfo("Success","Actor's Data Removed Successfully....!",parent=self.root)
                else:
                    if not remove_actor:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()
            except Exception as e:
                messagebox.showerror('Error',e,parent = self.root)

    def reset(self):
        ''' Used for resetting the values a selected record '''
        if self.var_act_name.get() == '':
            messagebox.showerror('Error','The Actor Name field is Empty...!',parent=self.root)
        else:
            x = random.randint(10000,99999)
            self.var_act_id.set(x)
            self.var_act_name.set(''),
            self.var_act_gender.set('')

    def search(self):
        '''Helps the user to search for a particular record'''
        try:
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            search_value = self.txt_search.get()
            if search_value == '':
                messagebox.showwarning('Warn','Please enter text in the Search box !',parent = self.root)
            my_cursor.execute("select * from Actor where "+str(self.search_var.get())+" like '%"+search_value+"%'")
            rows = my_cursor.fetchall()
            if len(rows) == 0:
                messagebox.showerror('Error','The search object does not exits 😢',parent = self.root)
            else:
                self.actor_detalails_table.delete(*self.actor_detalails_table.get_children())
                for i in rows:
                    self.actor_detalails_table.insert('',END,values=i)
                    connection.commit()
            connection.close()
        except Exception as e:
            messagebox.showerror('Error',e,parent = self.root)
            
        
    def about_actor(self):
        try:
            self.ent_aboutActor.delete(1.0,END)
            actor=self.var_act_name.get()
            self.ent_aboutActor.insert(INSERT, wikipedia.summary(str(actor)))
        except Exception as e:
            messagebox.showerror('Page Not Found',e,parent=self.root)

if __name__=='__main__':
    root=Tk()
    obj = Act_win(root)
    root.mainloop()