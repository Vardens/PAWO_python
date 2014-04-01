'''
Modul zawierajacy gre master mind
'''
import random

def start():
    '''Glowna funkcja modulu'''
    board = []
    for element in range(0, 4):
        board.append(random.choice(range(0, 6)))
    print "Master mind"
    print "Masz 10 prob na odgadniecie sekwencji 4 cyfr 0-5"
    print "Cyfry podawaj po kolei oddzielajac spacjami"
    for proba in range(1, 11):
        print ' '.join(["Proba", str(proba)])
        while 1:
            wejscie = raw_input("Podaj ciag: ")
            wejscie = wejscie.split()
            wejscie_int = []
            if len(wejscie) == 4:
                for element in wejscie:
                    try:
                        element_int = int(element)
                    except ValueError:
                        break
                    if element_int < 0 or element_int > 5:
                        break
                    wejscie_int.append(element_int)
                else:
                    break
            print "Podano niepoprawny ciag, sprobuj jeszcze raz\n"
        dobra_pozycja = 0
        dobry_kolor = 0
        kopia_board = board[:]
        for index in range(4):
            if wejscie_int[index] == kopia_board[index]:
                dobra_pozycja += 1
                wejscie_int[index] = -1
                kopia_board[index] = -1
        if dobra_pozycja < 4:
            for index in range(4):
                if wejscie_int[index] != -1:
                    if wejscie_int[index] in kopia_board:
                        dobry_kolor += 1
                        kopia_board.remove(wejscie_int[index])
        else:
            break
        print ' '.join([str(dobra_pozycja), " elementow na dobrej pozycji"])
        print ' '.join([str(dobry_kolor),
            " elementow o dobrym kolorze, ale na zlej pozycji"])
    else:
        print "Przegrales!\n"
        return
    print "Wygrales!\n"
    return
if __name__ == '__main__':
    start()
