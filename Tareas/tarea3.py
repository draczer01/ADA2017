#heurisitca grasp para sat 
from files import heuristicaksat
from files import generadorksat
generadorksat.generarkSat(100, 300, True)
print(heuristicaksat.heuristicgrasp('files/cnft.txt', 30, 0.1))
