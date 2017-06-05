#heurisitca grasp para sat 
from files import heuristicaksat
from files import generadorksat
#generar una nueva instancia
generadorksat.generarkSat(100, 300, False)
#resolver por medio de grasp con valores alpha de 0.1, 0.3 y 0.5
alpha = 0.1
ite = 30
bs, be, fi, sl = heuristicaksat.heuristicgrasp('files/cnft.txt', ite, alpha)
print('a: ', str(alpha), 'best fo value: ' , be, 'iteration:  ', fi)

alpha = 0.3
bs, be, fi, sl = heuristicaksat.heuristicgrasp('files/cnft.txt', ite, alpha)
print('a: ', str(alpha), 'best fo value: ' , be, 'iteration:  ', fi)

alpha = 0.5
bs, be, fi, sl = heuristicaksat.heuristicgrasp('files/cnft.txt', ite, alpha)
print('a: ', str(alpha), 'best fo value: ' , be, 'iteration:  ', fi)
