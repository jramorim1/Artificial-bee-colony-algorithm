import sys
sys.path.insert(0, 'C:/Users/jramo/Desktop/Trabalho de IA/Bibliotecas') #Alterar Caminho

import colmeia

bee = colmeia.Colmeia()
bee.inicializar()
bee.memorizar()

for i in range(0, bee.maxCiclos):
    bee.enviarEmpregadas()
    bee.CalcProbabilidade()
    bee.enviarObservadoras()
    bee.memorizar()
    bee.enviarExploradora()
    bee.memorizar()
    
    
print(bee.imprimirResultado())



