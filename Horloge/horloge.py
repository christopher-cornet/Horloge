from tkinter import *
import time as t

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
    hours = 10
    minutes = 30
    seconds = 0
    while True:
        if seconds == 60:
            seconds = 0
            if seconds == 0:
                minutes += 1
        if minutes == 60:
            minutes = 0
            if minutes == 0:
                hours += 1
        if hours == 24:
            hours = 0
        print("{:02d}".format(hours) + ":" + "{:02d}".format(minutes) + ":" + "{:02d}".format(seconds))
        seconds += 1
        t.sleep(1)

afficher_heure()

settingsButton = Button(root, bg='#7A7AC5', font=('Helvetica',12,'bold'), fg='#FFFF7F', text="Changer l'heure", command=afficher_heure)
settingsButton.place(x=10, y=150)

root.mainloop()