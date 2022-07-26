from turtle import width
import mysql.connector
import random
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Mov_win:
    def __init__(self,root):
        '''initializes all the necessary widgets onto the Tk'''
        self.root = root
        self,root.title('Movie Information')
        self.root.geometry('1150x540+205+180')
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("Main_Images/movies.ico")

        # ---------------------------vraiables for databse-------------------
        self.var_mov_id = StringVar()
        x = random.randint(1000,9999)
        self.var_mov_id.set(x)

        self.var_mov_title = StringVar()
        self.var_mov_year = StringVar()
        self.var_mov_lang = StringVar()
        self.var_Mov_prodn = StringVar()
        self.var_mov_dir_id = StringVar()
        self.var_mov_budget = IntVar()
        self.var_mov_genre = StringVar()

        #-------------------------- Casting Related Variables---------------------
        self.c_title = StringVar()
        self.c_actor_n_role = StringVar()
        

                        # Title
        lbl_title= Label(self.root,text='Movie Details',font='Castellar 25 bold',fg='burlywood2',bg='black',relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1150,height=35)


        # -------------------------Label Frame-------------------
        lbl_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='Movie Details',padx=2,font='times 14 bold italic')
        lbl_frame.place(x=5,y=38,width=420,height=500)
        
        # ----------labels and Entry fields---------------

        mov_id = Label(lbl_frame,text='MOVIE ID',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        mov_id.grid(row=0,column=0,sticky=W)

        ent_id = ttk.Entry(lbl_frame,textvariable=self.var_mov_id,width=22,font="times 12",state='readonly')
        ent_id.grid(row=0,column=3)

        mov_title = Label(lbl_frame,text='TITLE',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        mov_title.grid(row=1,column=0,sticky=W)

        ent_title = ttk.Entry(lbl_frame,textvariable=self.var_mov_title,width=22,font="times 12")
        ent_title.grid(row=1,column=3)

        mov_year = Label(lbl_frame,text='RELEASE YEAR',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        mov_year.grid(row=3,column=0,sticky=W)

        ent_year = ttk.Entry(lbl_frame,textvariable=self.var_mov_year,width=22,font="times 12")
        ent_year.grid(row=3,column=3)

        
        mov_lang = Label(lbl_frame,text='LANGUAGE',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        mov_lang.grid(row=4,column=0,sticky=W)

        ent_lang = ttk.Entry(lbl_frame,textvariable=self.var_mov_lang,width=22,font="times 12")
        ent_lang.grid(row=4,column=3)

        mov_prodn = Label(lbl_frame,text='PRODUCTION HOUSE ID',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        mov_prodn.grid(row=5,column=0,sticky=W)

        ent_prodn = ttk.Entry(lbl_frame,textvariable=self.var_Mov_prodn,width=22,font="times 12")
        ent_prodn.grid(row=5,column=3)

        mov_director  = Label(lbl_frame,text='DIRECTOR',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        mov_director.grid(row=6,column=0,sticky=W)

        ent_director = ttk.Entry(lbl_frame,textvariable=self.var_mov_dir_id,width=22,font="times 12")
        ent_director.grid(row=6,column=3)

        mov_budget = Label(lbl_frame,text='BUDGET',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        mov_budget.grid(row=7,column=0,sticky=W)

        ent_budget = ttk.Entry(lbl_frame,textvariable=self.var_mov_budget,width=22,font="times 12")
        ent_budget.grid(row=7,column=3)

        mov_genre = Label(lbl_frame,text='GENRE',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        mov_genre.grid(row=8,column=0,sticky=W)


        #------------------------- Combo Box for selecting type of movie--------------
        combo_genre = ttk.Combobox(lbl_frame,textvariable=self.var_mov_genre,font='arial 12 bold',width=18,state='readonly')
        combo_genre['values'] = ('Family','Comedy','Horror','Drama','Action')
        combo_genre.current(0)
        combo_genre.grid(row=8,column=3)

        #------------------------Images for Buttons-------------------------
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
        img_search= img_search.resize((60,30),Image.ANTIALIAS)
        self.img_search=ImageTk.PhotoImage(img_search)

        m_cast = Button(lbl_frame,text='CASTING',font = 'times 12 bold',command=self.casting,fg='white',bg='purple',width=15,height=1).grid(row = 9,column = 0,sticky=W,padx = 10, pady=5)

        #------------------------ Buttons Frame and Buttons--------------------

        
        btn_frame = Frame(lbl_frame,bd = 2, relief=RIDGE)
        btn_frame.place(x=0,y=350,width=413,height=50)

        Add_btn=Button(btn_frame,image=self.img1,command=self.add_data,bg='white',bd=3,relief=RIDGE)
        Add_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,image=self.img2,command=self.update,bg='white',bd=3,relief=RIDGE)
        Update_btn.grid(row=0,column=1)

        Reset_btn=Button(btn_frame,image=self.img4,command=self.reset,bg='white',bd=3,relief=RIDGE)
        Reset_btn.grid(row=0,column=2)

        Delete_btn=Button(btn_frame,image=self.img3,command=self.remove_movie,bg='white',bd=3,relief=RIDGE)
        Delete_btn.grid(row=0,column=3)

        # ---------------------Table Frame--------------------------
        table_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='View Details',padx=2,font='times 14 bold italic')
        table_frame.place(x=430,y=38,width=720,height=500,)


        # --------------------------------Search By Label-------------------------
        lbl_search =Label(table_frame,bd = 2,relief=RIDGE,text='Search By',font='times 12 bold',bg='red',fg='white')
        lbl_search.grid(row=0,column=0,sticky=W)


        # ------------------------------Search Combobox and Entry for Specific Search-----------------------
        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame,textvariable = self.search_var,font='arial 12 bold',width=18,state='readonly')
        combo_search['values'] = ('Title','Language','Release_year','Genre','Budget')
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
        table_data.place(x=0,y=45,width=690,height=400)

        # ------------------------Scroll Bar-------------------------
        Scrollbar_x = ttk.Scrollbar(table_data,orient=HORIZONTAL)
        Scrollbar_y = ttk.Scrollbar(table_data,orient=VERTICAL)
        
        # -------------------------Treeview--------------------------
        self.movie_detalails_table = ttk.Treeview(table_data,columns=('id','title','r_year','language','director','budget','genre','prodn_id'),xscrollcommand=Scrollbar_x.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_x.config(command=self.movie_detalails_table.xview)
        Scrollbar_y.config(command=self.movie_detalails_table.yview)

        # ---------------------Table Heading-----------------------------
        self.movie_detalails_table.heading('id',text='Movie Id')
        self.movie_detalails_table.heading('title',text='Title')
        self.movie_detalails_table.heading('language',text='Language')
        self.movie_detalails_table.heading('r_year',text='Release Year')
        self.movie_detalails_table.heading('director',text='Director')
        self.movie_detalails_table.heading('budget',text='Budget')
        self.movie_detalails_table.heading('genre',text='Genre')
        self.movie_detalails_table.heading('prodn_id',text='Production_id')

        self.movie_detalails_table['show']  ='headings'

        # ----------------------Adjusting the Column Width-------------------
        self.movie_detalails_table.column('id',width=70)
        self.movie_detalails_table.column('title',width=100)
        self.movie_detalails_table.column('language',width=100)
        self.movie_detalails_table.column('prodn_id',width=100)
        self.movie_detalails_table.column('r_year',width=50)
        self.movie_detalails_table.column('director',width=50)
        self.movie_detalails_table.column('budget',width=100)
        self.movie_detalails_table.column('genre',width=100)


        self.movie_detalails_table.pack(fill=BOTH,expand=1)
        self.movie_detalails_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()


    def add_data(self):
        ''' Adds new Movies to the Movie Database '''
        if self.var_mov_title.get()=='' or self.var_mov_lang.get()=='' or self.var_mov_year.get()=='' or self.var_mov_budget.get()=='':
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_mov_lang.get().isdigit():
            messagebox.showerror("Error","The Language cannot be a digit",parent=self.root)
        elif len(self.var_mov_year.get()) > 4:
            messagebox.showerror("Error","Enter a valid Year(Year must be a 4 digit number)",parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('INSERT INTO MOVIES VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(self.var_mov_id.get(),
                                                                                self.var_mov_title.get(),
                                                                                self.var_mov_year.get(),
                                                                                self.var_mov_lang.get(),
                                                                                self.var_mov_dir_id.get(),
                                                                                self.var_mov_budget.get(),
                                                                                self.var_mov_genre.get(),
                                                                                self.var_Mov_prodn.get()
                                                                            ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('Success','Movie added sucessfully',parent=self.root)
            except Exception as e:
                messagebox.showwarning('Warning',f'Something went wrong !{e}',parent=self.root)
            add_data = messagebox.askyesno('Movie Database System','Do you Want to add one more Movie',parent = self.root)
            if add_data > 0:
                self.reset()
            else: pass
            self.reset()

    def fetch_data(self):
        ''' Fetches the data present in the Movie Table '''
        try:
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            my_cursor.execute('SELECT * FROM MOVIES')
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.movie_detalails_table.delete(*self.movie_detalails_table.get_children())
                for i in rows:
                    self.movie_detalails_table.insert('',END,values=i)
            connection.commit()
            connection.close()
        except Exception as e :
            messagebox.showerror('Error',e,parent=self.root)

    def get_cursor(self,event=''):
        ''' Helps in show the data in the table Present in GUI window''' 
        cursor_row = self.movie_detalails_table.focus()
        content = self.movie_detalails_table.item(cursor_row)
        row = content['values']
        self.var_mov_id.set(row[0])
        self.var_mov_title.set(row[1])
        self.var_mov_year.set(row[2])
        self.var_mov_lang.set(row[3])
        self.var_mov_dir_id.set(row[4])
        self.var_mov_budget.set(row[5])
        self.var_mov_genre.set(row[6])
        self.var_Mov_prodn.set(row[7])

    def update(self):
        ''' Used for updating the fields/attribute values in a table'''
        try:    
            if self.var_mov_title.get() == '' or self.var_mov_budget.get() == '' or self.var_mov_lang.get() == '' :
                messagebox.showerror('Error','Please enter the Movie Title field...!',parent=self.root)
            elif self.var_mov_lang.get().isdigit():
                messagebox.showerror("Error","The Language cannot be a digit",parent=self.root)
            elif len(self.var_mov_year.get()) > 4:
                messagebox.showerror("Error","Enter a valid Year(Year must be a 4 digit number)",parent=self.root)
            else:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('UPDATE MOVIES SET title = %s, release_year = %s, language = %s, prodn_id = %s, budget = %s, genre = %s WHERE mov_id =%s',(
                                                                                                                                            self.var_mov_title.get(),
                                                                                                                                            self.var_mov_year.get(),
                                                                                                                                            self.var_mov_lang.get(),
                                                                                                                                            self.var_Mov_prodn.get(),                                                                                                                                        self.var_mov_budget.get(),
                                                                                                                                            self.var_mov_genre.get(),
                                                                                                                                            self.var_mov_id.get()
                                                                                                                                            ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('UPDATE','Movie Data Updated Successfully....!',parent=self.root)
                self.reset()
        except EXCEPTION as e:
            messagebox.showerror('Error',e,parent=self.root)

    def remove_movie(self):
        ''' Removes a selected Row/Tuple fromm the table '''
        if self.var_mov_title.get() == '':
            messagebox.showerror('Error','Please select a item from the table to Delete...!',parent=self.root)
        else:
            try:
                remove_movie = messagebox.askyesno('Movie Database System','Do You Want to Delete This Movie Data ?',parent = self.root)
                if remove_movie > 0:
                    connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                    my_cursor = connection.cursor()
                    Del_query = "DELETE FROM MOVIES WHERE mov_id=%s"
                    value = (self.var_mov_id.get(),)                        
                    my_cursor.execute(Del_query,value)
                    messagebox.showinfo('Success','Movie Data Removed Successfully....!',parent=self.root)
                else:
                    if not remove_movie:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()
                self.reset()
            except Exception as e:
                messagebox.showerror('Error',e,parent = self.root)

    def reset(self):
        ''' Used for resetting the values a selected record '''
        x = random.randint(1000,9999)
        self.var_mov_id.set(x)
        self.var_mov_title.set(''),
        self.var_mov_year.set(''),
        self.var_mov_lang.set(''),
        self.var_Mov_prodn.set('')
        self.var_mov_dir_id.set(''),
        self.var_mov_budget.set(''),
        
    def search(self):
        '''Helps the user to search for a particular record'''
        try:
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            search_value = self.txt_search.get()
            if search_value == '':
                messagebox.showwarning('Warn','Please enter text in the Search box !',parent = self.root)
            my_cursor.execute("select * from Movies where "+str(self.search_var.get())+" like '%"+search_value+"%'")
            rows = my_cursor.fetchall()
            if len(rows) == 0:
                messagebox.showerror('Error','The search object does not exits 😢',parent = self.root)
            else:
                self.movie_detalails_table.delete(*self.movie_detalails_table.get_children())
                for i in rows:
                    self.movie_detalails_table.insert('',END,values=i)
                    connection.commit()
            connection.close()
        except Exception as e:
            messagebox.showerror('Error',e,parent = self.root)

    def casting(self):
        '''Opens a new window having the information about the actors casting information in a selected movie'''
        Act_n_Role = ''
        #a_n_r is a temporary list
        a_n_r = [] 
        self.top = Toplevel(self.root)
        self.top.geometry("400x400+250+200")
        self.top.title("Casting")
        self.top.resizable(False,False)
        self.about_casting =LabelFrame(self.top,bd = 2,relief=RIDGE,text='View Details',padx=2,font='times 14 bold italic')
        self.about_casting.place(x=10,y=0,width=380,height=385)
        lbl1 = Label(self.about_casting,text= 'Movie name :',font='times 14 bold italic')
        lbl1.grid(row=0,column=1)
        lbl2 = Label(self.about_casting,text= 'Cast :',font='times 14 bold italic')
        lbl2.grid(row=1,column=1,sticky=W)
        try:
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            
            query = '''select m.title, a.Act_name, c.role
                        from casting c, movies m,actor a
                        where c.movie_id = m.mov_id and c.Act_id = a.Act_id and m.mov_id = %s '''
            value = (self.var_mov_id.get(),)
            
            my_cursor.execute(query,value)
            row = my_cursor.fetchall()
            self.c_title.set(row[0][0])
            
            for i in range(0,len(row)):
                a_n_r.append(f'{row[i][1]} Casing as {row[i][2]}')

            a_n_r_1 = '\n'.join(a_n_r) #a_n_r_1 is a temprary string
            self.c_actor_n_role.set(a_n_r_1)
            Act_n_Role = self.c_actor_n_role.get()
            ent_movie = ttk.Entry(self.about_casting,textvariable=self.c_title,width=22,font="times 12")
            ent_movie.grid(row=0,column=2)
            
            self.ent_aboutActor = Text(self.about_casting,font="times 12",width=40,height=10)
            self.ent_aboutActor.place(x=19,y=50)
            self.ent_aboutActor.insert(INSERT,Act_n_Role)
            connection.commit()
            connection.close()
        except Exception as e:
            messagebox.showerror('Failed',f'Something went wrong....!\n{e}',parent = self.root)
        
if __name__=='__main__':
    root=Tk()
    obj = Mov_win(root)
    root.mainloop()
