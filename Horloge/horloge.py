import time as t
from datetime import datetime

list_hours = []

def alarm(alarm_hour, alarm_minutes, alarm_seconds):
    if set_hours == 10: 
        print("Alarme déclenchée ! Il est:", alarm_hour, ":", alarm_minutes, ":", alarm_seconds)

morning_afternoon = "" # AM/PM

# Actualise l'heure chaque secondes
def afficher_heure(hours_input,minutes_input,seconds_input,morning_afternoon):
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
        if hours >= 12:
            morning_afternoon = "PM"
            if hours == 13:
                hours_print = 1
            elif hours == 14:
                hours_print = 2
            if hours == 15:
                hours_print = 3
            if hours == 16:
                hours_print = 4
            if hours == 17:
                hours_print = 5
            if hours == 18:
                hours_print = 6
            if hours == 19:
                hours_print = 7
            if hours == 20:
                hours_print = 8
            if hours == 21:
                hours_print = 9
            if hours == 22:
                hours_print = 10
            if hours == 23:
                hours_print = 11
        if hours == 12:
            morning_afternoon = "PM"
        if hours <= 12:
            morning_afternoon = "AM"
            if hours == 0:
                hours_print = 0
            elif hours == 1:
                hours_print = 1
            if hours == 2:
                hours_print = 2
            if hours == 3:
                hours_print = 3
            if hours == 4:
                hours_print = 4
            if hours == 5:
                hours_print = 5
            if hours == 6:
                hours_print = 6
            if hours == 7:
                hours_print = 7
            if hours == 8:
                hours_print = 8
            if hours == 9:
                hours_print = 9
            if hours == 10:
                hours_print = 10
        print(str(hours_print) + ":" + "{:02d}".format(minutes) + ":" + "{:02d}".format(seconds) + " " + morning_afternoon)
        seconds += 1
        t.sleep(1)

# Régler l'heure
def set_hours():
    print("Heure par défaut:")
    i = 0
    while True:
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")
        t.sleep(1)
        print(current_time)
        i += 1
        if i == 1:
            print("Voulez vous régler l'heure ? Y/N")
            user_settings = input()
            if user_settings == "Y":
                hours_input = input("Heures:")
                list_hours.append(hours_input)
                minutes_input = input("Minutes:")
                list_hours.append(minutes_input)
                seconds_input = input("Secondes:")
                list_hours.append(seconds_input)
                afficher_heure(hours_input,minutes_input,seconds_input,morning_afternoon) # Heure configurée
            elif user_settings == "N":
                print("Heure par défaut:")
                while True:
                    time_now = datetime.now()
                    current_time = time_now.strftime("%H:%M:%S")
                    print(current_time)
                    t.sleep(1)
        
set_hours()