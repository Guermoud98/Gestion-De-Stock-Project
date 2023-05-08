from tkinter import *
from tkinter import ttk
from PIL import ImageTk as img
from tkinter import messagebox
from connexion import connexion 
from admin import admin
from produit import produit
from produitDAO import produitDAO
from login_interface import logged_in_admin
c = produitDAO()
id_admin = logged_in_admin
# fct ajouter 
def ajouter():
    if nom_input.get()=='' or prix_input.get()=='' or qte_input.get() =='' or seuil_input.get()=='' or date_derniere_entree_input.get()=='' or date_derniere_sortie_input.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    nom = nom_input.get()
    prix = prix_input.get()
    qte_stock = qte_input.get()
    seuil_alerte = seuil_input.get()
    date_premiere_entree = date_derniere_entree_input.get()
    date_derniere_sortie = date_derniere_sortie_input.get()
    #image_produit = ""  # Add logic to get the image path
    
    
    # Add the product to the treeview self self, nom, prix, qte_stock, seuil_alerte, date_derniere_entree, date_derniere_sortie, admin_id
    tree.insert("", END, text="", values=(nom, prix, qte_stock, seuil_alerte, date_premiere_entree, date_derniere_sortie,id_admin))
    # Store the inputs in the database table
    pro = produit(nom_input.get(), prix_input.get(), qte_input.get(), seuil_input.get(),date_derniere_entree_input.get(), date_derniere_sortie_input.get(),id_admin)
    c.ajouterProduit(pro)



# fct supprimer
def supprimer():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'No product selected.')
        return
    elif(logged_in_admin != selected_item[id_admin]):
        tree.delete(selected_item)
        pro = produit(nom_input.get(), prix_input.get(), qte_input.get(), seuil_input.get(),date_derniere_entree_input.get(), date_derniere_sortie_input.get(),id_admin)
        c.supprimerProduit(pro)
    else:
        messagebox.showerror('Vous n etes pas le propriétaire de ce produit')
# afficher fct
def afficher():
    try:
        # Clear the treeview
        tree.delete(*tree.get_children())
        
        # Retrieve all products from the database
        produits = c.afficherProduits()
        
        # Insert each product into the treeview
        for produit in produits:
           nom = produit[1]
           prix = produit[2]
           qte_stock = produit[3]
           seuil_alerte = produit[4]
           date_premiere_entree = produit[5]
           date_derniere_sortie = produit[6]
           id_admin = produit[7]
           tree.insert("", END, values=(nom, prix, qte_stock, seuil_alerte, date_premiere_entree, date_derniere_sortie, id_admin))
    except Exception as e:
        print(f"An error occurred: {e}")

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
prix_label = Label(frame, text="prix", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
prix_label.grid(row=3,column=0, sticky="w",padx=10)

prix_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"))
prix_input.grid(row=4,column=0)

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
"""
# id_admin
nom_admin_label = Label(frame, text="admin", font= ("Microsoft Yahei UI Light",10,"bold"),pady=10)
nom_admin_label.grid(row=13,column=0, sticky="w",padx=10)

nom_admin_input = Entry(frame,width=30,font= ("Microsoft Yahei UI Light",10,"bold"))
nom_admin_input.grid(row=14,column=0)
"""
# add btn
ajouter_btn = Button(frame,text="Ajouter",font= ("Open Sans",16,"bold"), command= ajouter )
ajouter_btn.grid(row=6,column=1)

# modify btn
modifier_btn = Button(frame,text="Modifier",font= ("Open Sans",16,"bold") )
modifier_btn.grid(row=8,column=1)

# delete btn
delete_btn = Button(frame,text="Supprimer",font= ("Open Sans",16,"bold"),command = supprimer)
delete_btn.grid(row=10,column=1)

# Afficher btn
afficher_btn = Button(frame,text="Afficer",font= ("Open Sans",16,"bold"),command = afficher)
afficher_btn.grid(row=11,column=1)

# Create a treeview widget:
tree = ttk.Treeview(frame)
tree["columns"] = ("nom", "prix", "qte_stock", "seuil_alerte", "date_premiere_entree", "date_derniere_sortie",  "id_admin")

# Define the columns and their headings
tree.column("#0", width=0, stretch=NO)
tree.column("nom", width=100)
tree.column("prix", width=100)
tree.column("qte_stock", width=100)
tree.column("seuil_alerte", width=100)
tree.column("date_premiere_entree", width=150)
tree.column("date_derniere_sortie", width=150)
#tree.column("image_produit", width=100)
tree.column("id_admin", width=100)

tree.heading("#0", text="", anchor=W)
tree.heading("nom", text="Nom du produit", anchor=W)
tree.heading("prix", text="Prix", anchor=W)
tree.heading("qte_stock", text="Quantité en stock", anchor=W)
tree.heading("seuil_alerte", text="Seuil d'alerte", anchor=W)
tree.heading("date_premiere_entree", text="Date première entrée", anchor=W)
tree.heading("date_derniere_sortie", text="Date dernière sortie", anchor=W)
#tree.heading("image_produit", text="Image du produit", anchor=W)
tree.heading("id_admin", text="Admin", anchor=W)

tree.grid(row=0, column=2, rowspan=15, columnspan=2)



















# Run the application
window.mainloop()