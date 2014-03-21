#!/usr/bin/python 
import random
import string

__author__ = 'piotr'


def losuj_slowo():

    """
    Funkcja losuje 4 znaki, sposrod zbioru malych liter.
    Zwraca string zlozony z wylosowanych znakow.
    :rtype : str
    """

    slowo = ''
    for _ in range(4):
        slowo += random.choice(string.lowercase)

    return slowo


def sprawdz(temp, wzor):

    """
    Funkcja sluzy do oceny proby gracza.
    Porownywane sa odpowiadajace litery slowa.
    W przypadku, gdy znaki sa takie same do zlowa dopisywany jest ten znak.
    W przeciwnym razie do slowa dopisywana jest *.
    :rtype : str.
    """

    slowo = ''
    for j in range(4):
        if temp[j] == wzor[j]:
            slowo += wzor[j]
        else:
            slowo += '*'
    return slowo


if __name__ == '__main__':


    SZYFR = ""
    PROBY = 0
    PUNKTY = 0
    ODGADNIETE = 0
    RUNDY = 0
    AKTUALNE = False

    print "Witamy w grze Mastermind, gra polega na ogadywaniu szyfru \n"

    while 1:
        print "Podaj ile rund chcesz zagrac"
        RUNDY = input("-->")
        if RUNDY % 2 == 0:
            break
        else:
            print "Liczba nie jest parzysta, podaj jeszcze raz !"
            continue

    for i in range(RUNDY):
        SZYFR = losuj_slowo()
        print "Start runda :", (i + 1), "\n"

        while (PROBY < 8):
            print "Runda:", (i + 1)
            print "Proba:", PROBY
            print "Podaj swoj typ (4 znaki, male litery)"
            s = raw_input("-->")
            print s
            z = "****"

            if s.__len__() < 4:
                print "Wprowadzony szyfr jest zbyt krotki !\n"
                continue

            if s.__len__() > 4:
                print "Wprowadzony szyfr jest zbyt dlugi !\n"
                continue

            if s.islower() == 0:
                print "Nie zgadza sie wymagany typ znakow !\n"
                continue

            if s == SZYFR:
                print "Ogadles szyfr"
                ODGADNIETE += 0
                AKTUALNE = True
                break

            z = sprawdz(s, SZYFR)
            print "Ocena proby: ", z, "\n"
            PROBY += 1

        if AKTUALNE == False:
            print "W tej rundzie nie udalo Ci sie odgadnac szyfru, oto on: ", SZYFR

    PUNKTY += PROBY

print "Statystyki gracza: \n"

print "Liczba rozegranych rund     :", RUNDY, "."
print "Liczba uzyskanych punktow   :", PUNKTY, "."
print "Liczba odgadnietych szyforw :", ODGADNIETE, "."


