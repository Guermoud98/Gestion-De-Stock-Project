#nom, prix, qte_stock, seuil_alerte, date_premiere_entree, date_derniere_sortie,image_produit,id_admin
from tkinter import *
from tkinter import *
from tkinter import ttk
from PIL import ImageTk as img
from tkinter import messagebox

# creating an instance of the Tk class from the tkinter module
window = Tk()
window.geometry("990x660")
window.title("gestion de stock")
bgImage = img.PhotoImage(file ="bg5.jpg")
bgLabel = Label(window, image = bgImage)
bgLabel.grid(row=0,column=0) 

# container of labels
frame = Frame(window)
frame.place(x=20,y=40)

heading = Label(frame, text ="Infor des produits", font= ("Microsoft Yahei UI Light",18,"bold"),fg ="black" )
heading.grid(row=0,column=0)

# nom du produit
nom_label = Label(frame, text="nom du produit", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
nom_label.grid(row=1,column=0, sticky="w",padx=10)

nom_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"))
nom_input.grid(row=2,column=0)

# prix
username_label = Label(frame, text="prix", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
username_label.grid(row=3,column=0, sticky="w",padx=10)

username_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"))
username_input.grid(row=4,column=0)

# qte_stock
qte_label = Label(frame, text="quantité en stock", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
qte_label.grid(row=5,column=0, sticky="w",padx=10)

qte_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"))
qte_input.grid(row=6,column=0)

# seuil alerte
seuil_label = Label(frame, text="seuil d'alerte", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
seuil_label.grid(row=7,column=0, sticky="w",padx=10)

seuil_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"))
seuil_input.grid(row=8,column=0)

# date_derniere_entree
date_derniere_entree_label = Label(frame, text="date de la dernière entrée", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
date_derniere_entree_label.grid(row=9,column=0, sticky="w",padx=10)

date_derniere_entree_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"))
date_derniere_entree_input.grid(row=10,column=0)

# date_derniere_sortie
date_derniere_sortie_label = Label(frame, text="date de la dernière sortie", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
date_derniere_sortie_label.grid(row=11,column=0, sticky="w",padx=10)

date_derniere_sortie_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"))
date_derniere_sortie_input.grid(row=12,column=0)

# id_admin
nom_admin_label = Label(frame, text="admin", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
nom_admin_label.grid(row=13,column=0, sticky="w",padx=10)

nom_admin_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"))
nom_admin_input.grid(row=14,column=0)

# add btn
login_btn = Button(frame,text="Ajouter",font= ("Open Sans",16,"bold") )
login_btn.grid(row=6,column=1)

# modify btn
login_btn = Button(frame,text="Modifier",font= ("Open Sans",16,"bold") )
login_btn.grid(row=8,column=1)

# delete btn
login_btn = Button(frame,text="Supprimer",font= ("Open Sans",16,"bold") )
login_btn.grid(row=10,column=1)




















# Run the application
window.mainloop()