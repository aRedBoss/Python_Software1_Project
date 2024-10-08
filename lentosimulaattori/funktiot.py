import mysql.connector
from geopy.distance import geodesic
from random import randint
import random
import time
import os
import keyboard

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='omar',
    password='Amoury123',
    charset='utf8mb4',
    collation='utf8mb4_general_ci',
    autocommit=True
)

# Done by Omar
def player_exists(name):
    sql = "select count(screen_name) from game where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    cursor.close()

    return result[0] > 0

# Done by Omar
def get_count_of_players():
    sql = "select count(id) from game;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()

    return result[0]

# Done by Omar
def add_player(name):
    if player_exists(name):
        print("Tervetuloa takaisin!")
    else:
        count = get_count_of_players()
        player_id = count + 1
        sql = "insert into game (id, co2_consumed, co2_budget, location, screen_name, points) values (%s, %s, %s, %s, %s, %s)"
        values = [player_id, 0, 10000, 'EFHK', name, 0]
        cursor = yhteys.cursor()
        cursor.execute(sql, values)
        yhteys.commit()
        cursor.close()
    return

# Done by Hussein
def get_points(name):
    sql = "select points from game where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()

    return result[0]



# Done by Hussein
def change_point_win(name):
    sql = "update game set game.points = (game.points + 1) where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    yhteys.commit()
    cursor.close()

    return "Olet ansainnut pisteen!"

# Done by Hussein
def change_point_lost(name):
    sql = "update game set game.points = (game.points - 1) where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    yhteys.commit()
    cursor.close()

    return "Olet hävinnyt pisteen!"

# Done by Omar
def default_settings(name):
    sql = "update game set game.points = 0, game.co2_consumed = 0, game.location = 'EFHK' where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    yhteys.commit()
    cursor.close()

    return "Players values set to default"

