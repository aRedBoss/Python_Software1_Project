import funktiot
import random
import time
import os


def level_one(name):
    funktiot.add_player(name)
    while True:
        current_location = funktiot.get_location(name)
        if current_location is None:
            print("Virhe: Nykyistä sijaintia ei voitu hakea. Tarkista pelaajatietosi.")
            return

        print("Taso 1")
        country_code = input(
            f"Olet tällä hetkellä sijainnissa {current_location[1]}. Minkä maan haluaisit tutkia seuraavaksi? Syötä maan koodi (esim. US, FI): ")
        airports = funktiot.get_airport_list(country_code)
        if len(airports) == 0:
            print("Yritä uudelleen!")
            continue
        for airport in airports:
            print(f"{airport[0]}: {airport[1]}")
        while True:
            destination = input("Valmiina nousuun? Syötä määränpääsi lentokentän ID: ")
            if funktiot.check_airport_availability(destination, country_code) == False:
                print("Yritä uudelleen!")
                continue
            break
        time.sleep(1)
        funktiot.airplane_shape()
        print("Sää on selkeä! Nousu sujuu helposti.")
        time.sleep(3)
        funktiot.clear_line()
        print("Nousu alkaa! Ota ohjaimet käteen ja valmistaudu nousuun!")
        time.sleep(3)
        if funktiot.press_arrow_keys_fast(3.0) == 1:
            funktiot.change_point_win(name)
            print("+1 piste")
            time.sleep(4)
            funktiot.clear_line()
        while True:
            try:
                events = funktiot.random_events(1)
            except ValueError:
                print("Virheellinen syöte, yritä uudelleen!")
                time.sleep(2)
                funktiot.clear_line()
                continue
            break
        if events == 1:
            funktiot.change_point_win(name)
            print("+1 piste")
            time.sleep(3)
            funktiot.clear_line()

            print("Valmistaudu ohjaamaan lentokonetta vaikeuksien aikana.")
            time.sleep(3)
            if funktiot.press_arrow_keys_fast(3.0) == 1:
                funktiot.change_point_win(name)
                print("+1 piste")
                time.sleep(3)
                funktiot.clear_line()

            print(
                "Laskeutumisaika! Sää on selkeä. Laskeutuminen tulee olemaan helppoa. Ota ohjaimet käteen ja valmistaudu laskeutumaan!")
            time.sleep(4)
            if funktiot.press_arrow_keys_fast(3.0) == 1:
                funktiot.change_point_win(name)
                print("+1 piste")
                time.sleep(3)
                funktiot.clear_line()
            print("✅ Hyvin tehty! Siirrytään seuraavalle tasolle.")
            funktiot.change_location(destination, name)
            time.sleep(3)
            funktiot.clear_line()

            break
        else:
            time.sleep(3)
            funktiot.clear_line()

            print("Taso epäonnistui. Käynnistetään taso uudelleen!")
            time.sleep(3)
            funktiot.clear_line()

            funktiot.default_settings(name)
            continue


def level_two(name):
    points = funktiot.get_points(name)
    while True:
        current_location = funktiot.get_location(name)
        print(f"Taso 2, peli tulee vaikeutumaan! Sinulla on {points} pistettä.")
        country_code = input(
            f"Olet tällä hetkellä sijainnissa {current_location[1]}. Minkä maan haluaisit tutkia seuraavaksi? Syötä maan koodi (esim. US, FI): ")
        airports = funktiot.get_airport_list(country_code)
        if len(airports) == 0:
            print("Yritä uudelleen!")
            continue
        for airport in airports:
            print(f"{airport[0]}: {airport[1]}")
        while True:
            destination = input("Valmiina nousuun? Syötä määränpääsi lentokentän ID: ")
            if funktiot.check_airport_availability(destination, country_code) == False:
                print("Yritä uudelleen!")
                continue
            break
        time.sleep(1)
        funktiot.airplane_shape()
        print("Sää on pilvinen! Nousu tulee olemaan hieman vaikeampaa kuin viime kerralla.")
        time.sleep(3)
        funktiot.clear_line()
        print("Nousu alkaa! Ota ohjaimet käteen ja valmistaudu nousuun!")
        time.sleep(3)
        if funktiot.press_arrow_keys_fast(2.5) == 1:
            funktiot.change_point_win(name)
            print("+1 piste")
            time.sleep(4)
            funktiot.clear_line()
        while True:
            try:
                events = funktiot.random_events(1)
            except ValueError:
                print("Virheellinen syöte, yritä uudelleen!")
                time.sleep(2)
                funktiot.clear_line()
                continue
            break
        if events == 1:
            funktiot.change_point_win(name)
            print("+1 piste")
            time.sleep(3)
            funktiot.clear_line()

            print("Valmistaudu ohjaamaan lentokonetta vaikeuksien aikana.")
            time.sleep(3)
            if funktiot.press_arrow_keys_fast(2.5) == 1:
                funktiot.change_point_win(name)
                print("+1 piste")
                time.sleep(3)
                funktiot.clear_line()

            print(
                "Laskeutumisaika! Sää on pilvinen. Laskeutuminen tulee olemaan hieman vaikeampaa kuin viime kerralla. Ota ohjaimet käteen ja valmistaudu laskeutumaan!")
            time.sleep(4)
            if funktiot.press_arrow_keys_fast(2.5) == 1:
                funktiot.change_point_win(name)
                print("+1 piste")
                time.sleep(3)
                funktiot.clear_line()
            print("✅ Hyvin tehty! Siirrytään seuraavalle tasolle.")
            funktiot.change_location(destination, name)
            time.sleep(3)
            funktiot.clear_line()
            break
        else:
            time.sleep(3)
            funktiot.clear_line()
            print("Taso epäonnistui. Käynnistetään taso uudelleen!")
            time.sleep(3)
            funktiot.clear_line()
            points
            continue


