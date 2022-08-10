class Dreptunghi:
    lungime = 1
    latime = 1
    culoare = "verde"

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        return(f"Dreptunghi de culoare {self.culoare}, L: {self.lungime}, l: {self.latime}")

    def aria(self):
        arie_drept = self.lungime * self.latime
        return(f"aria: {arie_drept}")

    def perimetru(self):
        perim_drept = 2 * (self.lungime + self.latime)
        return(f"perimetru: {perim_drept}")

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare
        return(noua_culoare)

dreptunghi1 = Dreptunghi(4, 2, "galben")
print(dreptunghi1.descriere())
print(dreptunghi1.aria())
print(dreptunghi1.perimetru())
print(dreptunghi1.schimba_culoare("gri"))
print(dreptunghi1.descriere())