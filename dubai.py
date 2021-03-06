from tkinter import *
from tkinter.tix import *
from PIL import ImageTk, Image
import dubai_flight
import HomePage
from booking1 import main

def dubaipage(home_root):
        home_root.destroy()
        root=Tk()

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        mainframe = Frame(root,width = screen_width,height = screen_height)
        mainframe.pack()
        swin = ScrolledWindow(mainframe, width=screen_width, height=screen_height)
        swin.pack()
        win = swin.window

        root.minsize(width=screen_width, height=screen_height)
        root.config(bg="white")
        #root.attributes("-fullscreen",True)

        frame_width = win.winfo_screenwidth()
        frame_height = 1600

        top=Frame(win,width=frame_width,height=60,bg="white")
        top.pack(side=TOP)

        f1=Frame(win,width=frame_width/2,height=frame_height-60,bg="white")
        f1.propagate(0)
        f1.pack(side=LEFT)


        f2=Frame(win,width=frame_width/2,height=frame_height-60,bg="white")
        f1.propagate(0)
        f2.pack(side=RIGHT)

        #-----------HOME BUTTON-----------------------------------------------
        b=Button(top,command=lambda:HomePage.frontpage(root))
        img=PhotoImage(file="res/home_login.png")
        b.config(image=img,width="60",height="50",bg="white",bd = 0)
        b.place(x=screen_width-80,y=10)
        
        lb=Label(top,text="DUBAI",font=("lucida calligraphy",40,"bold"),fg="#4EB1BA",bg="white")
        lb.place(x=530,y=0)
        lb=Label(top,text="Come Explore Your Dreams",font=("arial",15,"bold"),fg="blue",bg="white")
        lb.place(x=470,y=70)

        path="res/mal.jpg"

        photo=ImageTk.PhotoImage(Image.open(path))
        lb=Label(f1,image=photo)
        lb.place(x=70,y=40,width=510,height=250)

        l1=Label(f2,text="Durham Marriott Hotel",font=("arial",30,"bold"),fg="black",bg="white")
        l1.place(x=0,y=40)

        path1="res/star.png"

        photo1=ImageTk.PhotoImage(Image.open(path1))
        lb1=Label(f2,image=photo1,bg="white")
        lb1.place(x=0,y=80,width=200,height=50)

        l2=Label(f2,text="Rs.21000",font=("arial",20,"bold"),fg="blue",bg="white")
        l2.place(x=9,y=120)
        t1=Message(f2,text="Posh riverside lodging with chic rooms and a hip BBQ restaurant.",font=("arial",20),fg="black",bg="white",width = 400)
        t1.place(x=0,y=160)
        b1=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white",command=lambda:main(root,"Durham Marriott Hotel"))
        b1.place(x=9,y=240)
        ################


        path2="res/mal15.jpg"

        photo2=ImageTk.PhotoImage(Image.open(path2))
        lb2=Label(f1,image=photo2)
        lb2.place(x=70,y=320,width=510,height=250)

        l3=Label(f2,text="Emirates Grand Hotel",font=("arial",30,"bold"),fg="black",bg="white")
        l3.place(x=0,y=320)

        path3="res/star.png"

        photo3=ImageTk.PhotoImage(Image.open(path3))
        lb3=Label(f2,image=photo3,bg="white")
        lb3.place(x=0,y=360,width=200,height=50)

        l4=Label(f2,text="Rs.35000",font=("arial",20,"bold"),fg="blue",bg="white")
        l4.place(x=9,y=400)
        t1=Message(f2,text="Beautiful beaches with good view and exotic rooms best.",font=("arial",20),fg="black",bg="white",width = 400)
        t1.place(x=0,y=440)
        b1=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white",command=lambda:main(root,"Emirates Grand Hotel"))
        b1.place(x=9,y=520)

        ################

        path4="res/mal70.jpg"

        photo4=ImageTk.PhotoImage(Image.open(path4))
        lb4=Label(f1,image=photo4)
        lb4.place(x=70,y=600,width=510,height=250)

        l5=Label(f2,text="Fortune Hotel Deira",font=("arial",30,"bold"),fg="black",bg="white")
        l5.place(x=0,y=600)

        path5="res/star.png"

        photo5=ImageTk.PhotoImage(Image.open(path5))
        lb5=Label(f2,image=photo5,bg="white")
        lb5.place(x=0,y=640,width=200,height=50)

        l5=Label(f2,text="Rs.45000",font=("arial",20,"bold"),fg="blue",bg="white")
        l5.place(x=9,y=680)
        t2=Message(f2,text="Beautiful beaches with good view and exotic rooms best.",font=("arial",20),fg="black",bg="white",width = 400)
        t2.place(x=0,y=720)
        b2=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white")
        b2.place(x=9,y=800)

        ################

        path6="res/mal80.jpg"

        photo6=ImageTk.PhotoImage(Image.open(path6))
        lb6=Label(f1,image=photo6)
        lb6.place(x=70,y=880,width=510,height=250)

        l7=Label(f2,text="Burj Khalifa",font=("arial",30,"bold"),fg="black",bg="white")
        l7.place(x=0,y=880)

        path7="res/star.png"

        photo7=ImageTk.PhotoImage(Image.open(path7))
        lb7=Label(f2,image=photo5,bg="white")
        lb7.place(x=0,y=920,width=200,height=50)

        l8=Label(f2,text="Rs.40000",font=("arial",20,"bold"),fg="blue",bg="white")
        l8.place(x=9,y=960)
        t3=Message(f2,text="Natural view with good atmosphere and exotic rooms.",font=("arial",20),fg="black",bg="white",width = 400)
        t3.place(x=0,y=1000)
        b3=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white")
        b3.place(x=9,y=1080)

        ################

        path8="res/mal18.jpg"

        photo8=ImageTk.PhotoImage(Image.open(path8))
        lb8=Label(f1,image=photo8)
        lb8.place(x=70,y=1160,width=510,height=250)

        l9=Label(f2,text="Atlantis",font=("arial",30,"bold"),fg="black",bg="white")
        l9.place(x=0,y=1160)

        path9="res/star.png"

        photo9=ImageTk.PhotoImage(Image.open(path9))
        lb9=Label(f2,image=photo5,bg="white")
        lb9.place(x=0,y=1200,width=200,height=50)

        l10=Label(f2,text="Rs.55000",font=("arial",20,"bold"),fg="blue",bg="white")
        l10.place(x=9,y=1240)
        t4=Message(f2,text="Natural view with good atmosphere and exotic rooms.",font=("arial",20),fg="black",bg="white",width = 400)
        t4.place(x=0,y=1280)
        b4=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white")
        b4.place(x=9,y=1360)
        #--------NEXT-------------------
        b5=Button(f2,text="NEXT",padx=20,pady=10,bd=5,bg="red",fg="white",command = lambda:dubai_flight.dubai_flights(root))
        b5.place(x=550,y=1420)
        root.mainloop()