def level_three(name):
    points = funktiot.get_points(name)
    while True:
        current_location = funktiot.get_location(name)
        print(f"Taso 3, peli tulee olemaan vielä vaikeampaa! Sinulla on {points} pistettä.")
        country_code = input(
            f"Olet tällä hetkellä sijainnissa {current_location[1]}. Minkä maan haluaisit tutkia seuraavaksi? Syötä maan koodi (esim. US, FI): ")
        airports = funktiot.get_airport_list(country_code)
        if len(airports) == 0:
            print("Yritä uudelleen!")
            continue
        for airport in airports:
            print(f"{airport[0]}: {airport[1]}")
        while True:
            destination = input("Valmiina nousuun? Syötä määränpääsi lentokentän ID: ")
            if funktiot.check_airport_availability(destination, country_code) == False:
                print("Yritä uudelleen!")
                continue
            break
        time.sleep(1)
        funktiot.airplane_shape()
        print("Sää on sateinen! Nousu tulee olemaan hieman vaikeampaa kuin viime kerralla.")
        time.sleep(3)
        funktiot.clear_line()
        print("Nousu alkaa! Ota ohjaimet käteen ja valmistaudu nousuun!")
        time.sleep(3)
        if funktiot.press_arrow_keys_fast(2.0) == 1:
            funktiot.change_point_win(name)
            print("+1 piste")
            time.sleep(4)
            funktiot.clear_line()
        while True:
            try:
                events = funktiot.random_events(1)
            except ValueError:
                print("Virheellinen syöte, yritä uudelleen!")
                time.sleep(2)
                funktiot.clear_line()
                continue
            break
        if events == 1:
            funktiot.change_point_win(name)
            print("+1 piste")
            time.sleep(3)
            funktiot.clear_line()

            print("Valmistaudu ohjaamaan lentokonetta vaikeuksien aikana.")
            time.sleep(3)
            if funktiot.press_arrow_keys_fast(2.0) == 1:
                funktiot.change_point_win(name)
                print("+1 piste")
                time.sleep(3)
                funktiot.clear_line()

            print(
                "Laskeutumisaika! Sää on sateinen. Laskeutuminen tulee olemaan hieman vaikeampaa kuin viime kerralla. Ota ohjaimet käteen ja valmistaudu laskeutumaan!")
            time.sleep(4)
            if funktiot.press_arrow_keys_fast(2.0) == 1:
                funktiot.change_point_win(name)
                print("+1 piste")
                time.sleep(3)
                funktiot.clear_line()
            print("✅ Hyvin tehty! Siirrytään seuraavalle tasolle.")
            funktiot.change_location(destination, name)
            time.sleep(3)
            funktiot.clear_line()
            break
        else:
            time.sleep(3)
            funktiot.clear_line()
            print("Taso epäonnistui. Käynnistetään taso uudelleen!")
            time.sleep(3)
            funktiot.clear_line()
            points
            continue


