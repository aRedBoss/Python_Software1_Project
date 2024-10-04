import taso_funktio
import funktiot
import time

name = input("Hei, mikä sinun nimesi on? ")
funktiot.default_settings(name)

high_score = 1

while True:
    taso_funktio.level_one(name)
    taso_funktio.level_two(name)
    taso_funktio.level_three(name)
    taso_funktio.level_four(name)
    taso_funktio.level_five(name)
    points = funktiot.get_points(name)
    print(f"Onneksi olkoon! Pääsit pelin läpi {points} pisteellä!")
    time.sleep(1)
    if points > high_score[0]:
        high_score[0] = points
        print(f"Uusi ennätys: {high_score} pistettä!")
        time.sleep(2)
    print (f"Piste ennätys: {high_score} pistettä.")
    time.sleep(1)
    play_again = input("Haluatko pelata uudelleen? (y/n): ").lower()
    if play_again == "y":
        continue
    elif play_again == "n":
        print("Ensi kertaan.")
        time.sleep(1)
        break
    else:
        break