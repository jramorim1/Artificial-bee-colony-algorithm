from random import *
import time

class Setup:
    
    def __init__(self):
        
        self.numParametros = 2
        self.lInf = -30
        self.lSup = 30

    def calcTfitness(self, p):
        
        
        x = p[0]
        y = p[1]
        
        #Funções para teste
        return (x*x - 10 - 41*x) #Mínimo Aproximadamente: -430
        #return (x*x*x*x - 10 - 41*x) #Mínimo Aproximadamente: -76
        #return (10 - 2*x + x*x) #Mínimo: 9
        #return (x*x + y*y) #Mínimo 0
        

    def getNum(self):
        
        return self.numParametros
        
