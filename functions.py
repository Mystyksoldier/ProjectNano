import random

def chooseYourGame():
    choice = input("Kies een spel(Raad het nummer, Galgje, Steen papier schaar): ").lower()
    if choice == "raad het nummer":
        GuessTheNumber()
    elif choice == "galgje":
        Galgje()
    else:
        print(f"{choice} is nog niet geimplementeerd")

def GuessTheNumber():
    TheNumber = random.randint(1, 100)

    coupons = 5

    for coupon in range(1, coupons + 1):
        TheGuess = input("Raad het cijder tussen de 1 en de 100?: ")
        if TheNumber == int(TheGuess):
            print("hoera je hebt nummer " + str(TheNumber) + " geraden.")
            break
        else:
            print("je hebt het fout probeer het opnieuw. :(")

    if coupon == coupons and TheGuess != TheNumber:
        print("je hebt het spel verloren take the L")

def Galgje():
    galgjefiguur = [
        """
        -----
        |   |
            |
            |
            |
            |
        =========
        """,
        """
        -----
        |   |
        o   |
            |
            |
            |
        =========
        """,
        """
        -----
        |   |
        o   |
        |   |
            |
            |
        =========
        """,
        """
        -----
        |   |
        o   |
       /|   |
            |
            |
        =========
        """,
        """
        -----
        |   |
        o   |
       /|\  |
            |
            |
        =========
        """,
        """
        -----
        |   |
        o   |
       /|\  |
       /    |
            |
        =========
        """,
        """
        -----
        |   |
        o   |
       /|\  |
       / \  |
            |
        =========
        """,
    ]

    goedeLetters = []
    fouteLetters = []

    woord = input("Geef een woord om te gebruiken voor het spel: ").lower()

    status = ["_" for _ in woord]

    while True:
        print(galgjefiguur[len(fouteLetters)])
        print("Woord: " + " ".join(status))
        print(f"Foute letters: {', '.join(fouteLetters)}")

        if "_" not in status:
            print("Gefeliciteerd! Je hebt het woord geraden!")
            break
        if len(fouteLetters) >= len(galgjefiguur) - 1:
            print("Helaas, je hebt verloren. Het woord was:", woord)
            break

        letter = input("Geef een letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Ongeldige invoer. Geef een enkele letter.")
            continue
        if letter in goedeLetters or letter in fouteLetters:
            print("Je hebt deze letter al geraden. Probeer een andere letter.")
            continue

        if letter in woord:
            print(f"Het woord bevat de letter '{letter}'")
            goedeLetters.append(letter)

            for i, char in enumerate(woord):
                if char == letter:
                    status[i] = letter
        else:
            print(f"Het woord bevat niet de letter '{letter}'")
            fouteLetters.append(letter)
