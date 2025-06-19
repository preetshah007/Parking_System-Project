import tkinter as tk
import tkinter.messagebox 
root=tk.Tk()
root.state('zoomed')
root.title('New User Regisration')
def submit():
    c=0
    c1=0
    c2=0
    n=[]
    with open("userinfo.txt", "r") as file:
        for i in file:
            i=i.strip()
            p=i.split(" - ")
            n.append(p[0])
    usern=user.get()
    passwo=passw.get()
    cpass=passw2.get()
    if usern in n:
        tkinter.messagebox.showinfo("Error", "User Already Exists")
        root.destroy()
        return
    for i in passwo:
        if ord(i)>=65 and ord(i)<=90:
            c+=1
        if i in "!@#$%^&*":
            c1+=1
        if ord(i)>=49 and ord(i)<=57:
            c2 += 1
    if len(passwo)>=8 and c>=1 and c1>=1 and c2>=1 and len(usern)!=0:
        if passwo==cpass:
            with open("userinfo.txt", "a") as file:
                tosave=f"{usern} - {passwo}"
                file.write("\n" + tosave)
            tkinter.messagebox.showinfo("New User", "New User Registration Complete")
            root.destroy()
        else:
            tkinter.messagebox.showinfo("Error", "Passwords not Matching")
    else:
        tkinter.messagebox.showinfo("Error", "Password not Strong and/or Username not Entered")
bg_image =tk.PhotoImage(file=r"C:\Users\Preet Shah\OneDrive\Desktop\PYTHON PROJECT\bg.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
tk.Label(root, text="Enter Username",font=("monospace",15,"bold")).place(x= 575, y=275)
user=tk.Entry(root)
user.place(x=760, y=280)
tk.Label(root, text="Enter Password", font=("monospace",15,"bold")).place(x= 575, y=350)
passw=tk.Entry(root, show='*')
passw.place(x=760, y=355)
tk.Label(root, text="Confirm Password",font=("monospace",15,"bold")).place(x= 575, y=425)
passw2=tk.Entry(root, show='*')
passw2.place(x=760, y=430)
sub=tk.Button(root, text="Create New User", width=15, height=1, bg='lightblue',font=("Arial Black",10,"bold"), command=submit)
sub.place(x=690, y=485)
tk.Label(root,text="Create New Account",font=("Bebas Neue", 22, "bold"),fg="black",).place(x=620, y=200)
root.mainloop()