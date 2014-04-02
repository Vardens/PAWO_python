'''
Created on 26-03-2014

@author: Vardens
'''
import unittest
from dodawaj_odejmuj import  redukcja_dodawaj_odejmuj

class Test_dodawaj_odejmuj(unittest.TestCase):


    def test_tylko_mnozenie(self):
        # ARANGE
        wejscie="1*2*3*4*5*6="
        oczekiwane = "1*2*3*4*5*6="
        
        # ACT
        wynik=redukcja_dodawaj_odejmuj(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_tylko_dodawanie(self):
        # ARANGE
        wejscie="1+2+3+4+5="
        oczekiwane = "15="
        
        # ACT
        wynik=redukcja_dodawaj_odejmuj(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
    def test_tylko_odejmowanie(self):
        # ARANGE
        wejscie="1-2-3-4="
        oczekiwane = "-8="
        
        # ACT
        wynik=redukcja_dodawaj_odejmuj(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_minus_z_przodu(self):
        # ARANGE
        wejscie="-1-2+3-4="
        oczekiwane = "-4="
        
        # ACT
        wynik=redukcja_dodawaj_odejmuj(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
         
    def test_minus_z_przodu2(self):
        # ARANGE
        wejscie="-100-2+3-4="
        oczekiwane = "-103="
        
        # ACT
        wynik=redukcja_dodawaj_odejmuj(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
  
    def test_dodawanie_mnozenie(self):
        # ARANGE
        wejscie="1+2*3+4+5*2-2-10*2+5="
        oczekiwane = "3*12*-10*7="
        
        # ACT
        wynik=redukcja_dodawaj_odejmuj(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)  
    
               

if __name__ == "__main__":
   
    unittest.main()