from tkinter import *
from PIL import ImageTk as img


def login_page():
    signup_window.destroy()
    import login

signup_window = Tk()

signup_window.geometry("990x660")
signup_window.title("gestion de stock")
bgImage = img.PhotoImage(file ="bg3.jpg")
bgLabel = Label(signup_window, image = bgImage)
bgLabel.grid(row=0,column=0)

# container of labels
frame = Frame(signup_window)
frame.place(x=600,y=120)

heading = Label(frame, text ="CREATE AN ACCOUNT", font= ("Microsoft Yahei UI Light",18,"bold"),fg ="black" )
heading.grid(row=0,column=0)

# username
username_label = Label(frame, text="username", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
username_label.grid(row=1,column=0, sticky="w",padx=10)

username_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"))
username_input.grid(row=2,column=0)

# password
password_label = Label(frame, text="password", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
password_label.grid(row=3,column=0, sticky="w",padx=10)

password_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"), show="*")
password_input.grid(row=4,column=0)

# Confirmpassword
pwd_confirm_label = Label(frame, text="confirm password", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
pwd_confirm_label .grid(row=5,column=0, sticky="w",padx=10)

pwd_confirm_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"), show="*")
pwd_confirm_input.grid(row=6,column=0,pady=10)

# signup button
signup_btn = Button(frame,text="Signup",font= ("Open Sans",16,"bold"))
signup_btn.grid(row=7,column=0)

#alreadyAccount
alreadyaccount = Label(frame, text="You have already an account?",font= ("Open Sans",9,"bold"))
alreadyaccount.grid(row=8,column=0,sticky="w")

#loginButton
login_btn = Button(frame,text="Log in",font= ("Open Sans",9,"bold underline"), bg="white",fg="blue",cursor="hand2",activeforeground="blue", command = login_page)
login_btn.place(x=180,y=290)












signup_window.mainloop()
