# -*- coding: utf-8 -*-
'''
Created on 26-03-2014

@author: Vardens
'''


def redukcja_mnoz_dziel(zadanie):
    nie_skonczone = True
    
    while(nie_skonczone):
        
        nie_cyfra = -1
        poczatek_dzialania = False
        ''' znak_start czynnik_A znak_middle czynnik_B znak stop'''
        znak_start = 0
        znak_middle = 0
        typ = '*'               #okreslenie typu operacji- startuje od *
    
    
        for i, znak in enumerate(zadanie):  
            if znak == '.':         #ominiecie liczb dziesietnych
                continue
            if i > 0:
                if (znak == '-') and (not zadanie[i-1].isdigit()):
                    continue
            
            '''jezeli mam * to szukam pierwszego czynnika'''
            if ((znak == '*') or (znak == '/')) and (not poczatek_dzialania):
                typ = znak         #ostatecznie ustalam typ dzialania
                czynnik_A = zadanie[nie_cyfra+1:i]  # zapamietuje wartosc pierwszego czynnika
                poczatek_dzialania = True  # zaczalem wykonywac dzialanie
                znak_start = nie_cyfra+1
                znak_middle = i
                continue               
                
            if (not znak.isdigit()) and (not poczatek_dzialania):  # jezeli mam juz dzialanie, to zapami�tuje gdzie ko�czy sie 1. czynnik
                nie_cyfra = i # bym wiedzial gdzie sie cofnac szukajac czynnika A
                continue
            
            if poczatek_dzialania == True and (not znak.isdigit()): #gdy znalazlem kolejny znak
                czynnik_B = zadanie[znak_middle + 1:i]
                if typ == '*':
                    zadanie = zadanie[0:znak_start] + mnoz(czynnik_A, czynnik_B) + zadanie[i:]
                else:
                    if float(czynnik_B)==0:
                        return "Error"
                    else:
                        zadanie = zadanie[0:znak_start] + dziel(czynnik_A, czynnik_B) + zadanie[i:]
                break #po zwinieciu jednego mnozenia (dzielenia) zacnzij od nowa
            #strasznie obliczeniochłonne, praktycznie n^2, ale... nie mam lepszego pomysłu
                
        if znak == '=':
            nie_skonczone = False
            
    return zadanie
            
            
def mnoz(a, b):

    wynik = float(a) * float(b)
    wynik=obcinacz(wynik)
    return wynik
           
def dziel(a, b):    
    wynik = float(a) / float(b)
    wynik=obcinacz(wynik)
    return wynik

def obcinacz(liczba): #upieksza wyglad wyniku
    if(abs((liczba-int(liczba)))>0):
        return str("{0:.3f}".format(liczba))                
    else:
        return str("{0:.0f}".format(liczba))
            
if __name__ == "__main__":
    print(redukcja_mnoz_dziel("0.5/-1=")) 
    
    
    
    
