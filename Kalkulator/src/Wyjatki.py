# -*- coding: utf-8 -*-
import re
class ZleDane(Exception):
    
    def __init__(self, opis):
        Exception.__init__(self, opis)
        self.opis=opis
        
    def __str__(self):
        return self.opis

def czy_poprawne(zadanie):
    if zadanie=='':
        raise ZleDane("Podaj coś!")
    
    if (not zadanie[0].isdigit()):
        if (zadanie[0] == '-') or (zadanie[0] == '('):
            pass
        else:
            raise ZleDane("Wyrazenie nie moze zaczynac sie od: "+zadanie[0])
        
    if(not zadanie[-1].isdigit()):
        if(zadanie[-1]!=')') :
            raise ZleDane("Wyrazenie nie moza konczyc sie na: "+zadanie[-1]) 
        else:
            pass
    

    if zadanie.count('(') != zadanie.count(')'):
        raise ZleDane("Niewlasciwa ilość nawiasow!")
       
