class Best:

    def __init__(self, numP):
        
        self.parametros = [0] * numP
        self.trueFit = None
        self.fitness = None
        self.rfitness = None
        self.treinos = None
        
    def clone(self, parametros):
            
        for i in range(0,len(self.parametros)):
            
            self.parametros[i] = parametros[i]
