import random

kartu_remi = ["Ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
deck = []

def start():
    if not deck:
        nilai = 1
        for kartu in kartu_remi:
            for i in range(4):
                deck.append([kartu, nilai])
            nilai = nilai + 1
        random.shuffle(deck)

    score = 0
    kartu1 = deck.pop(0)

    while True:
        print("-------~-------~-------\nKartu yang terbuka adalah kartu", kartu1[0])

        if not deck:
            print("Score akhir:",score)
            while True:
                restart = input("Selamat! Deck kartu sudah habis, restart? (y/n): ")
                if restart not in ["y","n"]:
                    print("Anda salah input, silakan ulang.")
                else:
                    break
            if restart == "y":
                return start()
            elif restart == "n":
                break

        kartu2 = deck.pop(0)
        print("Kartu tertutup sudah diambil")

        while True:
            guess = input("upper or lower?: ")
            if guess not in ["upper","lower"]:
                print("Anda salah input, silakan ulang.")
            else:
                break
        
        if guess == "upper":
            if kartu2[1] > kartu1[1]:
                print("Kartu tertutup adalah kartu " + str(kartu2[0]) + ". Jawaban anda benar.")
                score +=1
            elif kartu2[1] < kartu1[1]:
                print("Kartu tertutup adalah kartu " + str(kartu2[0]) + ". Jawaban anda salah.\nScore Akhir: " + str(score))
                while True:
                    restart = input("Restart? (y/n): ")
                    if restart not in ["y","n"]:
                        print("Anda salah input, silakan ulang.")
                    else:
                        break
                if restart == "y":
                    score = 0
                elif restart == "n":
                    break
            elif kartu2[1] == kartu1[1]:
                print("Nilai kartu sama, kita lanjutkan")
        
        elif guess == "lower":
            if kartu2[1] < kartu1[1]:
                print("Kartu tertutup adalah kartu " + str(kartu2[0]) + ". Jawaban anda benar.")
                score +=1
            elif kartu2[1] > kartu1[1]:
                print("Kartu tertutup adalah kartu " + str(kartu2[0]) + ". Jawaban anda salah.\nScore Akhir: " + str(score))
                while True:
                    restart = input("Restart? (y/n): ")
                    if restart not in ["y","n"]:
                        print("Anda salah input, silakan ulang.")
                    else:
                        break
                if restart == "y":
                    score = 0
                elif restart == "n":
                    break
            elif kartu2[1] == kartu1[1]:
                print("Nilai kartu sama, kita lanjutkan")
        
        kartu1 = kartu2

start()