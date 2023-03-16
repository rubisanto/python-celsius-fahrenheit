def celsius_vers_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit


def fahrenheit_vers_celsius(temp_fahrenheit):
    temp_celsius = (temp_fahrenheit - 32) * 5/9
    return temp_celsius


def main():
    print("Convertisseur de température")
    print("1. Celsius vers Fahrenheit")
    print("2. Fahrenheit vers Celsius")

    choix = int(input("Entrez votre choix (1 ou 2) : "))

    if choix == 1:
        temp_celsius = float(input("Entrez la température en Celsius : "))
        temp_fahrenheit = celsius_vers_fahrenheit(temp_celsius)
        print(
            f"{temp_celsius} degrés Celsius équivalent à {temp_fahrenheit} degrés Fahrenheit.")
    elif choix == 2:
        temp_fahrenheit = float(
            input("Entrez la température en Fahrenheit : "))
        temp_celsius = fahrenheit_vers_celsius(temp_fahrenheit)
        print(
            f"{temp_fahrenheit} degrés Fahrenheit équivalent à {temp_celsius} degrés Celsius.")
    else:
        print("Choix invalide. Veuillez choisir 1 ou 2.")


if __name__ == "__main__":
    main()
