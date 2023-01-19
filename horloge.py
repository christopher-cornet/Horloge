import time

# afficher une heure sous le format hh:mm:ss
# actualiser l'heure a chaque seconde (boucle while, tant que le programme est ouvert)
def refreshHour():
    while True:
        refresh_time = time.strftime("%H:%M:%S")
        time.sleep(1)
        print(refresh_time)

refreshHour()