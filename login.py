from tkinter import *
from PIL import ImageTk as img



def signup_page():
    login_window.destroy()
    import signup

# creating an instance of the Tk class from the tkinter module
login_window = Tk()
login_window.geometry("990x660")
login_window.title("gestion de stock")
bgImage = img.PhotoImage(file ="bg3.jpg")
bgLabel = Label(login_window, image = bgImage)
bgLabel.grid(row=0,column=0)

# container of labels
frame = Frame(login_window)
frame.place(x=600,y=120)

heading = Label(frame, text ="USER LOGIN", font= ("Microsoft Yahei UI Light",18,"bold"),fg ="black" )
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

#alreadyAccount
alreadyaccount = Label(frame, text="Don't have an account?",font= ("Open Sans",9,"bold"))
alreadyaccount.grid(row=5,column=0,sticky="w")

#loginButton
login_btn = Button(frame,text="Sign Up",font= ("Open Sans",9,"bold underline"), bg="white",fg="blue",cursor="hand2",activeforeground="blue", command = signup_page)
login_btn.place(x=30,y=150)

    
# Run the application
login_window.mainloop()



#u = login()