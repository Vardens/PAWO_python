
'''
Created on 26-03-2014

@author: Vardens
'''


def redukcja_dodawaj_odejmuj(zadanie):
    nie_skonczone = True
    
    while(nie_skonczone):
        nie_cyfra = -1
        poczatek_dzialania = False
        ''' znak_start czynnik_A znak_middle czynnik_B znak stop'''
        znak_start = 0
        znak_middle = 0
        typ = '+' #okreslenie typu operacji- startuje od +
        
    
        for i, znak in enumerate(zadanie): 
             
            if(znak=='-' and i == 0):
                continue
            
            if i > 0:
                if (znak == '-') and (not zadanie[i-1].isdigit()):
                    continue
            
            if znak == '.': #ominięcie liczb dziesietnych
                continue
            
            #jezeli mam + to szukam pierwszego czynnika
            if ((znak == '+') or (znak == '-')) and (not poczatek_dzialania):
                typ = znak                          #ostatecznie ustalam typ dzialania
                czynnik_A = zadanie[nie_cyfra+1:i]  # zapamietuje wartosc pierwszego czynnika
                poczatek_dzialania = True           # zaczalem wykonywac dzialanie
                znak_start = nie_cyfra+1
                znak_middle = i
                continue
                
                
            if (not znak.isdigit()) and (not poczatek_dzialania):  # jeżeli mam juz dzialanie, to zapamiętuje gdzie kończy sie 1. czynnik
                nie_cyfra = i # bym wiedzial gdzie sie cofnac szukajac czynnika A
                continue
            
            if poczatek_dzialania == True and (not znak.isdigit()): #gdy znalazlem kolejny znak
                czynnik_B = zadanie[znak_middle + 1:i]
                #if zadanie[znak_start]=='-':
                #   czynnik_A='-'.join(czynnik_A)
                
                if typ == '+':
                    zadanie = zadanie[0:znak_start] + dodaj(czynnik_A, czynnik_B) + zadanie[i:]
                else:
                    zadanie = zadanie[0:znak_start] + odejmij(czynnik_A, czynnik_B) + zadanie[i:]
               
                break   #po zwinieciu jednego mnozenia (dzielenia) zacnzij od nowa
                        #strasznie obliczeniochłonne, praktycznie n^2, ale... nie mam lepszego pomysłu
                
        if znak == '=': #zakończenie while'a
            nie_skonczone = False
    return zadanie
            
            
def dodaj(a, b):

    wynik = float(a) + float(b)
    wynik=obcinacz(wynik)
    return wynik
           
def odejmij(a, b):    
    wynik = float(a) - float(b)
    wynik=obcinacz(wynik)
    return wynik

def obcinacz(liczba): #upiększa wygląd wyniku
    if((liczba-int(liczba))>0):
        return str("{0:.3f}".format(liczba))                
    else:
        return str("{0:.0f}".format(liczba))
    
if __name__=="__main__":
    print(redukcja_dodawaj_odejmuj("1+2*3+4+5*2-2-10*2+5="))