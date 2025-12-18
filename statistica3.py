"""Esercizio 1
Sulla base dei seguenti valori ottenuti su un campione casuale proveniente da una popolazione normale
1.1 3.1 4.2 4.6 5.0 5.2 5.3 6.5 8.4 9.6
verificare l’ipotesi H0:mu =4 al livello di significatività mu=0.01
"""
import numpy as np
import math as math

class TestIpotesi():
    def showLista (self, lista):
        print("lista:", lista)

    def showMedia(self, lista):
        media = np.mean(lista)
        print("media", media)
        return media

    def showVarianza(self, lista):
        devStandard = np.std(lista)
        print("deviazione standard:", devStandard)
        return devStandard

    def showVarianzaCorretta(self, lista):
        devStandardCorretta = np.std(lista, ddof=1)
        print("deviazione standard corretta:", devStandardCorretta)
        print("varianza corretta:", devStandardCorretta*devStandardCorretta)
        return devStandardCorretta

    def showStatisticaTest(self, lista, media, mediaPopolazione, devStandardCorretta):
        numeratore = media - mediaPopolazione
        denominatore = math.sqrt(devStandardCorretta*devStandardCorretta/len(lista))
        t = numeratore/denominatore
        print("statistica test:", t)
        return t


    

lista1 = [1.1, 3.1, 4.2, 4.6, 5.0, 5.2, 5.3, 6.5, 8.4, 9.6]
mediaPopolazione = 4

test1 = TestIpotesi()
test1.showLista(lista1)
test1.showMedia(lista1)
test1.showVarianza(lista1)
test1.showVarianzaCorretta(lista1)
test1.showStatisticaTest(lista1, test1.showMedia(lista1), mediaPopolazione, test1.showVarianzaCorretta(lista1))






