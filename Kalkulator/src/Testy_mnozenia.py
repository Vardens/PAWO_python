'''
Created on 26-03-2014

@author: Vardens
'''
import unittest
import mnoz_dziel as kolejka

class Test_mnoz_dziel(unittest.TestCase):
    
    def test_mnozenie(self):
        # ARANGE
        wejscie="1*2*3*4*5*6="
        oczekiwane = "720="
        
        # ACT
        wynik=kolejka.redukcja_mnoz_dziel(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_dzielenie(self):
        # ARANGE
        wejscie="1024/256/2/2="
        oczekiwane = "1="
        
        # ACT
        wynik=kolejka.redukcja_mnoz_dziel(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)

    def test_redukcja_mnoz(self):
        
        # ARANGE
        wejscie="1+2*3*4-5*6="
        oczekiwane = "1+24-30="
        
        # ACT
        wynik=kolejka.redukcja_mnoz_dziel(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_mnoz_dziel_mieszanie(self):
        # ARANGE
        wejscie="1*4/2*5*3/15="
        oczekiwane = "2="
        
        # ACT
        wynik=kolejka.redukcja_mnoz_dziel(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_mnoz_dziel_dodawanie(self):
        # ARANGE
        wejscie="1*2+4/2*5*3-60/15="
        oczekiwane = "2+30-4="
        
        # ACT
        wynik=kolejka.redukcja_mnoz_dziel(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_mnoz_liczby_ujemne(self):
        # ARANGE
        wejscie="4+1*2*-3="
        oczekiwane = "4+-6="
        
        # ACT
        wynik=kolejka.redukcja_mnoz_dziel(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
    def test_zacznij_od_ujemnej(self):
        # ARANGE
        wejscie="-3*2*5+1="
        oczekiwane = "-30+1="
        
        # ACT
        wynik=kolejka.redukcja_mnoz_dziel(wejscie)
        
        # ASSERT
        self.assertEqual(wynik, oczekiwane)
        
if __name__ == "__main__":
    unittest.main()