def level_four(name):
    points = funktiot.get_points(name)
    while True:
        current_location = funktiot.get_location(name)
        print(f"Taso 4, peli tulee olemaan vielä vaikeampaa! Sinulla on {points} pistettä.")
        country_code = input(
            f"Olet tällä hetkellä sijainnissa {current_location[1]}. Minkä maan haluaisit tutkia seuraavaksi? Syötä maan koodi (esim. US, FI): ")
        airports = funktiot.get_airport_list(country_code)
        if len(airports) == 0:
            print("Yritä uudelleen!")
            continue
        for airport in airports:
            print(f"{airport[0]}: {airport[1]}")
        while True:
            destination = input("Valmiina nousuun? Syötä määränpääsi lentokentän ID: ")
            if funktiot.check_airport_availability(destination, country_code) == False:
                print("Yritä uudelleen!")
                continue
            break
        time.sleep(1)
        funktiot.airplane_shape()
        print("Sää on tuulinen! Nousu tulee olemaan hieman vaikeampaa kuin viime kerralla.")
        time.sleep(3)
        funktiot.clear_line()
        print("Nousu alkaa! Ota ohjaimet käteen ja valmistaudu nousuun!")
        time.sleep(3)
        if funktiot.press_arrow_keys_fast(1.7) == 1:
            funktiot.change_point_win(name)
            print("+1 piste")
            time.sleep(4)
            funktiot.clear_line()
        while True:
            try:
                events = funktiot.random_events(1)
            except ValueError:
                print("Virheellinen syöte, yritä uudelleen!")
                time.sleep(2)
                funktiot.clear_line()
                continue
            break
        if events == 1:
            funktiot.change_point_win(name)
            print("+1 piste")
            time.sleep(3)
            funktiot.clear_line()

            print("Valmistaudu ohjaamaan lentokonetta vaikeuksien aikana.")
            time.sleep(3)
            if funktiot.press_arrow_keys_fast(1.7) == 1:
                funktiot.change_point_win(name)
                print("+1 piste")
                time.sleep(3)
                funktiot.clear_line()

            print(
                "Laskeutumisaika! Sää on tuulinen. Laskeutuminen tulee olemaan hieman vaikeampaa kuin viime kerralla. Ota ohjaimet käteen ja valmistaudu laskeutumaan!")
            time.sleep(4)
            if funktiot.press_arrow_keys_fast(1.7) == 1:
                funktiot.change_point_win(name)
                print("+1 piste")
                time.sleep(3)
                funktiot.clear_line()
            print("✅ Hyvin tehty! Siirrytään seuraavalle tasolle.")
            funktiot.change_location(destination, name)
            time.sleep(3)
            funktiot.clear_line()
            break
        else:
            time.sleep(3)
            funktiot.clear_line()
            print("Taso epäonnistui. Käynnistetään taso uudelleen!")
            time.sleep(3)
            funktiot.clear_line()
            points
            continue


def level_five(name):
    points = funktiot.get_points(name)
    while True:
        current_location = funktiot.get_location(name)
        print(f"Taso 5, tämä on viimeinen ja vaikein taso! Sinulla on {points} pistettä.")
        country_code = input(
            f"Olet tällä hetkellä sijainnissa {current_location[1]}. Minkä maan haluaisit tutkia seuraavaksi? Syötä maan koodi (esim. US, FI): ")
        airports = funktiot.get_airport_list(country_code)
        if len(airports) == 0:
            print("Yritä uudelleen!")
            continue
        for airport in airports:
            print(f"{airport[0]}: {airport[1]}")
        while True:
            destination = input("Valmiina nousuun? Syötä määränpääsi lentokentän ID: ")
            if funktiot.check_airport_availability(destination, country_code) == False:
                print("Yritä uudelleen!")
                continue
            break
        time.sleep(1)
        funktiot.airplane_shape()
        print("Sää on myrskyinen! Nousu tulee olemaan hieman vaikeampaa kuin viime kerralla.")
        time.sleep(3)
        funktiot.clear_line()
        print("Nousu alkaa! Ota ohjaimet käteen ja valmistaudu nousuun!")
        time.sleep(3)
        if funktiot.press_arrow_keys_fast(1.3) == 1:
            funktiot.change_point_win(name)
            print("+1 piste")
            time.sleep(4)
            funktiot.clear_line()
        while True:
            try:
                events = funktiot.random_events(1)
            except ValueError:
                print("Virheellinen syöte, yritä uudelleen!")
                time.sleep(2)
                funktiot.clear_line()
                continue
            break
        if events == 1:
            funktiot.change_point_win(name)
            print("+1 piste")
            time.sleep(3)
            funktiot.clear_line()

            print("Valmistaudu ohjaamaan lentokonetta vaikeuksien aikana.")
            time.sleep(3)
            if funktiot.press_arrow_keys_fast(1.3) == 1:
                funktiot.change_point_win(name)
                print("+1 piste")
                time.sleep(3)
                funktiot.clear_line()

            print(
                "Laskeutumisaika! Sää on myrskyinen. Laskeutuminen tulee olemaan hieman vaikeampaa kuin viime kerralla. Ota ohjaimet käteen ja valmistaudu laskeutumaan!")
            time.sleep(4)
            if funktiot.press_arrow_keys_fast(1.3) == 1:
                funktiot.change_point_win(name)
                print("+1 piste")
                time.sleep(3)
                funktiot.clear_line()
            print("✅ Hyvin tehty! Peli on nyt ohi! Ole ylpeä itsestäsi!")
            funktiot.change_location(destination, name)
            time.sleep(3)
            funktiot.clear_line()
            break
        else:
            time.sleep(3)
            funktiot.clear_line()
            print("Taso epäonnistui. Käynnistetään taso uudelleen!")
            time.sleep(3)
            funktiot
