"""Esercizio 1
lista1 = [4.29, 3.9, 3.783, 3.9, 4.095]
lista2 = [3.12, 3.112, 3.12, 3.847, 3.081, 3.042, 3.742]
"""
import numpy as np
import math as math

class TestIpotesi():
    def showLista1 (self, lista):
        print("lista1:", lista)
        return lista

    def showLista2 (self, lista):
        print("lista2:", lista)
        return lista

    def showMedia1(self, lista):
        media = np.mean(lista)
        print("media", media)
        return media

    def showMedia2(self, lista):
        media = np.mean(lista)
        print("media", media)
        return media        

    def showDeviazStand1(self, lista):
        devStandard = np.std(lista)
        print("deviazione standard1:", devStandard)
        return devStandard

    def showDeviazStand2(self, lista):
        devStandard = np.std(lista)
        print("deviazione standard2:", devStandard)
        return devStandard   

    def showDevianza1(self, lista, media):
        scarti_quadrati1 = (lista - media)**2
        devianza = np.sum(scarti_quadrati1)
        print("devianza1:", devianza)
        return devianza

    def showDevianza2(self, lista, media):
        scarti_quadrati2 = (lista - media)**2
        devianza = np.sum(scarti_quadrati2)
        print("devianza2:", devianza)
        return devianza

    def showVarianzaPonderata(self, dev1, dev2, lista1, lista2):
        S_pooled = (dev1 + dev2)/(len(lista1)  + len(lista2))
        print("S_pooled", S_pooled)
        return S_pooled
  
    def showTest_T(self, media1, media2, S_pooled, lista1, lista2):
        numeratore = (media1 - media2)
        l1 = 1/len(lista1)
        l2 = 1/len(lista2)
        gradi_di_liberta = len(lista1) + len(lista2) - 2
        denominatore = math.sqrt(S_pooled * (l1 + l2))
        t_student = numeratore/denominatore
        print("t student:", t_student)
        print("Gradi di liberta:", gradi_di_liberta)
        return t_student
         

#lista1 = [4.29, 3.9, 3.783, 3.9, 4.095]
#lista2 = [3.12, 3.112, 3.12, 3.847, 3.081, 3.042, 3.742]
#lista1 = [25, 30, 21, 26, 24, 22, 27, 29, 22, 24]
#lista2 = [24, 28, 20, 31, 22, 23, 21, 28, 21, 23]
#lista1 = [639, 646, 650, 641, 641, 637, 659, 650, 640, 635]
#lista2 = [650, 633, 632, 637, 642, 638, 640, 634, 626, 636, 640]
lista1 = [11.8, 11.8, 9.5, 8.2, 8.1, 7.6, 7.1, 6.8, 6.5, 6.3, 6.2, 6.2, 5.9,
          5.9, 5.7, 5.39, 5.2, 5.1, 5,5, 4.8, 4.8, 4.7, 4.6, 3.98, 4.3, 3.9, 3.9 ]
lista2 = [43.8, 8.71, 5.9, 4.9, 4.3, 4.1, 4.1, 4.0, 3.9, 3.9, 3.9, 3.7, 3.6, 
          3.4, 3.4, 3.3, 2.9, 2.5, 2.1, 2.5, 2.1, 2.1, 2.1, 2, 1.8, 1.6]

test1 = TestIpotesi()
test1.showLista1(lista1)
test1.showLista2(lista2)

test1.showMedia1(lista1)
test1.showMedia2(lista2)

test1.showDeviazStand1(lista1)
test1.showDeviazStand2(lista2)

showDevianza1 = test1.showDevianza1(test1.showLista1(lista1), test1.showMedia1(lista1))
showDevianza2 = test1.showDevianza2(test1.showLista2(lista2), test1.showMedia2(lista2))

varianza_ponderata = test1.showVarianzaPonderata(showDevianza1, showDevianza2, test1.showLista1(lista1), test1.showLista2(lista2))

test1.showTest_T(test1.showMedia1(lista1), test1.showMedia2(lista2), varianza_ponderata, lista1, lista2)






