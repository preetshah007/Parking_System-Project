import tkinter as tk
import subprocess
from datetime import datetime
root=tk.Tk()
root.title("Bike Parking Dashboard")
root.state('zoomed')
def backclick():
       subprocess.Popen(["python", "afterlogin.py"], shell=True)
def dailyrecord():
       subprocess.Popen(["notepad", "daily(2wheeler).txt"], shell=True)
def click(button):
        def printi():
              bill.destroy()
        global hour
        global minute
        if button.cget("bg") == "red":
            bill=tk.Toplevel(root)
            bill.state('zoomed')
            bill.title("Billing")
            bg_image =tk.PhotoImage(file=r"C:\Users\Preet Shah\OneDrive\Desktop\PYTHON PROJECT\bg.png")
            bg_label = tk.Label(bill, image=bg_image)
            bg_label.place(relwidth=1, relheight=1)
            t1=datetime.now()
            h1,m1=t1.hour, t1.minute
            time1=(f"{h1}:{m1}")
            with open("daily(2wheeler).txt", "r") as file:
                lines = file.readlines()
            with open("daily(2wheeler).txt", "w") as file:
                for line in lines:
                        if line.startswith(button.cget("text")) and line.count('-') == 2 and line.endswith("\n"):
                                file.write(line.strip() + f" - {time1}\n")
                        else:
                                file.write(line)
            with open("daily.txt", "r") as file:
                lines = file.readlines()
            with open("daily.txt", "w") as file:
                for line in lines:
                        if line.startswith(button.cget("text")) and line.count('-') == 2 and line.endswith("\n"):
                                file.write(line.strip() + f" - {time1}\n")
                        else:
                                file.write(line)
            th=h1-hour
            tm=m1-minute
            tk.Label(bill, text=f'Time till Parked: {h1}:{m1}', font="15").place(x=650, y=200)
            tk.Label(bill, text=f'Total Time Parked: {th}:{tm}', font="15").place(x=645, y=250)
            if(th<=1):
                 price=20
            if(th>1 and th<=5):
                 price=th*50
            if(th>5 and th<=10):
                 price=th*100
            if(th>10):
                 price=th*120
            tk.Label(bill, text=f'Total Bill: {price}', font="15").place(x=690, y=300)
            tk.Label(bill, text=f'Grand Total (With GST): {price+price*0.18}' , font="15").place(x=625, y=350)
            tk.Button(bill, text="Print", width=9, height=2, command=printi).place(x=720, y=445)
            button.config(bg='SystemButtonFace')
        elif button.cget("bg") == "SystemButtonFace":
                regi=tk.Toplevel(root)
                regi.state('zoomed')
                
                t=datetime.now()
                h,m=t.hour,t.minute
                hour=h
                minute=m
                time=(f"{h}:{m}")
                bg_image =tk.PhotoImage(file=r"C:\Users\Preet Shah\OneDrive\Desktop\PYTHON PROJECT\bg.png")
                bg_label = tk.Label(regi, image=bg_image)
                bg_label.place(relwidth=1, relheight=1)
                regi.title("Vehicle Registration")
                tk.Label(regi, text="Enter Vehicle Number: ",font=("Arial Black",11)).place(x=650, y=250)
                regi_e=tk.Entry(regi)
                regi_e.insert(0, "AB:02:CD:3456")
                regi_e.place(x=850, y=255)
                def saving():
                        regie=regi_e.get()
                        tosave=(f"{button.cget('text')} - {regie} - {time}\n")
                        with open("daily(2wheeler).txt", "a") as file:
                                file.write(tosave)
                                file.flush()
                        with open("daily.txt", "a") as file1:
                                file1.write(tosave)
                                file1.flush()
                        regi.destroy()
                        button.config(bg="red")
                save=tk.Button(regi, text="Save and Print Token",font=("Arial Black",10), command=saving, width=18, height=2,)
                save.place(x=694, y=400)
                save.config(bg="red")
                tk.Label(regi, text=f"Vehicle Parking Starts at: {h}:{m}",font=("calibri",10)).place(x=675, y=300)
                tk.Label(regi, text=f"Vehicle Parked at: {button.cget('text')}",font=("calibri",10)).place(x=700, y=350)
                button.config(bg='red')
bg_image =tk.PhotoImage(file=r"C:\Users\Preet Shah\OneDrive\Desktop\PYTHON PROJECT\bg.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
icon = tk.PhotoImage(file=r"C:\Users\Preet Shah\OneDrive\Desktop\PYTHON PROJECT\icon1.png")
small_icon = icon.subsample(10, 10)
tk.Label(root, text='Bike Parking Allotment', font=("Bebas Neue", 22, "bold")).place(x=610, y=170)
b1=tk.Button(root,text="E1",width=7,height=3,command=lambda:click(b1))
b1.place(x=625,y=250)
b2=tk.Button(root,text="E2",width=7,height=3,command=lambda:click(b2))
b2.place(x=700,y=250)
b3=tk.Button(root,text="E3",width=7,height=3,command=lambda:click(b3))
b3.place(x=775,y=250)
b4=tk.Button(root,text="E4",width=7,height=3,command=lambda:click(b4))
b4.place(x=850,y=250)
b5=tk.Button(root,text="F1",width=7,height=3,command=lambda:click(b5))
b5.place(x=625,y=320)
b6=tk.Button(root,text="F2",width=7,height=3,command=lambda:click(b6))
b6.place(x=700,y=320)
b7=tk.Button(root,text="F3",width=7,height=3,command=lambda:click(b7))
b7.place(x=775,y=320)
b8=tk.Button(root,text="F4",width=7,height=3,command=lambda:click(b8))
b8.place(x=850,y=320)
b9=tk.Button(root,text="G1",width=7,height=3,command=lambda:click(b9))
b9.place(x=625,y=390)
b10=tk.Button(root,text="G2",width=7,height=3,command=lambda:click(b10))
b10.place(x=700,y=390)
b11=tk.Button(root,text="G3",width=7,height=3,command=lambda:click(b11))
b11.place(x=775,y=390)
b12=tk.Button(root,text="G4",width=7,height=3,command=lambda:click(b12))
b12.place(x=850,y=390)
b13=tk.Button(root,text="H1",width=7,height=3,command=lambda:click(b13))
b13.place(x=625,y=460)
b14=tk.Button(root,text="H2",width=7,height=3,command=lambda:click(b14))
b14.place(x=700,y=460)
b15=tk.Button(root,text="H3",width=7,height=3,command=lambda:click(b15))
b15.place(x=775,y=460)
b16=tk.Button(root,text="H4",width=7,height=3,command=lambda:click(b16))
b16.place(x=850,y=460)
back=tk.Button(root,image=small_icon, text="Main Dashboard", font=("Arial Black",10),width=162, height=45,bg="yellow", command=backclick,compound="left").place(x=550, y=550)
daily4wheeler=tk.Button(root, text="Daily Records (2 Wheelers)", font=("Arial Black",10),width=22, height=2,bg="lightblue", command=dailyrecord).place(x=775, y=550)
root.mainloop()