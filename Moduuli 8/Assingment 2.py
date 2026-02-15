import mysql.connector


def get_airports_by_country(country_code):
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
        SELECT type, COUNT(*)
        FROM airport
        WHERE iso_country = %s
        GROUP BY type
        ORDER BY type
    """

    cursor.execute(sql, (country_code,))
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland):\n")

    country_code = country_code.strip()
    country_code = country_code.replace("'", "")
    country_code = country_code.replace('"', "")
    country_code = country_code.upper()

    airports = get_airports_by_country(country_code)

    if len(airports) == 0:
        print(f"No airports found for country code {country_code}.")
    else:
        print()
        print(f"Airports in {country_code}:")
        for airport_type, count in airports:
            print(f"{count} {airport_type} airports")

run_country_program()