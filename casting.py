from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class cast_win:
    def __init__(self,root):
        '''initializes all the necessary widgets onto the Tk'''
        self.root = root
        self.root.title('Casting Information')
        self.root.geometry('950x310+375+280')
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("Main_Images/movies.ico")


        #------------Variables------------------
        self.var_mov_id = StringVar()
        self.var_Act_id = StringVar()
        self.var_Act_Role = StringVar()

         #-------------------------Title-------------------------
        lbl_title= Label(self.root,justify='center',text='Casting Details',font='Castellar 25 bold',fg='burlywood2',bg='black',relief=RIDGE)
        lbl_title.place(x=0,y=0,width=950,height=35)

        # -------------------------Label Frame-------------------
        lbl_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='Casting Details',padx=2,font='times 14 bold italic')
        lbl_frame.place(x=5,y=38,width=400,height=300)

        # ----------labels and Entry fields---------------

        mov_id = Label(lbl_frame,text='MOVIE ID',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        mov_id.grid(row=0,column=0,sticky=W)

        ent_id = ttk.Entry(lbl_frame,textvariable=self.var_mov_id,width=22,font="times 12")
        ent_id.grid(row=0,column=3)



        Act_id = Label(lbl_frame,text='ACTOR ID',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        Act_id.grid(row=1,column=0,sticky=W)

        ent_Act_id = ttk.Entry(lbl_frame,textvariable=self.var_Act_id,width=22,font="times 12")
        ent_Act_id.grid(row=1,column=3)

        role = Label(lbl_frame,text='ROLE',font = 'times 12 bold',padx=2,pady=6,fg='crimson')
        role.grid(row=2,column=0,sticky=W)

        ent_role = ttk.Entry(lbl_frame,textvariable=self.var_Act_Role,width=22,font="times 12")
        ent_role.grid(row=2,column=3)


        #------------------------Images for Buttons-------------------------
        img_add=Image.open("Main_Images/add.jpg")
        img_add= img_add.resize((94,50),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img_add)


        Add_btn=Button(lbl_frame,command=self.add_data,image=self.img1,bg='white',bd=0,relief=RIDGE)
        Add_btn.grid(row=5,column=3)



        # ---------------------Table Frame--------------------------
        table_frame =LabelFrame(self.root,bd = 2,relief=RIDGE,text='View Details',padx=2,font='times 14 bold italic')
        table_frame.place(x=410,y=38,width=535,height=270)

        #--------------------------Table Heading-----------------------------------
        t_heading = Label(table_frame,justify='center',text = 'Casting Details Table',font ='times 20 bold', fg = 'white',bg = 'green').grid(row=0,column=0)



        # --------------------------Show Data Table----------------------------
        table_data =LabelFrame(table_frame,bd = 2,relief=RIDGE)
        table_data.place(x=0,y=45,width=530,height=170)

        # ------------------------Scroll Bar-------------------------
        Scrollbar_x = ttk.Scrollbar(table_data,orient=HORIZONTAL)
        Scrollbar_y = ttk.Scrollbar(table_data,orient=VERTICAL)
        
        # -------------------------Treeview--------------------------
        self.casting_details_table = ttk.Treeview(table_data,columns=('m_id','a_id','role'),xscrollcommand=Scrollbar_x.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_x.config(command=self.casting_details_table.xview)
        Scrollbar_y.config(command=self.casting_details_table.yview)

        # ---------------------Table Heading-----------------------------
        self.casting_details_table.heading('m_id',text='Movie Id')
        self.casting_details_table.heading('a_id',text='Act_id')
        self.casting_details_table.heading('role',text='Role')

        self.casting_details_table['show']  ='headings'

        # ----------------------Adjusting the Column Width-------------------
        self.casting_details_table.column('m_id',width=30)
        self.casting_details_table.column('a_id',width=150)
        self.casting_details_table.column('role',width=20)

        self.casting_details_table.pack(fill=BOTH,expand=1)
        self.casting_details_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()


    def add_data(self):
        ''' Adds new cast to the Movie Database '''
        if self.var_Act_id.get()=='' or self.var_mov_id.get() == '':
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
                my_cursor = connection.cursor()
                my_cursor.execute('INSERT INTO casting VALUES(%s,%s,%s)',(self.var_mov_id.get(),
                                                                                self.var_Act_id.get(),
                                                                                self.var_Act_Role.get(),
                                                                            ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('Success','Cast added sucessfully',parent=self.root)
            except Exception as e:
                messagebox.showwarning('Warning',f'Something went wrong !{e}',parent=self.root)

    def fetch_data(self):
        ''' Fetches the data present in the Cast Table '''
        try:
            connection = mysql.connector.connect(host = 'localhost',username ='root',password = '#10dssk01#',database = 'moviedb')
            my_cursor = connection.cursor()
            my_cursor.execute('SELECT * FROM casting')
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.casting_details_table.delete(*self.casting_details_table.get_children())
                for i in rows:
                    self.casting_details_table.insert('',END,values=i)
            connection.commit()
            connection.close()
        except Exception as e:
            messagebox.showerror('Error',e,parent = self.root)

    def get_cursor(self,event=''):
        ''' Helps in show the data in the table Present in GUI window''' 
        cursor_row = self.casting_details_table.focus()
        content = self.casting_details_table.item(cursor_row)
        row = content['values']
        self.var_mov_id.set(row[0])
        self.var_Act_id.set(row[1]),
        self.var_Act_Role.set(row[2])

if __name__=='__main__':
    root=Tk()
    obj = cast_win(root)
    root.mainloop()
    