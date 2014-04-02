
import Wyjatki as Wyj
from mnoz_dziel import redukcja_mnoz_dziel
from dodawaj_odejmuj import redukcja_dodawaj_odejmuj
import re

#instrukcja
helper='''
Witam w Kalkulatorze Pythonek 1.1, przygotowanym przez Tomasza Szandała ;-)

Program wykonuje na razie podstawowe operacje: +, -, * i /.
Program obsługuje kolejność wykonywania działań, z uwzględnieniem nawiasów.
Sam dostosowuje typ liczb (int czy float) w zależności od potrzeb.

Przykłady uzycia (co wpisano => wynik):
1+2+3*4-10/5 => 1+2+3*4-10/5=13
5+-3 => 5+-3=2
1/8 => 1/8=0.125
100/3 => 100/3=33.333

Dodatkowo:
x- kończy pracę programu
help- wypisuje pomoc

'''


def sprawdzenie_zadania(zadanie):
    '''sprawdza czy dobrze podany input'''
    try:
        Wyj.czy_poprawne(zadanie)
        return True
    except Wyj.ZleDane as wyjatek:
        print(wyjatek)
    else:
        return False

def main(zadanie):
    
    if zadanie=='help':
        return helper
    if zadanie=='x':
        return 'x'
    #zapamiętanie oryginalnego wpisu
    oryginal=zadanie
    
    czy_poprawne=sprawdzenie_zadania(zadanie)
    if not czy_poprawne:
        return zadanie+"Error"
    
    zadanie=zadanie+'=' #pomoze mi znaleźć koniec
    #A teraz wyszukiwanie działań
    
    
    while True:
        regex=re.search(r'\(([+\-*\/.0-9]*)\)', zadanie)
        if regex==None:
            break
        regex=regex.group()
            
        wyrazenie=regex[1:-1]+"="
        
        wynik=redukcja_mnoz_dziel(wyrazenie)
        if wynik=="Error":
            return zadanie+"Error"
        wynik=redukcja_dodawaj_odejmuj(wynik)
        
        wynik=wynik[:-1]
        
        zadanie=re.sub(r'\(([+\-*\/.0-9]*)\)', wynik, zadanie, count=1)
        print(zadanie)
    
    
    wynik=redukcja_mnoz_dziel(zadanie)
    if wynik=="Error":
        return zadanie+"Error"
    wynik=redukcja_dodawaj_odejmuj(wynik)
    
    wynik=oryginal+"="+wynik[:-1]
        
        
    return wynik
    
if __name__=="__main__":
    while(True):
        zadanie=str(input("Podaj działanie do wykonania: "))
        wynik=main(zadanie)
        if(wynik=='Error'):
            pass
        elif(wynik=='x'):
            print("Dziękujemy za skorzystanie z programu!")
        else:
            print(wynik)
    
    
    
    