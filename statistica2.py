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



    
