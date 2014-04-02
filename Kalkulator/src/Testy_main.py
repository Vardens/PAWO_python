'''
Created on 27-03-2014

@author: Vardens
'''
import unittest
from Kalkulator import main


class Test_main(unittest.TestCase):

    def test_dodawanie_odejmowanie_mnozenie(self):
        
        # ARANGE
        wejscie="1+2*3*4-5*6"
        oczekiwane = wejscie+"=-5"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_ujemna_z_przodu(self):
        
        # ARANGE
        wejscie="-1-4-5-3"
        oczekiwane = wejscie+"=-13"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_ujemna_z_przodu_mnozenie(self):
        
        # ARANGE
        wejscie="-1*6*4+5*9+3"
        oczekiwane = wejscie+"=24"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
                
    def test_mnozenie_ujemna(self):
        
        # ARANGE
        wejscie="5+5*-2+3"
        oczekiwane = wejscie+"=-2"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
                    
    def test_mnozenie_ujemna_po_dodawaniu(self):
        
        # ARANGE
        wejscie="5+-5*2+3"
        oczekiwane = wejscie+"=-2"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_dzielenie_przez_zero(self):
        
        # ARANGE
        wejscie="5+3/0-4"
        oczekiwane = wejscie+"=Error"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
    def test_odejmowanie_ujemnej(self):
        
        # ARANGE
        wejscie="15--5"
        oczekiwane = wejscie+"=20"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_dzialanie_Damiana(self):
        
        # ARANGE
        wejscie="0.5/-1"
        oczekiwane = wejscie+"=-0.500"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_dzielenie_wielkokrotne(self):
        
        # ARANGE
        wejscie="1/2*3/5"
        oczekiwane = wejscie+"=0.300"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_bledny_poczatek(self):
        
        # ARANGE
        wejscie="+5-6-1"
        oczekiwane = wejscie+"Error"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_male_liczby(self):
        
        # ARANGE
        wejscie="0.001/1000"
        oczekiwane = wejscie+"=0.000"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_zakonczenie(self):
        
        # ARANGE
        wejscie="x"
        oczekiwane ="x"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
    
    def test_nawiasów(self):
        
        # ARANGE
        wejscie="(2+3)*2"
        oczekiwane =wejscie+"=10"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
    def test_nawiasy_zagniezdzone(self):
        
        # ARANGE
        wejscie="2*(3+(2+4/0.5)/5-(-3))"
        oczekiwane =wejscie+"=16"
        
        # ACT
        wynik=main(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()