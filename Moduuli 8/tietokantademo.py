import mysql.connector

def hae_data():
    sql = SELECT * FROM hae_data()
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Päivää! Olen {rivi[2]} {rivi[1]}. Palkkani on {rivi[3]} euroa kuussa.")
    return

# Pääohjelma
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='pass',
         autocommit=True
         )

sukunimi = input("Anna sukunimi: ")
hae_työntekijät_sukunimellä(sukunimi)