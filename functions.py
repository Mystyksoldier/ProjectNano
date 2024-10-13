import random

def welcome():
    print("**************************************")
    print("*                                    *")
    print("*     WELKOM BIJ EPIC NANOGAMES!     *")
    print("*                                    *")
    print("**************************************")
    print("")
    print("Gemaakt door Dave Havelaar.")
    print("")

def chooseYourGame():
    while True:
        choice = input("Kies een spel(1: Raad het nummer, 2: Galgje, 3: Steen papier schaar, 4: Bim Bam Baap, 5: Exit): ")
        if choice == "1":
            GuessTheNumber()
            break
        elif choice == "2":
            Galgje()
            break
        elif choice == "3":
            rockPaperScissors()
        elif choice == "4":
            bimBamBaap()
            break
        elif choice == "5":
            print("Bedankt voor het spelen!")
            break
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
    
    #ask for a replay
    replay = input("Wil je nog een keer spelen? (ja/nee): ").lower()
    if replay == "ja":
        GuessTheNumber()
    else:
        replayOtherGame()

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
    name = input("Wat is je naam?: ")

    file_name = None

    #continue the task til a difficulty is chosen
    while file_name is None:

        difficulty = input("Geef de moeilijkheidsgraad aan (makkelijk, normaal, moeilijk): ").lower()

        if difficulty == "makkelijk":
            file_name = "data/easy.txt"
        elif difficulty == "normaal":
            file_name = "data/normal.txt"
        elif difficulty == "moeilijk":
            file_name = "data/hard.txt"
        else:
            print("Dit is niet geïmplementeerd")
    
    #opens the correct dificulty file and spilt the words
    with open(file_name, "r") as f:
        list = f.read().split(",")

    woord = random.choice(list).lower()

    status = ["_" for _ in woord]

    while True:
        #shows the game status and the letters that are already guessed
        print(galgjefiguur[len(fouteLetters)])
        print(f"{name}")
        print("Woord: " + " ".join(status))
        print(f"Foute letters: {', '.join(fouteLetters)}")

        #checks if you won or lost the game
        if "_" not in status:
            print("Gefeliciteerd! Je hebt het woord geraden!")
            break
        if len(fouteLetters) >= len(galgjefiguur) - 1:
            print("Helaas, je hebt verloren. Het woord was:", woord)
            break

        letter = input("Geef een letter: ").lower()

        #checks if the input is correct
        if len(letter) != 1 or not letter.isalpha():
            print("Ongeldige invoer. Geef een enkele letter.")
            continue
        if letter in goedeLetters or letter in fouteLetters:
            print("Je hebt deze letter al geraden. Probeer een andere letter.")
            continue

        #checks if the letter is in the word if not the in the wrong letters list
        if letter in woord:
            print(f"Het woord bevat de letter '{letter}'")
            goedeLetters.append(letter)

            for i, char in enumerate(woord):
                if char == letter:
                    status[i] = letter
        else:
            print(f"Het woord bevat niet de letter '{letter}'")
            fouteLetters.append(letter)

    #ask for a replay
    replay = input("Wil je nog een keer spelen? (ja/nee): ").lower()
    if replay == "ja":
        Galgje()
    else:
        replayOtherGame()

def rockPaperScissors():
    
    gameRounds = None

    while gameRounds is None:

        gameMode = input("kies de game mode (1: tot de drie punten, 2: tot de vijf punten, 3: één ronde,): ")

        if gameMode == "1":
            gameRounds = 3
        elif gameMode == "2":
            gameRounds = 5
        elif gameMode == "3":
            gameRounds = 1

    playerScore = 0
    computerScore = 0
    rounds = 0

    while True:

        #checks if the game is over
        if playerScore == gameRounds or computerScore == gameRounds:
            if playerScore > computerScore:
                print(f"Je hebt gewonnen met {playerScore} tegen {computerScore}")
            elif playerScore < computerScore:
                print(f"Je hebt verloren met {playerScore} tegen {computerScore}")
            else:
                print(f"Het is gelijkspel met {playerScore} tegen {computerScore}")
            break
        else:
            #print the score and the round
            print(f"Speler: {playerScore} - Computer: {computerScore}")
            print(f"Ronde {rounds}")

            playerChoice = input("Kies steen, papier of schaar: ").lower()

            if playerChoice not in ["steen", "papier", "schaar"]:
                print("Ongeldige invoer. Kies steen, papier of schaar.")
                continue
            else:
                computerChoice = random.choice(["steen", "papier", "schaar"])

                if playerChoice == computerChoice:
                    print(f"Computer koos {computerChoice}. Het is gelijkspel.")
                elif playerChoice == "steen":
                    if computerChoice == "papier":
                        print(f"Computer koos {computerChoice}. Computer wint!")
                        computerScore += 1
                    else:
                        print(f"Computer koos {computerChoice}. Jij wint!")
                        playerScore += 1
                elif playerChoice == "papier":
                    if computerChoice == "schaar":
                        print(f"Computer koos {computerChoice}. Computer wint!")
                        computerScore += 1
                    else:
                        print(f"Computer koos {computerChoice}. Jij wint!")
                        playerScore += 1
                elif playerChoice == "schaar":
                    if computerChoice == "steen":
                        print(f"Computer koos {computerChoice}. Computer wint!")
                        computerScore += 1
                    else:
                        print(f"Computer koos {computerChoice}. Jij wint!")
                        playerScore += 1
                rounds += 1

    #ask for a replay
    replay = input("Wil je nog een keer spelen? (ja/nee): ").lower()
    if replay == "ja":
        rockPaperScissors()
    else:
        replayOtherGame()

def bimBamBaap():

    #gets all the questions from the file
    with open("data/bimbambaap.txt", "r") as f:
        list = f.read().split(",")

    #creates the first random letter
    alphabet = str("abcdefghijklmnopqrstuvwxyz")
    randomLetter = random.choice(alphabet)
    randomLetter = randomLetter.upper()
    
    #say in the beginning how to stop the game
    print(f"Als je wilt stoppen type dan 'stop' in.")

    #the loop for the rest of the game
    while True:
        randomquestion = random.choice(list)
        print(randomLetter)
        print(randomquestion)
        answer = input("Geef antwoord: ").lower()

        if len(answer) == 0 or not answer.isalpha():
            print("Je moet een antwoord geven")
            continue

        if answer == "stop":
            break

        firstLetter = answer[0].upper()
        if firstLetter == randomLetter:
            lastLetter = answer[-1].upper()
            randomLetter = lastLetter
        else:
            print(f"Het woord moet beginnen met de letter {randomLetter}")
    
    #ask for a replay
    replay = input("Wil je nog een keer spelen? (ja/nee): ").lower()
    if replay == "ja":
        bimBamBaap()
    else:
        replayOtherGame()

def replayOtherGame():
    replay = input("Wil je een ander spel spelen? (ja/nee): ").lower()
    if replay == "ja":
        chooseYourGame()
    else:
        print("Bedankt voor het spelen!")
