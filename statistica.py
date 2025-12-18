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
        gradiDiLiberta = campione1Corretto + campione2Corretto
        VCongiunta = ((campione1Corretto*v1) + (campione2Corretto*v2))/(campione1Corretto + campione2Corretto)
        print('VCongiunta', VCongiunta)
        print('gradiDiLiberta', gradiDiLiberta)
        return VCongiunta;

    def calcolaTStudent(self, m1, m2, VCongiunta, g1, g2):
        denominatore = (VCongiunta/len(g1)  + VCongiunta/len(g2))
        TStudent = (m1-m2)/(pow(denominatore, 0.5))
        print('TStudent', TStudent)
        
#g1 = [25, 38, 21, 26, 24, 22, 27, 29,22, 24]  
g2 = [24, 28, 20, 31, 22, 23, 21, 28, 21, 23, 24, 28, 20, 31, 22, 23, 21, 28, 21, 23]
g1 = [0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0, 2]  
#g2 = [1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4]
 
ht = HypotesisTest()
ht.calcolaMedia1(g1)
ht.calcolaMedia2(g2)
ht.calcolaVarianza1(ht.calcolaMedia1(g1), g1)
ht.calcolaVarianza2(ht.calcolaMedia2(g2), g2)
vg = ht.varianzaCongiunta(ht.calcolaVarianza1(ht.calcolaMedia1(g1), g1), ht.calcolaVarianza2(ht.calcolaMedia2(g2), g2), g1, g2)
ht.calcolaTStudent(ht.calcolaMedia1(g1), ht.calcolaMedia2(g2), vg, g1, g2)
