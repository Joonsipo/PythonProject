sukupuoli = (input("Enter biological gender (male/female): ")).lower()
hemoglobiiniarvo = float(input("Enter hemoglobin value (g/l): "))

if sukupuoli == "male":
    if hemoglobiiniarvo < 134:
        print("Your hemoglobin is low.")
    elif 134 <= hemoglobiiniarvo <= 167:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")

elif sukupuoli == "female":
    if hemoglobiiniarvo < 117:
        print("Your hemoglobin is low.")
    elif 117 <= hemoglobiiniarvo <= 155:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")

else:
    print("Invalid gender.")