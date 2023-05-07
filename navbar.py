from tkinter import *
from tkinter import ttk
from PIL import ImageTk as img
from tkinter import messagebox


def open_add_product():
    messagebox.showinfo("Ajouter Produit", "Button Ajouter Produit clicked!")

def open_delete_product():
    messagebox.showinfo("Supprimer Produit", "Button Supprimer Produit clicked!")

def open_display_products():
    messagebox.showinfo("Afficher Produits", "Button Afficher Produits clicked!")


# creating an instance of the Tk class from the tkinter module
navbar_window = Tk()
navbar_window.geometry("990x660")
navbar_window.title("gestion de stock")



navbar_window.mainloop()
