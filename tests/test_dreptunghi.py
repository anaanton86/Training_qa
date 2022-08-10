from app2.dreptunghi import Dreptunghi
# import pytest

class TestDreptunghi:
    def setup_method(self):
        print("se executa la inceput")
        self.drept1 = Dreptunghi(2, 3, "alb")

    def teardown_method(self):
        print("se executa la final")

    def test_aria(self):
        assert self.drept1.aria() == 'aria: 6', "aria is not working"

    def test_perimetru(self):
        assert self.drept1.perimetru() == 'perimetru: 10', "perimetru is not working"

    # def schimba_culoare(self, noua_culoare):
    #     assert self.drept1.schimba_culoare() == noua_culoare, "not working"