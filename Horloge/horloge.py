import time as t
from datetime import datetime

list_hours = []
tuple_hours = tuple(list_hours)

# Actualise l'heure chaque secondes
def afficher_heure(hours_input,minutes_input,seconds_input):
    hours = int(hours_input)
    minutes = int(minutes_input)
    seconds = int(seconds_input)
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

# Régler l'heure
def set_hours():
    print("Heure par défaut:")
    i = 0
    while True:
        c = datetime.now()
        current_time = c.strftime("%H:%M:%S")
        t.sleep(1)
        print(current_time)
        i += 1
        if i == 5:
            print("Voulez vous régler l'heure ? y/n")
            user_settings = input()
            if user_settings == "y":
                hours_input = input("Heures:")
                list_hours.append(hours_input)
                minutes_input = input("Minutes:")
                list_hours.append(minutes_input)
                seconds_input = input("Secondes:")
                list_hours.append(seconds_input)
                afficher_heure(hours_input,minutes_input,seconds_input) # Heure configurée
            elif user_settings == "n":
                print("Heure par défaut:")
                while True:
                    c = datetime.now()
                    current_time = c.strftime("%H:%M:%S")
                    print(current_time)
                    t.sleep(1)
        
set_hours()