# Done by Omar, Hussein, Mostafa, Cahit
def random_events(level):
    if level == 1:

        while True:
            random_event = random.randint(1, 3)

            if random_event == 1:
                print("\n⚠️  Olet kohdannut myrskyn kesken lennon! Tee oikea päätös, jotta pääset turvallisesti jatkamaan.")
                print("1. Lennä turvallisesti myrskyn yläpuolella.")
                print("2. Lennä suoraan myrskyn läpi.")
                print("3. Yritä vaarallista hätälaskua mereen.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 1:
                    print("✅ Oikein! Vältit onnistuneesti myrskyn ja jatkat matkaasi.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Väärä valinta! Lentokone törmäsi.")
                    return 2
            elif random_event == 2:
                print("\n🌪️  Varoitus: Olet saapumassa turbulenssivyöhykkeelle! Valitse toimintasi huolellisesti.")
                print("1. Sukella alemmalle korkeudelle paetaksesi turbulenssia.")
                print("2. Pidä nykyinen korkeus ja koita kestää se.")
                print("3. Nouse korkeammalle väistääksesi turbulenssia turvallisesti.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 3:
                    print("✅ Viisas valinta! Nousit korkeammalle ja väistät turbulenssia sujuvasti.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Huono valinta! Turbulenssi pahenee ja aiheuttaa vahinkoa lentokoneelle.")
                    return 2

            elif random_event == 3:
                print("\n🔧  Varoitus: Olet kohdannut mekaanisen vian! Päätä, miten reagoit.")
                print("1. Jatka lentoa normaalisti, ei hätää.")
                print("2. Yritä selvittää ongelma ja jatka lentoa mahdollisimman vakaasti.")
                print("3. Sammuta moottori ja leiju alas.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 2:
                    print("✅ Hyvä valinta! Arvioit tilanteen ja vakautat lennon.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Huono valinta! Lentokone törmäsi.")
                    return 2

    if level == 2:
        while True:
            random_event = random.randint(1, 3)

            if random_event == 1:
                print("\n⚠️  Varoitus: Lentokoneesi polttoainevarat ovat vähissä. Miten reagoit?")
                print("1. Etsi lähin paikka, johon voit laskeutua ja laskeudu. Jatka sen jälkeen matkaa.")
                print("2. Lennä suoraan lähimmälle lentokentälle, vaikka se olisi kaukana.")
                print("3. Yritä säästää polttoainetta leijumalla ja valitse reitti sen mukaan.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 1:
                    print("✅ Hyvä valinta! Tankkasit lentokoneen ja nyt jatkat matkaa.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Huono valinta! Lentokoneesta loppui polttoaine, ja se törmäsi maahan.")
                    return 2
            elif random_event == 2:
                print("\n🌪️  Hälytys: Olet kohdannut voimakkaan tuulen, joka uhkaa lennon vakaata kulkua. Miten toimit?")
                print("1. Pysy nykyisellä reitillä ja odota, että tuuli laantuu.")
                print("2. Vaihda reittiä ja etsi suojaisampi alue.")
                print("3. Käynnistä kaikki moottorit täysillä ja yritä voittaa tuuli.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 2:
                    print("✅ Hyvä valinta! Väistit tuulen.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Huono valinta! Lentokone ei kestänyt voimakkaita tuulia ja vaurioitui.")
                    return 2
            elif random_event == 3:
                print("\n🔧  Lentosi aikana yksi matkustaja alkaa käyttäytyä levottomasti ja uhkaavasti. Miten toimit?")
                print("1. Ohita tilanne ja keskity lennon ohjaamiseen.v")
                print("2. Ilmoita heti lentohenkilökunnalle ja pyydä apua.")
                print("3. Pyydä muita matkustajia rauhoittumaan ja yritä keskustella matkustajan kanssa.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 2:
                    print("✅ Oikea valinta! Henkilökunta hallitsee tilanteen..")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Huono valinta! Levoton matkustaja aiheuttaa pelkoa muissa matkustajissa, joten hätälasku on tarpeen.")
                    return 2
    if level == 3:
        while True:
            random_event = random.randint(1, 3)

            if random_event == 1:
                print("\n⚠️  Varoitus: Säteilytutkasi näyttää epätavallista aktiviteettia alueella, jossa lennät. Miten toimit?")
                print("1. Ilmoita välittömästi lennonjohdolle ja noudata heidän ohjeitaan.")
                print("2. Jatka lentoa normaalisti ja toivo parasta.")
                print("3. Muuta reittiä ja nouse korkeammalle, kunnes olet turvallisemmalla alueella.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 1:
                    print("✅ Oikea valinta! Lennonjohdon ilmoittaminen auttaa varmistamaan, että saat oikeat ohjeet ja tuen tilanteen käsittelyyn.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Väärä valinta! Tämä ei ollut järkevin valinta, koska vaaratilanteita ei tule aliarvioida.")
                    continue
            elif random_event == 2:
                print("\n🌪️  Varoitus: Matkustaja ilmoittaa, että hän on menettänyt tajuntansa kesken lennon. Miten reagoit?")
                print("1. Ohita tilanne, koska se ei liity lentoon.")
                print("2. Pyydä matkustajia rauhoittumaan ja tarkista tilanne itse.")
                print("3. Ilmoita heti lentohenkilökunnalle ja ryhdy ensiaputoimiin.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 3:
                    print("✅ Oikea valinta! Sillä ensiapu ja oikea-aikainen ilmoittaminen auttavat matkustajaa ja muita matkustajia tuntemaan olonsa turvalliseksi.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Väärä valinta! Tämä ei ollut oikea päätös, sillä matkustajien turvallisuus ja hyvinvointi ovat ensisijaisia.")
                    continue
            elif random_event == 3:
                print("\n🔧  Varoitus: Lentokoneesi ilmaisinjärjestelmä näyttää virheellisiä tietoja, ja olet epävarma korkeudestasi. Mikä on toimintasi?")
                print("1. Luota silmämääräiseen arvioon ja tee päätöksesi sen mukaan.")
                print("2. Pysähdy ja yritä korjata vika ennen kuin jatkat matkaa.")
                print("3. Vahvista tietosi muista järjestelmistä ja toimi niiden mukaan.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 3:
                    print("✅ Onnittelut! Varajärjestelmien käyttö voi estää virheitä ja varmistaa, että lentosi on turvallinen.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Pahoittelut!! Tämä ei ollut hyvä valinta, koska silmämääräinen arviointi voi olla epätarkkaa ja johtaa vaarallisiin tilanteisiin.")
                    continue
    if level == 4:
        while True:
            random_event = random.randint(1, 3)

            if random_event == 1:
                print("\n⚠️  Varoitus: Lentosi aikana havaitset, että toinen lentokone on tullut vaarallisen lähelle. Miten toimit?")
                print("1. Yritä manuaalisesti muuttaa korkeutta ja suuntaa väistääksesi toista konetta.")
                print("2. Ilmoita lennonjohdolle ja noudata heidän ohjeitaan.")
                print("3. Hidasta kone ja odota, että toinen lentokone ohittaa.v")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 2:
                    print("✅ Onnittelut!  Lennonjohdon ohjeet auttavat sinua navigoimaan turvallisesti.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Pahoittelut! Et voi toimia itsenäisesti tällaisessa tilanteessa ilman ohjeita.")
                    continue
            elif random_event == 2:
                print("\n🌪️  Vaara: Olet kohdannut äkillisen jäätävän sään, joka voi aiheuttaa ongelmia lentosi aikana. Mitä teet?")
                print("1. Laskeudu nopeasti lämpimämmälle alueelle.")
                print("2. Tee nopea analyysi ja säädä lentosuunnitelma jäätävien alueiden välttämiseksi.")
                print("3. Ilmoita matkustajille, että he eivät saa hätääntyä, ja jatka normaalisti.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 2:
                    print("✅ Oikea vastaus! Jäätävä sää vaatii ennakoivaa reagointia turvallisuuden takaamiseksi.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Väärä valinta! Tämä ei ollut paras vaihtoehto.")
                    continue
            elif random_event == 3:
                print("\n🔧  Hälytys: Lentokoneesi navigointijärjestelmä epäonnistuu, ja olet epävarma sijainnistasi. Mikä on seuraava toimintasi?")
                print("1. Ilmoita lennonjohdolle ja pyydä tarkkoja koordinaatteja.")
                print("2. Luota muihin järjestelmiin ja jatka lentoa.")
                print("3. Käytä visuaalisia maamerkkejä ja tee arvio sijainnistasi.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 1:
                    print("✅ Hyvä valinta! Olet valinnut parhaan vaihtoehdon, joka varmistaa, että saat oikeat tiedot ja tuen tilanteen selvittämiseksi.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Huono valinta! Tämä ei ollut hyvä valinta, sillä navigoinnin epävarmuus voi aiheuttaa vaarallisia tilanteita.")
                    continue
    if level == 5:
        while True:
            random_event = random.randint(1, 3)

            if random_event == 1:
                print("\n⚠️  Varoitus: Olet lentänyt alueella, jossa on tiedossa voimakas sähkömyrsky. Laitteistosi näyttää olevan normaali, mutta tiedät, että myrskyn saapuessa asiat voivat muuttua nopeasti. Miten toimit?")
                print("1. Nouse korkeammalle, sillä sähkömyrskyjen yläpuolella on yleensä rauhallista.")
                print("2. Jatka normaalisti ja toivo parasta.")
                print("3. Muuta reittiä ja vältä myrskyä, vaikka se tarkoittaisi lisää lentoaikaa.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 3:
                    print("✅ Hyvä valinta! Olet toiminut oikein, sillä myrskyn välttäminen on aina paras vaihtoehto turvallisuuden kannalta.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Huono valinta! Myrskyt voivat vaikuttaa kaikkiin korkeuksiin ja vaarantaa lentosi.")
                    continue
            elif random_event == 2:
                print("\n🌪️  Hälytys: Lentosi aikana havaitset, että yksi moottori on ylikuumentunut ja käynnistää itsensä uudelleen kesken lennon. Miten toimit?")
                print("1. Ilmoita lennonjohdolle, että moottori on ylikuumentunut, ja valmistautu hätälaskuun.")
                print("2. Jatka lentoa normaalisti, sillä moottorin itsenäinen uudelleenkäynnistys on yleensä turvallista.")
                print("3. Sammuta ylikuumentunut moottori ja yritä laskeutua lähimmälle kentälle.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 1:
                    print("✅ Oikea valinta! Moottorin ylikuumeneminen voi johtaa vakaviin ongelmiin, ja lennonjohdon tuki on elintärkeää.v")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Väärin! Tämä ei ollut paras päätös, sillä moottorin ylikuumeneminen voi aiheuttaa vaaratilanteita.")
                    continue
            elif random_event == 3:
                print("\n🔧  Hälytys: Kohtaat äkillisen ja vakavan systeemihäiriön, joka vaikuttaa useisiin järjestelmiin samanaikaisesti. Mitä teet?")
                print("1. Ilmoita lennonjohdolle, arvioi tilanne ja valmistaudu hätälaskuun.")
                print("2. Yritä sammuttaa ja käynnistää järjestelmät uudelleen.")
                print("3. Luota varajärjestelmiin ja jatka lentoa normaalisti.")
                choice = int(input("Valitse 1, 2 tai 3: "))
                if choice == 1:
                    print("✅ Hyvä valinta! Kriittiset systeemihäiriöt vaativat aina huolellista arviointia ja apua.")
                    return 1
                elif choice > 3:
                    print("Virheellinen syöte, yritä uudelleen!")
                    time.sleep(2)
                    clear_line()
                    continue
                else:
                    print("💥 Huono valinta! Tämä voi pahentaa tilannetta ja johtaa entistä vakavampiin ongelmiin.")
                    continue

# Done by Mostafa
def get_location(name):
    sql = """  select country.name, airport.name, airport.id 
                from country 
                inner join airport 
                on country.iso_country = airport.iso_country 
                inner join game 
                on game.location = airport.gps_code 
                where game.screen_name = %s"""
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    cursor.close()

    return result
# Done by Mostafa
def get_airport_id(name):
    sql = """   select airport.id from airport 
                inner join country on airport.iso_country = country.iso_country 
                inner join game on game.location = airport.gps_code 
                where game.screen_name = %s"""
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    cursor.close()

    return result

# Done by Mostafa
def get_airport_list(country_code):
    sql = """select airport.id, airport.name from airport
            inner join country 
            on country.iso_country = airport.iso_country
            where country.iso_country = %s and airport.type = "large_airport";"""
    cursor = yhteys.cursor()
    cursor.execute(sql, (country_code,))
    result = cursor.fetchall()
    cursor.close()

    return result
# Done by Nasiro
def country_code(name):
    sql = """   select country.iso_country from country 
                inner join airport on airport.iso_country = country.iso_country 
                inner join game on game.location = airport.gps_code 
                where game.screen_name = %s"""
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    cursor.close()

    return result

# Done by Omar
def check_airport_availability(destination, country_code):
    sql = """select airport.id from airport inner join country on airport.iso_country = country.iso_country where airport.id = %s and country.iso_country = %s;"""
    cursor = yhteys.cursor()
    cursor.execute(sql, (destination, country_code))
    result = cursor.fetchall()
    cursor.close()
    if len(result) == 0:
        return False
    else:
        return True

# Done by Mostafa
def change_location(destination, name):
    sql = """  update game 
                join airport on game.location = airport.gps_code 
                join country on country.iso_country = airport.iso_country
                set game.location = (select airport.gps_code from airport where id = %s)
                where game.screen_name = %s;"""

    cursor = yhteys.cursor()
    cursor.execute(sql, (destination, name))
    yhteys.commit()
    cursor.close()

    return  # (f"Player {name}'s location has been updated to {destination}")

# Done by Omar
def get_fuel(name):
    sql = """ select co2_budget, co2_consumed
                from game
                where screen_name = %s;
            """
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    cursor.close()

    return result
# Done by Omar, Mostafa
def press_arrow_keys_fast(num: float):
    arrow_keys = ['up', 'down', 'left', 'right']

    # Generate a random sequence of 5 arrow keys, ensuring no consecutive keys are the same
    sequence = []
    while len(sequence) < 5:
        next_key = random.choice(arrow_keys)
        if not sequence or next_key != sequence[-1]:  # Ensure no consecutive keys
            sequence.append(next_key)

    # Show the countdown before starting
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    print("Go!\n")

    # Start tracking time
    start_time = time.time()

    # Show the sequence to the user one key at a time
    for key in sequence:
        print(f"Paina: {key} (Sinulla on {num} sekuntia!)")
        # Wait for the user to press the correct key within the time limit
        key_start_time = time.time()  # Start time for the current key
        while time.time() - key_start_time < num:
            if keyboard.is_pressed(key):
                print("✅ Oikein!")
                break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[F\033[K', end='')
            print("💥 Liian hidas! Et saa pistettä! Siirrytään eteenpäin.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[F\033[K', end='')
            return 2

    end_time = time.time()

    total_time = end_time - start_time

    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[F\033[K', end='')
    print(f"✅ Hienoa! Painoit kaikkia näppäimiä {total_time:.2f} sekunnissa.")

    return 1

# Done by Omar
def airport_distance(name, destination):
    current_location = get_location(name)
    airport1 = current_location[1]

    airport2 = destination

    cursor = yhteys.cursor()

    sql1 = "SELECT latitude_deg, longitude_deg FROM airport WHERE name = %s"
    cursor.execute(sql1, (airport1,))
    result1 = cursor.fetchone()
    if result1 is None:
        cursor.close()
        return f"Lentokenttää {airport1} ei löytynyt."

    sql2 = "SELECT latitude_deg, longitude_deg FROM airport WHERE id = %s"
    cursor.execute(sql2, (airport2,))
    result2 = cursor.fetchone()
    if result2 is None:
        cursor.close()
        return f"Lentokenttää {airport2} ei löytynyt."

    cursor.close()

    airport1_coords = (result1[0], result1[1])
    airport2_coords = (result2[0], result2[1])

    distance = geodesic(airport1_coords, airport2_coords).kilometers


    return distance

# Done by Omar
def change_fuel(name, destination):
    distance = airport_distance(name, destination)
    fuel_consumed = (distance / 100) * 10
    sql = """update game
                set co2_consumed = co2_consumed + %s
                where screen_name = %s;
            """
    cursor = yhteys.cursor()
    cursor.execute(sql, (fuel_consumed, name))
    yhteys.commit()
    cursor.close()

    result = f"Player {name} has consumed {int(fuel_consumed)} usnit of fuel"
    # print(result)

    return result
# Done by Cahit
def display_scoreboard():
    sql = "SELECT screen_name, high_score FROM game ORDER BY high_score DESC"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    print("\nScoreboard:")
    for row in result:
        print(f"Player: {row[0]}, high score: {row[1]}")

# Done by Cahit
def get_high_score(name):
    sql = "SELECT high_score FROM game where screen_name = %s"
    cursor = yhteys.cursor()
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    cursor.close()

    return result

# Done by Cahit
def change_high_score(points, name):
    sql = """update game set high_score = %s where screen_name = %s;"""
    high_score = get_high_score(name)[0]
    if points > high_score:
        cursor = yhteys.cursor()
        cursor.execute(sql, (points, name))
        yhteys.commit()
        cursor.close()
        return 1
    return 0

# Done by Cahit
def airplane_shape():
    airplane_shape = r"""
       __|__
--o--o--´O`--o--o--
        """
    print(airplane_shape)

# Done by Mostafa
def clear_line():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[F\033[K', end='')
