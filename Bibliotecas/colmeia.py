from random import *
import sys
import copy
sys.path.insert(0, 'C:/Users/jramo/Desktop/Trabalho de IA/Bibliotecas')

import Setup
import EstruturaABC
import Best

class Colmeia:
    
    def __init__(self):
        
        self.setup = Setup.Setup()
        self.size = 40
        self.foodNumber = int(self.size/2)
        self.limit = 100
        self.maxCiclos = 3500
        self.numParametros = self.setup.getNum()
        self.lInf = self.setup.lInf
        self.lSup = self.setup.lSup
        self.runtime = 30
        self.nectar = [0] * self.foodNumber
        self.empregadas = [0] * self.foodNumber 
        self.observadoras = [0] * self.foodNumber 
        self.bestResult = Best.Best(self.numParametros)
        
        for i in range(0,self.foodNumber):
            self.nectar[i] = EstruturaABC.EstruturaABC(self.numParametros)
            self.empregadas[i] = EstruturaABC.EstruturaABC(self.numParametros)
            self.observadoras[i] = EstruturaABC.EstruturaABC(self.numParametros)
            
    def inicializar(self):
        
        for i in range(0,self.foodNumber):
            for j in range(0,self.numParametros):
                self.nectar[i].parametros[j] = self.aleatorio(self.lInf, self.lSup)
            
            self.empregadas[i].clone(self.nectar[i].parametros)
            self.observadoras[i].clone(self.nectar[i].parametros)
            self.bestResult.clone(self.nectar[0].parametros)
            
            self.nectar[i].calcTfitness()
            self.nectar[i].calcFitness()
            
            self.empregadas[i] = copy.deepcopy(self.nectar[i])
            self.observadoras[i] = copy.deepcopy(self.nectar[i])
            
        
        self.bestResult = copy.deepcopy(self.nectar[0])
        
        
    def imprimirResultado(self):
        
        print("\n\n\nO valor das variáveis são:" )
        self.bestResult.parametros = [ '%.2f' % elem for elem in self.bestResult.parametros ]
        print(self.bestResult.parametros)

        print("\n\nResultado obtido: ")    
        print(round(self.bestResult.trueFit,4))
        print("\n-------------------------------\n")
        return "Fim de Programa"
            
    def aleatorio(self, min, max):
        
        return (min + (max - min) * random())
    
    def memorizar(self):
        
        for i in range(0, self.foodNumber):
            
            if self.nectar[i].trueFit < self.bestResult.trueFit:
                
                self.bestResult.clone(self.nectar[i].parametros)
                self.bestResult.trueFit = self.nectar[i].trueFit
            
                
    def CalcProbabilidade(self):
        
        maxFit = self.nectar[0].fitness
        
        for i in range(1,self.foodNumber):
            if (self.nectar[i].fitness > maxFit):
                maxFix = self.nectar[i].fitness

        for i in range(0,self.foodNumber):
            self.nectar[i].rfitness = (0.9*(self.nectar[i].fitness/maxFit)) + 0.1
            
    def enviarEmpregadas(self):
        
        for i in range(1,self.foodNumber):
            
            parametroAlterado = int(self.aleatorio(0,self.numParametros))
            k = None
            
            while(True):
                k = int(self.aleatorio(0,self.foodNumber))
                if(k != i):
                    break
            
            self.empregadas[i].clone(self.nectar[i].parametros)
            fi = self.aleatorio(-1,1)
            self.empregadas[i].parametros[parametroAlterado] = self.nectar[i].parametros[parametroAlterado] + fi *(self.nectar[i].parametros[parametroAlterado] - self.nectar[k].parametros[parametroAlterado])
            
            if(self.empregadas[i].parametros[parametroAlterado] > self.lSup):
                self.empregadas[i].parametros[parametroAlterado] = self.lSup
            
            if(self.empregadas[i].parametros[parametroAlterado] < self.lInf):
                self.empregadas[i].parametros[parametroAlterado] = self.lInf
                
            self.empregadas[i].calcTfitness()
            self.empregadas[i].calcFitness()
            
            if(self.empregadas[i].trueFit < self.nectar[i].trueFit):
                self.nectar[i] = copy.deepcopy(self.empregadas[i])
                self.nectar[i].treinos = 0
            
            else:
                self.nectar[i].treinos = self.nectar[i].treinos + 1
                
    def enviarObservadoras(self):
            
        t=0
        i=0
        
        while t < self.foodNumber:
            
            if (self.aleatorio(0,1) < self.nectar[i].rfitness):
                
                t = t + 1
                parametroAlterado = int(self.aleatorio(0,self.numParametros))
                
                while(True):
                    k = int(self.aleatorio(0,self.foodNumber))
                    if (k != i):
                        break
                    
                fi = self.aleatorio(-1, 1)
                self.observadoras[i].clone(self.nectar[i].parametros)
                self.observadoras[i].parametros[parametroAlterado] = self.nectar[i].parametros[parametroAlterado] + fi*(self.nectar[i].parametros[parametroAlterado] - self.nectar[k].parametros[parametroAlterado])
                
                if (self.observadoras[i].parametros[parametroAlterado] > self.lSup):
                    self.observadoras[i].parametros[parametroAlterado] = self.lSup
                
                if (self.observadoras[i].parametros[parametroAlterado] < self.lInf):
                    self.observadoras[i].parametros[parametroAlterado] = self.lInf
                
                self.observadoras[i].calcTfitness()
                self.observadoras[i].calcFitness()
                
                if (self.observadoras[i].trueFit < self.nectar[i].trueFit):
                    
                    self.nectar[i].clone(self.observadoras[i].parametros)
                    self.nectar[i].treinos = 0
                    self.nectar[i].trueFit = self.empregadas[i].trueFit
                    self.nectar[i].fitness = self.empregadas[i].fitness
                    
                else:
                    self.nectar[i].treinos = self.nectar[i].treinos + 1  
            
            i = i + 1
            if (i is self.foodNumber):
                i=0
                
    def enviarExploradora(self):
            
        indiceMaxTreino = 0
        
        for i in range(1, self.foodNumber):
            
            if(self.nectar[i].treinos > self.nectar[indiceMaxTreino].treinos):
                indiceMaxTreino = i
        
        if (self.nectar[indiceMaxTreino].treinos >= self.limit):
            
            for i in range(0,self.numParametros):
                R = self.aleatorio(0,1)
                self.nectar[indiceMaxTreino].parametros[i] = self.lInf + R*(self.lSup - self.lInf)
                
            self.nectar[indiceMaxTreino].treinos = 0;
            self.nectar[indiceMaxTreino].calcTfitness();
            self.nectar[indiceMaxTreino].calcFitness();
        
