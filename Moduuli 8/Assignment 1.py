import mysql.connector

conn = mysql.connector.connect()

cursor = conn.cursor()

icao_code = input("Enter the ICAO code of an airport: ").upper()

query = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(query, (icao_code,))

row = cursor.fetchone()

if row:
    name, municipality = row
    print(f"Airport name: {name}")
    print(f"Location: {municipality}")
else:
    print(f"No airport found with ICAO code {icao_code}")

cursor.close()
conn.close()