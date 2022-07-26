import random
import wikipedia
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector

class Prodn_win:
    def __init__(self,root):
        '''initializes all the necessary widgets onto the Tk'''
        self.root = root
        self,root.title('Production company Information')
        self.root.geometry('1150x540+205+180')
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("Main_Images/movies.ico")

        self.var_prodn_id = StringVar()
        x = random.randint(1,99)
        self.var_prodn_id.set(x)

        self.var_prodn_name = StringVar()
        self.var_prodn_addr = StringVar()
        self.var_TOT_amt = IntVar()

        #-------------------------Title-------------------------
        lbl_title= Label(self.root,text='Production Company Details',font='Castellar 25 bold',fg='burlywood2',bg='black',relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1140,height=35)

        # -------------------------Label Frame-------------------
        lbl_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='Company Details',padx=2,font='times 14 bold italic')
        lbl_frame.place(x=5,y=38,width=420,height=500)

        # ----------labels and Entry fields---------------

        prodn_id = Label(lbl_frame,text='Company ID',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        prodn_id.grid(row=0,column=0,sticky=W)

        ent_id = ttk.Entry(lbl_frame,textvariable=self.var_prodn_id,width=22,font="times 12",state='readonly')
        ent_id.grid(row=0,column=4)

        prodn_name = Label(lbl_frame,text='Name',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        prodn_name.grid(row=1,column=0,sticky=W)

        ent_prodn_name = ttk.Entry(lbl_frame,textvariable=self.var_prodn_name,width=22,font="times 12")
        ent_prodn_name.grid(row=1,column=4)

        prodn_addr = Label(lbl_frame,text='Address',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        prodn_addr.grid(row=2,column=0,sticky=W)

        ent_prodn_addr = ttk.Entry(lbl_frame,textvariable=self.var_prodn_addr,width=22,font="times 12")
        ent_prodn_addr.grid(row=2,column=4)

        TOT_INVST = Label(lbl_frame,text='Total Investment',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        TOT_INVST.grid(row=3,column=0,sticky=W)

        ent_tot_invst = ttk.Entry(lbl_frame,textvariable=self.var_TOT_amt,width=22,font="times 12",state='readonly')
        ent_tot_invst.grid(row=3,column=4)

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

        #------------------------ Buttons Frame and Buttons-----------------------
        btn_frame = Frame(lbl_frame,bd = 2, relief=RIDGE)
        btn_frame.place(x=0,y=390,width=413,height=50)

        Add_btn=Button(btn_frame,image=self.img1,command=self.add_data,bg='white',bd=3,relief=RIDGE)
        Add_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,image=self.img2,command=self.update,bg='white',bd=3,relief=RIDGE)
        Update_btn.grid(row=0,column=1)

        Reset_btn=Button(btn_frame,image=self.img4,command=self.reset,bg='white',bd=3,relief=RIDGE)
        Reset_btn.grid(row=0,column=2)

        Delete_btn=Button(btn_frame,image=self.img3,command=self.remove_data,bg='white',bd=3,relief=RIDGE)
        Delete_btn.grid(row=0,column=3)

        btnAbout = Button(lbl_frame,text='About Company',command=self.about_prodn,width=7,font='arial 16 bold',bg = 'blue',fg = 'white')
        btnAbout.place(x=100,y=150,width=170,height=30)

        self.ent_about_prod_company = Text(lbl_frame,width=22,font="times 12")
        self.ent_about_prod_company.place(x=10,y=190,width=390,height=175)

        # ---------------------Table Frame--------------------------
        table_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='View Details',padx=2,font='times 14 bold italic')
        table_frame.place(x=430,y=38,width=720,height=500,)

        # --------------------------------Search By Label-------------------------
        lbl_search =Label(table_frame,bd = 2,relief=RIDGE,text='Search By',font='times 12 bold',bg='red',fg='white')
        lbl_search.grid(row=0,column=0,sticky=W)


        # ------------------------------Search Combobox and Entry for Specific Search-----------------------
        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame,textvariable = self.search_var,font='arial 12 bold',width=18,state='readonly')
        combo_search['values'] = ('prodn_id','prodn_name','prodn_addr')
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
        self.prodn_details_table = ttk.Treeview(table_data,columns=('id','Name','addr','tot_invst'),xscrollcommand=Scrollbar_x.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_x.config(command=self.prodn_details_table.xview)
        Scrollbar_y.config(command=self.prodn_details_table.yview)

        # ---------------------Table Heading-----------------------------
        self.prodn_details_table.heading('id',text='Company Id')
        self.prodn_details_table.heading('Name',text='Company Name')
        self.prodn_details_table.heading('addr',text='Address')
        self.prodn_details_table.heading('tot_invst',text='Investment')

        self.prodn_details_table['show']  ='headings'

        # ----------------------Adjusting the Column Width-------------------
        self.prodn_details_table.column('id',width=70)
        self.prodn_details_table.column('Name',width=200)
        self.prodn_details_table.column('addr',width=100)
        self.prodn_details_table.column('tot_invst',width=100)

        self.prodn_details_table.pack(fill=BOTH,expand=1)
        self.prodn_details_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()
    #---------------------------All the necessary methods----------------------
    
    def add_data(self):
        ''' Adds new Production Company to the Movie Database '''
        if self.var_prodn_name.get()=='':
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_prodn_name.get().isdigit():
             messagebox.showerror("Error","The name field must be a valid name",parent=self.root)
        elif self.var_prodn_addr.get().isdigit():
             messagebox.showerror("Error","Enter a valid Address",parent=self.root)
        elif self.var_prodn_addr.get().isdigit():
             messagebox.showerror("Error","Please enter a valid address....!",parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('INSERT INTO prod_company VALUES(%s,%s,%s,%s)',(self.var_prodn_id.get(),
                                                                                self.var_prodn_name.get(),
                                                                                self.var_prodn_addr.get(),
                                                                                self.var_TOT_amt.get()
                                                                            ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('Success','Production Company added sucessfully',parent=self.root)
            except Exception as e:
                messagebox.showwarning('Warning',f'Something went wrong !{e}',parent=self.root)
            add_data = messagebox.askyesno('Movie Database System','Do you Want to add more Production Companies',parent = self.root)
            if add_data > 0:
                self.reset()
            else: pass
            self.reset()

    def remove_data(self):
        ''' Removes a selected Row/Tuple fromm the table as well as in the database '''
        if self.var_prodn_name.get() == '':
            messagebox.showerror('Error','Please enter the Company Name field...!',parent=self.root)
        else:
            remove_prodn = messagebox.askyesno("Movie Database System","Do You Want to Delete this Production company Data ?",parent = self.root)
            try:
                if remove_prodn > 0:
                    connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                    my_cursor = connection.cursor()
                    Del_query = "DELETE FROM prod_company WHERE prodn_id=%s"
                    value = (self.var_prodn_id.get(),)                        
                    my_cursor.execute(Del_query,value)
                    messagebox.showinfo("Success","Production company's Data Removed Successfully....!",parent=self.root)
                else:
                    if not remove_prodn:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()
                self.reset()
            except Exception as e:
                messagebox.showerror('Error',e,parent = self.root)

    def reset(self):
        ''' Used for resetting the values a selected record '''
        x = random.randint(1,99)
        self.var_prodn_id.set(x),
        self.var_prodn_name.set(''),
        self.var_prodn_addr.set(''),
        self.var_TOT_amt.set(0)

    def fetch_data(self):
        ''' Fetches the data present in the Production Company Table '''
        try:    
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            my_cursor.execute('SELECT * FROM prod_company')
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.prodn_details_table.delete(*self.prodn_details_table.get_children())
                for i in rows:
                    self.prodn_details_table.insert('',END,values=i)
            connection.commit()
            connection.close()
        except Exception as e:
            messagebox.showerror('Error',e,parent = self.root)

    def search(self):
        '''Searches a particular Item in the table'''
        try:    
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            search_value = self.txt_search.get()
            if search_value == '':
                messagebox.showwarning('Warn','Please enter text in the Search box !',parent = self.root)
            my_cursor.execute("select * from prod_company where "+str(self.search_var.get())+" like '%"+search_value+"%'")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.prodn_details_table.delete(*self.prodn_details_table.get_children())
                for i in rows:
                    self.prodn_details_table.insert('',END,values=i)
            else:
                messagebox.showerror('Error','The search item is not found in the list....')
            connection.commit()
            connection.close()
        except Exception as e:
            messagebox.showerror('Error',e,parent = self.root)

    def update(self):
        ''' Used for updating the fields/attribute values in a table'''
        if self.var_prodn_name.get() == '' or self .var_prodn_addr.get() == '':
            messagebox.showerror('Error','Please enter the values in all fields...!',parent=self.root)
        elif self.var_prodn_name.get().isdigit():
            messagebox.showerror('Error','Production Company name cannot be a number')
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('UPDATE prod_company SET prodn_name = %s, prodn_addr = %s WHERE prodn_id =%s',(
                                                                                                        self.var_prodn_name.get(),
                                                                                                        self.var_prodn_addr.get(),
                                                                                                        self.var_prodn_id.get()
                                                                                                    ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('UPDATE','Production Company Data Updated Successfully....!',parent=self.root)
                self.reset()
            except Exception as e:
                messagebox.showerror('Error',e,parent = self.root)
                
    def get_cursor(self,event=''):
        ''' Helps in show the data in the table Present in GUI window''' 
        cursor_row = self.prodn_details_table.focus()
        content = self.prodn_details_table.item(cursor_row)
        row = content['values']
        self.var_prodn_id.set(row[0])
        self.var_prodn_name.set(row[1]),
        self.var_prodn_addr.set(row[2]),
        self.var_TOT_amt.set(row[3])

    def about_prodn(self):
        '''Gives a brief information about the Production company'''
        try:
            self.ent_about_prod_company.delete(1.0,END)
            company=self.var_prodn_name.get()
            self.ent_about_prod_company.insert(INSERT, wikipedia.summary(str(company)))
        except Exception as e:
            messagebox.showerror('Page Not Found\n',e)

if __name__=='__main__':
    root=Tk()
    obj = Prodn_win(root)
    root.mainloop()