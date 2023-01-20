from tkinter import *
import time

root = Tk()
root.title("Horloge - Christopher CORNET")
root.geometry('550x400')
root.iconbitmap('temps.ico')
root.config(bg='#535386')

# Affiche l'heure
display_time = Label(root,font=('Helvetica',50,'bold'),bg='#7A7AC5',fg="#FFFF7F",anchor='center', width=5)
display_time.place(x=170, y=30)

# Indication format de l'heure
hourFormat = Label(root, text='Format: HH:MM:SS', fg='gray', bg='white', font=('Helvetica',10,'bold'), width=16)
hourFormat.place(x=10, y=200)

# Entrée de l'heure
hour = Entry(root, width=19, font=('Helvetica',10,'bold'), justify='center')
hour.place(x=10, y=240)

def afficher_heure():
    hour_tuple = (10, 20, 0)
    print(hour_tuple)
    while hour_tuple[2] < 60:
        hour_list = list(hour_tuple)
        hour_list[2] += 1
        hour_list[2]
        new_tuple = tuple(hour_list)
        print(new_tuple)
        time.sleep(1)

afficher_heure()

settingsButton = Button(root, bg='#7A7AC5', font=('Helvetica',12,'bold'), fg='#FFFF7F', text="Changer l'heure", command=afficher_heure)
settingsButton.place(x=10, y=150)

root.mainloop()