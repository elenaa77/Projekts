import random #lai no saraksta atlasītu nejaušu vārdu

def choose_word():# Funkcija izvēlas nejaušu vārdu no iepriekš definētu vārdu saraksta
    words = ['lauva', 'zilonis', 'žirafe', 'degunradis', 'zebra', 'gepards', 'hiena', 'antilope',
             'krokodils','šimpanze','gorilla','bizonis','ērglis','pūce','mangusts','pantera','anakonda']
    return random.choice(words)

def display_word(word, uzminetais_burts):
    displayed_word = ''
    for letter in word:
        if letter in uzminetais_burts:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def draw_hangman(tries):
    #Atkarībā no mēģinājumiem attēlots Hangman modelis
    stages = [
        """
           -------
           |     |
           |     
           |     
           |    
           -
        """,
        """
           -------
           |     |
           |     O
           |     
           |    
           -
        """,
        """
           -------
           |     |
           |     O
           |     |
           |    
           -
        """,
        """
           -------
           |     |
           |     O
           |    /|
           |    
           -
        """,
        """
           -------
           |     |
           |     O
           |    /|\\
           |    
           -
        """,
        """
           -------
           |     |
           |     O
           |    /|\\
           |    / 
           -
        """,
        """
           -------
           |     |
           |     O
           |    /|\\
           |    / \\
           -
        """
    ]
    print(stages[tries])

def hangman():
    game_over = False
    while not game_over:
        game_over = True
    
    MAX_TRIES = 6
    word = choose_word()# Izvēlē nejaušu vārdu
    uzminetais_burts = [] # Uzminēto burtu saraksts
    tries = 0

    print("Spēlēsim 'Hangman'!")
    print("Spēles noteikumi:")
    print("1. Jums būs jāuzmin Āfrikā dzīvojošie dzīvnieki")
    print("2. Jums jāatmin vārds, ievadot pa vienam burtam.")
    print("3. Jums ir 6 mēģinājumi uzminēt visus burtus.")
    print("4. Ja uzminēsiet burtu, tas tiks parādīts tā vietā vārdā.")
    print("5. Beigās jums būs iespēja sākt spēli no jauna")
    print("(Ja jums ir pārāk grūti uzminēt, varat izmantot iespējamo vārdu sarakstu: lauva, zilonis, degunradis, zebra, gepards, hiena, antilope, krokodils, šimpanze, gorilla, bizonis, ērglis, pūce, mangusts, pantera, anakonda)")

    while True:
        print(display_word(word, uzminetais_burts)) # Parāda vārda pašreizējo stāvokli
        draw_hangman(tries)
        guess = input("Ievadiet burtu: ").lower()

        if len(guess) != 1 or not guess.isalpha():# Pārbauda, vai kods darbojas
            print("Lūdzu, ievadiet tikai vienu burtu.")
            continue

        if guess in uzminetais_burts:# Pārbauda, vai šis burts jau ir uzminēts
            print("Jūs jau uzminējāt šo burtu.")
            continue

        uzminetais_burts.append(guess)# Pievieno uzminēto burtu sarakstam

        if guess not in word: # Ja uzminētais burts nav vārdā
            tries += 1
            print("Nepareizi!")
            print(f"Palikušie mēģinājumi: {MAX_TRIES - tries}")
            if tries >= MAX_TRIES:#Ja visi mēģinājumi ir izsmelti, spēlētājs zaudē.
                print("Jūs zaudējāt! Mērķa vārds bija:", word)
                break
        else:
            print("Pareizi!")# Ja uzminētais burts ir vārdā

        if '_' not in display_word(word, uzminetais_burts):
            print("Apsveicam, jūs uzvarējāt!")
            break

    while True:
        play_again = input("Vai vēlaties spēlēt velreiz? (jā/nē): ").lower()#Piedāvā spēlēt vēlreiz 
        if play_again == "jā":
            hangman()
        elif play_again == "nē":
            print("Paldies par spēli!")
            break
        else:
            print("Lūdzu ievadiet 'jā' vai 'nē'")
hangman()