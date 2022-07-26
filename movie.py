from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
from Movies import Mov_win
from actors import Act_win
from director import Dir_win
from production import Prodn_win
from rev_stars import Rev_win
from About_Us import About_Us
from casting import cast_win

class Movie:
    dt_string = ''
    def __init__(self,root):
        '''initializes all the necessary widgets onto the Tk'''
        self.root=root
        # self.root.attributes('-fullscreen', True)
        self.root.title('Movie Database')
        self.root.geometry('1450x800')
        self.root.wm_iconbitmap("Main_Images/movies.ico")

                        # Image_1 : logo
        img_1=Image.open("Main_Images/moviz.png")
        img_1= img_1.resize((230,90),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img_1)

        limg1=Label(self.root,image=self.img1,bg='cyan',bd=3,relief=RIDGE)
        limg1.place(x=0,y=0,width=200,height=150)

        img_mov=Image.open("Main_Images/movie_icon.jpg")
        img_mov= img_mov.resize((80,80),Image.ANTIALIAS)
        self.img_movie=ImageTk.PhotoImage(img_mov)

        main_label = Label(self.root,text='★▄︻デ🅶🅳🅿 🅼🅾🆅🅸🅴🆂══━一★',font=('',40),
        fg='Black',bg='light green').place(x=205,y=0,width=1200,height=100)
        main_sub_label = Label(self.root,image=self.img_movie,bg='crimson').place(x=300,y=0,width=100,height=100)

        Log_out_button = Button(self.root,text= 'Log Out',width=15,command=self.log_out,font = 'algerian 12 bold',bg='black',fg= 'gold',cursor='hand2')
        Log_out_button.place(x = 1180, y = 65)

                        # Label : Tiltle
        lbl_title= Label(self.root,text='Movie Database',font='Algerian 30 bold',fg='gold',bg='black',relief=RIDGE)
        lbl_title.place(x=205,y=100,width=1200,height=50) 

                        # Main Frame
        main_frame= Frame(self.root,bd=3,relief=RIDGE,bg='black')
        main_frame.place(x=0,y=150,width=1360,height=610)

                            # menu
        lbl_menu= Label(main_frame,text='Menu',font='Times 22 bold',fg='gold',bg='black',relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=200,height=40)

                        # Button Frame
        button_frame= Frame(main_frame,bd=3,relief=RIDGE)
        button_frame.place(x=0,y=35,width=200,height=250)

        movie_button = Button(button_frame,text= 'MOVIES',command=self.mov_details,width=19,font='algerian 12 bold',bg='black',fg= 'gold',cursor='hand2')
        # movie_button.grid(row=0,column=0)
        movie_button.place(x=0,y=0,width=195,height=32)

        actors_button = Button(button_frame,text= 'ACTORS',command=self.actor_details,width=19,font = 'algerian 12 bold',bg='black',fg= 'gold',cursor='hand2')
        # actors_button.grid(row=1,column=0)
        actors_button.place(x=0,y=32,width=195,height=32)

        directors_button = Button(button_frame,text= 'DIRECTORS',command=self.director_details,width=19,font = 'algerian 12 bold',bg='black',fg= 'gold',cursor='hand2')
        # directors_button.grid(row=2,column=0)
        directors_button.place(x=0,y=64,width=195,height=32)

        mov_prodn_button = Button(button_frame,text= 'PRODUCTION HOUSE',command=self.production_House_details,width=19,font = 'algerian 12 bold',bg='black',fg= 'gold',cursor='hand2')
        # mov_prodn_button.grid(row=3,column=0)
        mov_prodn_button.place(x=0,y=96,width=195,height=32)

        ratings_button = Button(button_frame,text= 'RATINGS',width=19,command=self.review_details,font = 'algerian 12 bold',bg='black',fg= 'gold',cursor='hand2')
        # ratings_button.grid(row=4,column=0)
        ratings_button.place(x=0,y=128,width=195,height=32)

        cast_button = Button(button_frame,text= 'CAST',width=19,command=self.Casting_details,font = 'algerian 12 bold',bg='black',fg= 'gold',cursor='hand2')
        # cast_button.grid(row=5,column=0)
        cast_button.place(x=0,y=160,width=195,height=32)

                                    # Date Label
        self.cdate = Label(button_frame,text=self.dt_string,width=18,font='Helvetica  13 bold',bg='white',fg= 'black',bd=6)
        # self.cdate.grid(row=6,column=0,sticky=W)
        self.cdate.place(x=0,y=200,width=195,height=40)
        self.clock()        

                            # Images_2
        img_mov=Image.open("Main_Images/mainmoviz.jpg")
        img_mov= img_mov.resize((1180,600),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(img_mov)

        limg2=Label(main_frame,image=self.img2,bd=0,relief=RIDGE)
        limg2.place(x=204,y=0,width=1180,height=600)

        #---------------------------About Us Button----------------------------------
        about_us = Button(main_frame,text= 'About Us',width=19,command=self.about_us,font = 'algerian 12 bold',bg='Green',fg= 'White',cursor='hand2')
        about_us.place(x = 1130,y = 530)

                            #Images_3
        img_3=Image.open("Main_Images/img3.jpg")
        img_3= img_3.resize((200,140),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(img_3)                    
        limg3=Label(main_frame,image=self.img3,bg='black',bd=2,relief=RIDGE)
        limg3.place(x=0,y=276,width=200,height=150)

                            # Images_4
        img_4=Image.open("Main_Images/img4.jpg")
        img_4= img_4.resize((200,180),Image.ANTIALIAS)
        self.img4=ImageTk.PhotoImage(img_4)
        limg4=Label(main_frame,image=self.img4,bg='black',bd=2,relief=RIDGE)
        limg4.place(x=0,y=426,width=200,height=178)

    def clock(self):
        '''creates a clock on the window'''
        now = datetime.now()    # datetime object containing current date and time
        self.dt_string = now.strftime("%d/%h/%Y\n%I:%M:%S %p")
        self.cdate.config(text=self.dt_string)
        self.cdate.after(1000,self.clock)
        
    def mov_details(self):
        '''This acts like a bridge which connects this window to the movie window'''
        self.new_win1 = Toplevel(self.root)
        self.app1 = Mov_win(self.new_win1)

    def actor_details(self):
        '''This acts like a bridge which connects this window to the actor window'''
        self.new_win2 = Toplevel(self.root)
        self.app2 = Act_win(self.new_win2)

    def director_details(self):
        '''This acts like a bridge which connects this window to the director window'''
        self.new_win3 = Toplevel(self.root)
        self.app3 = Dir_win(self.new_win3)

    def review_details(self):
        '''This acts like a bridge which connects this window to the rating window'''
        self.new_winx = Toplevel(self.root)
        self.app4 = Rev_win(self.new_winx)    

    def production_House_details(self):
        '''This acts like a bridge which connects this window to the production company window'''
        self.new_win4 = Toplevel(self.root)
        self.app4 = Prodn_win(self.new_win4)

    def Casting_details(self):
        '''This acts like a bridge which connects this window to the Casting window'''
        self.new_win5 = Toplevel(self.root)
        self.app5 = cast_win(self.new_win5)    

    def log_out(self):
        '''Destroys the main window(current) and redirects the user to the login window'''
        self.root.destroy()

    def about_us(self):
        '''Everything About Developers'''
        self.top = Toplevel(self.root)
        self.top.geometry("800x500+250+200")
        self.top.title("toplevel")
        self.top.resizable(False,False)
        self.About_Us_Frame =LabelFrame(self.top,bd = 2,relief=RIDGE,text='View Details',padx=2,font='times 14 bold italic')
        self.About_Us_Frame.place(x=10,y=0,width=780,height=495)
        self.ent_aboutActor = Text(self.About_Us_Frame,width=22,font="times 12")
        self.ent_aboutActor.place(x=30,y=30,width=700,height=255)
        self.ent_aboutActor.insert(INSERT,About_Us)
        
        Thank_You=Label(self.top,text = 'Thank You\nFor Using our Application.........!',font='Algerian 22 bold',fg="crimson",bd=0,relief=RIDGE)
        Thank_You.place(x=50,y=340,width=500,height=58)
        
        img_namaste=Image.open("Main_Images/namaste.png")
        img_namaste= img_namaste.resize((80,80),Image.ANTIALIAS)
        self.img_namaste=ImageTk.PhotoImage(img_namaste)
        limg2=Label(self.top,image=self.img_namaste,bd=0,relief=RIDGE)
        limg2.place(x=550,y=350,width=120,height=80)

if __name__=='__main__':
    root=Tk()
    obj = Movie(root)
    root.mainloop()
