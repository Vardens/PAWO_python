#!/usr/bin/python
"Prosty Kalkulator"
__author__ = 'Piotr Chmiel'

def wykonaj_operacje(dzialanie, wartosc_a, wartosc_b):
    """
    Funkcja wykonuje zadana operacje
    :rtype : float
    """

    if dzialanie == 'dodawanie':
        wynik = wartosc_a + wartosc_b
        return wynik
    elif dzialanie == 'odejmowanie':
        wynik = wartosc_a - wartosc_b
        return wynik
    elif dzialanie == 'mnozenie':
        wynik = wartosc_a * wartosc_b
        return wynik
    elif dzialanie == 'dzielenie':
        if wartosc_b == 0:
            return "Nie mozna dzielic przez 0 !"
        wynik = wartosc_a / wartosc_b
        return wynik

def save(nazwa, dane):

    "Funkcja wykonuje zapis do pliku o zadanej nazwie"

    logfile = open(nazwa,'w')
    logfile.write(dane)
    logfile.close()

    print "Zapis do pliku zakonczony powodzeniem !"

def main():

    "Funkcja glowna"

    operacje = ['dodawanie', 'odejmowanie', 'mnozenie', 'dzielenie', 'save', 'exit']
    log = ''
    nazwa_operacji = ''
    operand_a = 0
    operand_b = 0

    print 'Witamy w programie calc ! '
    print 'Dostepne sa nastepujace operacje:'
    print operacje
    print 'Operacje matematyczne wymagaja podania dwoch liczb'
    print 'Operacja zapisu wymaga podania nazwy pliku'
    print 'Pamietaj dane oddziel spacjami'
    print 'Format: dzialanie liczba 1 liczba2'


    while 1:

        print "\nPodaj operacje do wykonania: "

        dane = raw_input('-->')
        podzielone_dane = dane.split(' ', 2)
        nazwa_operacji = str(podzielone_dane[0])

        if nazwa_operacji not in operacje:
            print "Nie ma takiej operacji ! Sproboj ponownie \n"
            continue
        else:
            if nazwa_operacji == 'exit':
                print "\nKoniec programu\n"
                break

            elif nazwa_operacji == 'save':
                if len(podzielone_dane) != 2:
                    print "Nieprawidlowa ilosc danych dla operacji save ! Sprobuj ponownie !\n"
                    continue
                if log == '':
                    print "Nie ma czego zapisywac ! Najpierw wykonaj jakies operacje\n"
                    continue

                nazwa_pliku = podzielone_dane[1]

                sprawdz = nazwa_pliku.split('.', 1)

                if len(sprawdz) == 2:
                    if (sprawdz[1] == 'txt'):
                        save(nazwa_pliku, log)
                        continue
                else:
                    nazwa_pliku += '.txt'
                    save(nazwa_pliku, log)
                    continue
            else:
                if len(podzielone_dane) != 3:
                    print "Nieprawidlowa ilosc danych ! Sprobuj ponownie !\n"
                    continue

                try:
                    operand_a = float(podzielone_dane[1])
                    operand_b = float(podzielone_dane[2])

                except ValueError:
                    print "Dane nie sa liczbami ! Sprobuj ponownie !\n"
                    continue

                wynik = wykonaj_operacje(nazwa_operacji, operand_a, operand_b)
                log += str(dane)
                log += str(' ')
                log += str(wynik)
                log += '\n'

                print "Wynik :", wynik


if __name__ == '__main__':

    main()
