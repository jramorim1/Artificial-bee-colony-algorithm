import Setup 
import time

class EstruturaABC:
   
    def __init__(self, numP):
        
         self.parametros = [0] * numP
         self.trueFit = 0;
         self.fitness = 0;
         self.rfitness = 0;
         self.treinos = 0;
         self.setup = Setup.Setup()

    def calcTfitness(self):
    
        self.trueFit = self.setup.calcTfitness(self.parametros) 
      

    def calcFitness(self):
        
        if(self.trueFit >= 0):
            self.fitness = (1 / (self.trueFit + 1))
        else:
            self.fitness = (1 + float(abs(self.trueFit)))

    def clone(self, parametros):

        for i in range(0,len(self.parametros)):
            
            self.parametros[i] = parametros[i]
            
