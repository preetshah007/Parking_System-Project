import tkinter as tk
import subprocess
import tkinter.messagebox 
root=tk.Tk()
root.state('zoomed')
root.title("Welcome- Login")
def newu():
    subprocess.Popen(["python", "newuser.py"], shell=True)
def submit():
    n=[]
    m=[]
    passwo = passw.get()
    usern = user.get()
    with open("userinfo.txt", "r") as file:
        for i in file:
            i=i.strip()
            p=i.split(" - ")
            if len(p)==2:
                n.append(p[0])
                m.append(p[1])
    if not usern or not passwo:
        tkinter.messagebox.showinfo("Error", "Username and Password cannot be Empty")
        return
    if usern in n:
        index=n.index(usern)
        if passwo==m[index]:
            subprocess.Popen(["python", "afterlogin.py"], shell=True)
            return
        else:
            tkinter.messagebox.showinfo("Error", "Wrong Password")
            return
    else:
        tkinter.messagebox.showinfo("Error", "User Doesn't Exist")
def forg():
    tkinter.messagebox.showinfo("Oh No!", "Check for User Info File and Dont tell anyone")
bg_image =tk.PhotoImage(file=r"C:\Users\Preet Shah\OneDrive\Desktop\PYTHON PROJECT\bg.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
tk.Label(root,text="Welcome User",font=("Bebas Neue", 22, "bold"),fg="black",bg="white").place(x=670, y=190)
new=tk.Button(root, text="Create one",bg="white", command=newu)
new.place(x=800, y=480)
tk.Label(root, text="Username", bg="white", font=("monospace",15,"bold")).place(x= 630, y=275)
user=tk.Entry(root)
user.place(x=750, y=280)
tk.Label(root, text="Password", font=("monospace",15,"bold")).place(x= 630, y=325)
passw=tk.Entry(root, show='*')
passw.place(x=750, y=330)
forg=tk.Button(root, text="Forgot Password?", bg='white',fg="blue",font=("Arial",10),width=15, height=1, command=forg)
forg.place(x= 700, y=370)
sub=tk.Button(root, text="Login", width=20, height=1, bg='lightblue',font=("Arial Black",10), command=submit)
sub.place(x=660, y=410)
tk.Label(root, text="Don,t have account", fg="black", font=("arial",12)).place(x= 650, y=480)
root.mainloop()