import mysql.connector
from geopy.distance import geodesic


def get_airport_coordinates(icao_code):
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        database = "flight_game",
        user = "root",
        password = "pass",
        autocommit = True
    )

    cursor = connection.cursor()

    sql = """
        SELECT latitude_deg, longitude_deg
        FROM airport
        WHERE ident = %s
    """

    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


def run_airport_distance():
    icao1 = input("Enter the ICAO code of the first airport: ").strip().upper()
    icao2 = input("Enter the ICAO code of the second airport: ").strip().upper()

    coords1 = get_airport_coordinates(icao1)
    if coords1 is None:
        print(f"Airport with ICAO code {icao1} not found in the database.")
        return

    coords2 = get_airport_coordinates(icao2)
    if coords2 is None:
        print(f"Airport with ICAO code {icao2} not found in the database.")
        return

    distance = geodesic(coords1, coords2).kilometers

    print(f"Distance between {icao1} and {icao2}: {distance:.2f} kilometers")


run_airport_distance()