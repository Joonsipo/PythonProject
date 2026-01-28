correct_username = ("python")
correct_password = ("rules")
kirjautumisyritykset = 0
liian_monta_yritysta = 5

while kirjautumisyritykset < liian_monta_yritysta:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        kirjautumisyritykset = kirjautumisyritykset + 1
        if kirjautumisyritykset < liian_monta_yritysta:
            print("Incorrect username or password. Please try again.")

if kirjautumisyritykset == liian_monta_yritysta:
    print("Access denied")