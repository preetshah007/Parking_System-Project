import subprocess
import tkinter as tk
from datetime import datetime
root=tk.Tk()
root.title("Main Dashboard")
root.state('zoomed')
def signout():
    root.destroy()
def fourwheeler():
    subprocess.Popen(["python", "4wheelerdashboard.py"], shell=True)
def twowheeler():
    subprocess.Popen(["python", "2wheelerdashboard.py"], shell=True)
def dail():
    subprocess.Popen(["notepad", "daily.txt"], shell=True)
icon = tk.PhotoImage(file=r"C:\Users\Preet Shah\OneDrive\Desktop\PYTHON PROJECT\icon.png")
small_icon = icon.subsample(5, 5)
icon1=tk.PhotoImage(file=r"C:\Users\Preet Shah\OneDrive\Desktop\PYTHON PROJECT\icon2.png")
small_icon1 = icon1.subsample(5, 5)
bg_image =tk.PhotoImage(file=r"C:\Users\Preet Shah\OneDrive\Desktop\PYTHON PROJECT\bg.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
fw=tk.Button(root,image=small_icon1, text="4 Wheeler Parking", font=("Arial Black",10),bg="white",width=220, height=50, command=fourwheeler,compound="left")
fw.place(x= 660, y=330)
tw=tk.Button(root,image=small_icon, text="2 Wheeler Parking ",font=("Arial Black",10),bg="white", width=220, height=50, command=twowheeler,compound="left").place(x= 660, y=400)
so=tk.Button(root, text="Sign Out", width=17, height=1,fg="white",bg="red",font=("Arial Black",15), command=signout).place(x= 1250, y=50)
da=tk.Button(root, text="Daily Record (All)", width=15, height=1,font=("Arial Black",10), command=dail).place(x= 700, y=500)
tk.Label(root,text="Select Your Vehicle Type",font=("Bebas Neue", 22, "bold"),fg="black",bg="white").place(x=600, y=280)
root.mainloop()