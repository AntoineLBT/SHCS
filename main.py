#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sqlite3
from tkinter import *

def connect_db():
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor() 
    return connection, cursor

#definition of menubar button
def new():
    print("new")
def import_file():
    print("import")
def export_file():
    print("export")
def delete():
    print("delete")
def save():
    print("save")
def save_as():
    print("save_as")

def zoom():
    print("zoom")
def unzoom():
    print("dézoomer")
def search():
    print("search")

def documentation():
    print("doc")

#affichage des clients
def display_customer_array():
    #FrameArray.pack_forget()
    #FrameArray.grid_forget()
    connection, cursor = connect_db()
    for i in range(1, 10, 2):
        Label(FrameArray, text='|').grid(row=0, column=i)

    Label(FrameArray, text='N°client').grid(row=0, column=0)
    Label(FrameArray, text='Cagnotte').grid(row=0, column=2)
    Label(FrameArray, text='Nom').grid(row=0, column=4)
    Label(FrameArray, text='Prénom').grid(row=0, column=6)
    Label(FrameArray, text='Contact').grid(row=0, column=8)

    cursor.execute("SELECT *  FROM Customer")
    row = cursor.fetchall()
    i = 1
    for customer in row:
        j = 0
        k = 1
        for data in customer:
            Label(FrameArray, text=data).grid(row=i, column=j)
            Label(FrameArray, text='|').grid(row=i, column=k)
            j+=2
            k+=2
        i+=1
    connection.close()

#affichage des vêtements 
def display_clothe_array():
    connection, cursor = connect_db()
    for i in range(1, 11, 2):
        Label(root, text='|').grid(row=0, column=i)

    Label(FrameArray, text='N°vêtement').grid(row=0, column=0)
    Label(FrameArray, text='Couleur').grid(row=0, column=2)
    Label(FrameArray, text='Taille').grid(row=0, column=4)
    Label(FrameArray, text='Date').grid(row=0, column=6)
    Label(FrameArray, text='Type').grid(row=0, column=8)
    Label(FrameArray, text='Prix').grid(row=0, column=10)

    cursor.execute("SELECT *  FROM Clothe")
    row = cursor.fetchall()
    i = 1
    for customer in row:
        j = 0
        k = 1
        for data in customer:
            Label(root, text=data).grid(row=i, column=j)
            Label(root, text='|').grid(row=i, column=k)
            j+=2
            k+=2
        i+=1
    connection.close()

#Configuration menu
def config_menu():
    menubar = Menu(root)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label='Nouveau', command=new)
    menu1.add_command(label='Importer', command=import_file)
    menu1.add_command(label='Exporter', command=export_file)
    menu1.add_command(label='Supprimer', command=delete)
    menu1.add_command(label='Save', command=save)
    menu1.add_command(label='Save as', command=save_as)

    menu2 = Menu(menubar)
    menu2.add_command(label='Zoomer', command=zoom)
    menu2.add_command(label='Dézoomer', command=unzoom)
    menu2.add_command(label='Rechercher', command=search)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label='Mode d\'emploi', command=documentation)

    menubar.add_cascade(label='Fichier', menu= menu1)
    menubar.add_cascade(label='Outils', menu=menu2)
    menubar.add_cascade(label='Aide', menu=menu3)
    return menubar

#main
# Construction de la fenêtre principale
root = Tk()
root.title('SHCS')

# Création des frames

    # frame bouton à gauche
FrameButton = Frame(root)
FrameButton.pack(side=LEFT)
    # frame tableau à droite
FrameArray = Frame(root)
FrameArray.pack(side=RIGHT)

Button(FrameButton, text="Clothe", relief=GROOVE, command=display_clothe_array).grid(row=0, column=0)
Button(FrameButton, text='Customer', relief=GROOVE, command=display_customer_array).grid(row=1, column=0)

display_customer_array()
#display_clothe_array()

root.config(menu=config_menu())
root.mainloop()



