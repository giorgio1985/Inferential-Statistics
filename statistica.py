import numpy as np #Approccio metodologico senza utilizzo delle librerie
class HypotesisTest():
    def calcolaMedia1(self, m1):
        media1 = np.mean(m1);
        return media1
    def calcolaMedia2(self, m2):
        media2 = np.mean(m2);
        return media2
    def calcolaVarianza1(self, m1, g1):
        i = 0;
        j = 0;
        for x in g1:
            i = i + (x*x)
            j = j + 1
        correzione1 = -m1*m1*j
        varianzaCamp1 = (i + correzione1)/(j-1)
        print(f" i: {i}, j: {j}, correzione1: {correzione1}, varianzaCamp1: {varianzaCamp1}");
        return varianzaCamp1;
    def calcolaVarianza2(self, m2, g2):
        i = 0;
        j = 0;
        for x in g2:
            i = i + (x*x)
            j = j + 1
        correzione2 = -m2*m2*j
        varianzaCamp2 = (i + correzione2)/(j-1)
        print(f" i: {i}, j: {j}, correzione2: {correzione2}, varianzaCamp2: {varianzaCamp2}");        
        return varianzaCamp2;
    def varianzaCongiunta(self, v1, v2, g1, g2):
        campione1Corretto = len(g1) - 1
        campione2Corretto = len(g2) - 1
        VCongiunta = ((campione1Corretto*v1) + (campione2Corretto*v2))/(campione1Corretto + campione2Corretto)
        print(VCongiunta)
        return VCongiunta;
    def calcolaTStudent(self, m1, m2, VCongiunta, g1, g2):
        denominatore = (VCongiunta/len(g1)  + VCongiunta/len(g2))
        TStudent = (m1-m2)/(pow(denominatore, 0.5))
        print(TStudent)
        
g1 = [0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0, 2]  
g2 = [1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4]
ht = HypotesisTest()
ht.calcolaMedia1(g1)
ht.calcolaMedia2(g2)
ht.calcolaVarianza1(ht.calcolaMedia1(g1), g1)
ht.calcolaVarianza2(ht.calcolaMedia2(g2), g2)
vg = ht.varianzaCongiunta(ht.calcolaVarianza1(ht.calcolaMedia1(g1), g1), ht.calcolaVarianza2(ht.calcolaMedia2(g2), g2), g1, g2)
ht.calcolaTStudent(ht.calcolaMedia1(g1), ht.calcolaMedia2(g2), vg, g1, g2)

class Madre ():
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
class Figlia(Madre):
    def __init__(self, nome, cognome, legame):
        super().__init__(nome, cognome)
        self.legame = legame
    def calcolaFiglia(self):
        print(f"nome: {self.nome}, cognome: {self.cognome}, legame: {self.legame}" )
class Figlio (Madre):
    def __init__(self, nome, cognome, legame):
        super().__init__(nome, cognome)
        self.legame = legame
    def calcolaFiglio(self):
        print(f"nome: {self.nome}, cognome: {self.cognome}, legame: {self.legame}")
        
figlio1 = Figlia("Giorgia","Adonoo", "Figlia")
figlio2 = Figlio("Giorgio","Adonoo", "Figlio")

figlio1.calcolaFiglia()
figlio2.calcolaFiglio()


import numpy as np
class Inferenza():
    def __init__(self, lista):
        self.lista = lista;
    def showList(self):
        print(lista)
        return self.lista
        
class Media(Inferenza):
    def __init__(self, lista):
       super().__init__(lista)
      #self.media= media
    def calcolaMedia(self):
        self.media = np.mean(lista)
        print(f"media: {self.media}" )
        return self.media
        
class DevStandard(Inferenza):
    def __init__(self, lista):
        super().__init__(lista)
    def calcolaDevStd(self):
        self.deviazStd = np.std(lista)
        print("dev standard:",  self.deviazStd*self.deviazStd)
        return self.deviazStd*self.deviazStd
        
class TestIpotesi ():
    def calcolaIpotesi(self,media, deviazioneStd, lista):
        self.varianza = deviazioneStd
        self.campione = len(lista)
        self.denominatore = self.varianza/self.campione
        self.h = (media - 4)/(pow(self.denominatore, 0.5))
        print(self.h)
        

lista = [1.1,3.1,4.2,4.6,5.0,5.2,5.3,6.5,8.4,9.6]
inf = Inferenza(lista)
inf.showList()

med = Media(lista)
med.calcolaMedia()

devst = DevStandard(lista)
devst.calcolaDevStd()

h = TestIpotesi()
h.calcolaIpotesi(med.calcolaMedia(), devst.calcolaDevStd(), inf.showList())



    
