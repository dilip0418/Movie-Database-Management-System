from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Rev_win:
    def __init__(self,root):
        '''initializes all the necessary widgets onto the Tk'''
        self.root = root
        self.root.title('Rating Information')
        self.root.geometry('950x340+375+280')
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("Main_Images/movies.ico")


        #------------Variables------------------
        self.var_mov_id = StringVar()
        self.var_mov_title = StringVar()
        self.var_mov_rating = StringVar()

         #-------------------------Title-------------------------
        lbl_title= Label(self.root,justify='center',text='Review Details',font='Castellar 25 bold',fg='burlywood2',bg='black',relief=RIDGE)
        lbl_title.place(x=0,y=0,width=950,height=35)

        # -------------------------Label Frame-------------------
        lbl_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='Review Details',padx=2,font='times 14 bold italic')
        lbl_frame.place(x=5,y=38,width=400,height=300)

        # ----------labels and Entry fields---------------

        mov_id = Label(lbl_frame,text='MOVIE ID',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        mov_id.grid(row=0,column=0,sticky=W)

        ent_id = ttk.Entry(lbl_frame,textvariable=self.var_mov_id,width=22,font="times 12")
        ent_id.grid(row=0,column=3)


        #----------Fetch Button-------------
        fetchbtn = Button(lbl_frame,text='Fetch data',command=self.fetch_movie,font='arial 11 bold',borderwidth=0,bg='green',fg='white',width=10)
        fetchbtn.grid(row=0,column=4,padx=10)

        # ----------labels and Entry fields---------------
        
        mov_title = Label(lbl_frame,text='MOVIE TITLE',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        mov_title.grid(row=1,column=0,sticky=W)
        
        ent_title = ttk.Entry(lbl_frame,textvariable=self.var_mov_title,width=22,font="times 12")
        ent_title.grid(row=1,column=3)

        rating = Label(lbl_frame,text='RATING',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        rating.grid(row=2,column=0,sticky=W)

        ent_rating = ttk.Entry(lbl_frame,textvariable=self.var_mov_rating,width=22,font="times 12")
        ent_rating.grid(row=2,column=3)


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

        #------------------------ Buttons Frame and Buttons--------------------

        
        btn_frame = Frame(lbl_frame,bd = 2, relief=RIDGE)
        btn_frame.place(x=60,y=190,width=290, height=50)

        Add_btn=Button(btn_frame,command=self.rate,image=self.img1,bg='white',bd=0,relief=RIDGE)
        Add_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,command=self.update,image=self.img2,bg='white',bd=0,relief=RIDGE)
        Update_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,command=self.reset,image=self.img4,bg='white',bd=0,relief=RIDGE)
        Reset_btn.grid(row=0,column=4)

        # Delete_btn=Button(btn_frame,image=self.img3,bg='white',bd=0,relief=RIDGE)
        # Delete_btn.grid(row=0,column=3)

        # ---------------------Table Frame--------------------------
        table_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='View Details',padx=2,font='times 14 bold italic')
        table_frame.place(x=410,y=38,width=535,height=300,)

        # --------------------------------Search By Label-------------------------
        lbl_search =Label(table_frame,bd = 2,relief=RIDGE,text='Search By',font='times 12 bold',bg='red',fg='white')
        lbl_search.grid(row=0,column=0,sticky=W)


        # ------------------------------Search Combobox and Entry for Specific Search-----------------------
        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame,textvariable = self.search_var,font='arial 12 bold',width=15,state='readonly')
        combo_search['values'] = ('Mov_Id','Title','Rating')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=12)

        self.txt_search = StringVar()
        ent_search = ttk.Entry(table_frame,textvariable = self.txt_search,width=22,font="times 12")
        ent_search.grid(row=0,column=2,padx=7)


        # -----------------------------Search annd Show All Buttons-------------------------
        btnSearch = Button(table_frame,command=self.search,image=self.img_search,width=75,height=40,bd=0)
        btnSearch.grid(row=0,column=3)

        btnShowAll = Button(table_frame,command=self.fetch_data,text='Show All',width=7,height=1,font='arial 11 bold',bg = 'green',fg = 'white')
        btnShowAll.place(x = 430,y = 246,width=90,height=25)

        # --------------------------Show Data Table----------------------------
        table_data =LabelFrame(table_frame,bd = 2,relief=RIDGE)
        table_data.place(x=0,y=45,width=530,height=190)

        # ------------------------Scroll Bar-------------------------
        Scrollbar_x = ttk.Scrollbar(table_data,orient=HORIZONTAL)
        Scrollbar_y = ttk.Scrollbar(table_data,orient=VERTICAL)
        
        # -------------------------Treeview--------------------------
        self.rating_detalails_table = ttk.Treeview(table_data,columns=('id','title','rating'),xscrollcommand=Scrollbar_x.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_x.config(command=self.rating_detalails_table.xview)
        Scrollbar_y.config(command=self.rating_detalails_table.yview)

        # ---------------------Table Heading-----------------------------
        self.rating_detalails_table.heading('id',text='Movie Id')
        self.rating_detalails_table.heading('title',text='Title')
        self.rating_detalails_table.heading('rating',text='Rating')

        self.rating_detalails_table['show']  ='headings'

        # ----------------------Adjusting the Column Width-------------------
        self.rating_detalails_table.column('id',width=30)
        self.rating_detalails_table.column('title',width=150)
        self.rating_detalails_table.column('rating',width=20)

        self.rating_detalails_table.pack(fill=BOTH,expand=1)
        self.rating_detalails_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()


    def fetch_movie(self):
        if self.var_mov_id.get() == '':
            messagebox.showerror('Error','Please enter the Movie Id',parent =self.root)
        elif not self.var_mov_id.get().isdigit():
            messagebox.showerror('Error ','The movie id can only be in digits',parent=self.root)
        else:
            try:    
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                query = ("SELECT title FROM MOVIES WHERE mov_id=%s")
                Value = (self.var_mov_id.get(),)
                my_cursor.execute(query,Value)
                movie_title = my_cursor.fetchone()
                
                if movie_title == None:
                    messagebox.showerror('Failed','No movie available with this movie id',parent = self.root)
                else:
                    messagebox.showinfo('Successful','Data fetched Wonderfully',parent = self.root)
                    self.var_mov_title.set(movie_title[0])
                    connection.commit()
                    connection.close()
            except Exception as e:
                messagebox.showerror('Unsuccessful',e,parent = self.root)
    
    def rate(self):
        '''Used for rating a particular movie'''
        if self.var_mov_id.get() == '' or self.var_mov_title.get() == '' or self.var_mov_rating.get() =='':
            messagebox.showerror('Error','Empty entries found\nPlease fill the entries and then proceed again...!',parent = self.root)
        else:
            try:    
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('INSERT INTO RATINGS VALUES(%s,%s,%s)',(self.var_mov_id.get(),
                                                                        self.var_mov_title.get(),
                                                                        self.var_mov_rating.get()
                                                                        ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('Success','Ratings added sucessfully',parent=self.root)
            except Exception as e:
                messagebox.showwarning('Warning',f'Something went wrong !{e}',parent=self.root)


    def fetch_data(self):
        ''' Fetches the data present in the Ratings Table '''
        connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
        my_cursor = connection.cursor()
        my_cursor.execute('SELECT * FROM RATINGS')
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.rating_detalails_table.delete(*self.rating_detalails_table.get_children())
            for i in rows:
                self.rating_detalails_table.insert('',END,values=i)
        connection.commit()
        connection.close()

    def get_cursor(self,event=''):
        ''' Helps in show the data in the table Present in GUI window''' 
        cursor_row = self.rating_detalails_table.focus()
        content = self.rating_detalails_table.item(cursor_row)
        row = content['values']
        self.var_mov_id.set(row[0])
        self.var_mov_title.set(row[1])
        self.var_mov_rating.set(row[2])
    
    def update(self):
        ''' Used for updating the fields/attribute values in a table'''
        if self.var_mov_id.get() == '' or self.var_mov_rating == '':
            messagebox.showerror('Failed','All entries need to be filled...!',parent = self.root)
        else:
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            my_cursor.execute('UPDATE RATINGS SET rating = %s WHERE mov_id =%s',(
                                                                                self.var_mov_rating.get(),
                                                                                self.var_mov_id.get()
                                                                                ))
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo('UPDATE','Ratings Data Updated Successfully....!',parent=self.root)
            self.reset()

    def reset(self):
        '''Used for resetting the values a selected record '''
        self.var_mov_id.set('')
        self.var_mov_title.set(''),
        self.var_mov_rating.set('')

    def search(self):
        '''Helps the user to search for a particular record'''
        connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
        my_cursor = connection.cursor()
        search_value = self.txt_search.get()
        if search_value == '':
            messagebox.showwarning('Warn','Please enter text in the Search box !',parent = self.root)
        my_cursor.execute("select * from ratings where "+str(self.search_var.get())+" like '%"+search_value+"%'")
        rows = my_cursor.fetchall()
        if len(rows) == 0:
            messagebox.showerror('Error','The search object does not exits 😢',parent = self.root)
        else:
            self.rating_detalails_table.delete(*self.rating_detalails_table.get_children())
            for i in rows:
                self.rating_detalails_table.insert('',END,values=i)
                connection.commit()
        connection.close()

if __name__=='__main__':
    root=Tk()
    obj = Rev_win(root)
    root.mainloop()