# generador de instancias de grafos
from files import graph
from files import InstanciesGenerator
#Nombre
name = 'test'

#Numero de vertices
n= 10
#Numero de aristas
m=round(n*0.3*n)

dl, du = 1 , 3
wl, wu = 1, 10

# Distribucion de los grados
dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, dl, du)
#Distribucion de los pesos
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, wl, wu)

generadorcomplete = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.complete,distribution_weight = dw,distribution_degree = dd, directed = True )

generadorconnected = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.connected,distribution_weight = dw,distribution_degree = dd, directed = True )

generadortree = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.tree,distribution_weight = dw,distribution_degree = dd, directed = True )

g1 = generadorcomplete.generateInstance(name + ' complete', n, m)
g2 = generadorconnected.generateInstance(name + ' connected', n, m)
g3 = generadortree.generateInstance(name + ' tree', n, m)

g1.connected
g1.complete
g1.tree
print(g1.to_string())

g2.connected
g2.complete
g2.tree
print(g2.to_string())

g3.connected
g3.complete
g3.tree
print(g3.to_string())



#Generador SAT
from files import generadorksat
#Numero de variables
v = 100
#Cumero de clausulas
c = 250
#Es DNF? 
dnf = False
# se cren los 4 archivos en la carpeta de files, el que termina en t con una instancia que tiene se puede sartisfacer, uno que terminsa en f con la instancia que no se puede satisfacer, uno r que es completamente aleatoria y el archivo de asignacion de valors para las 4 instancias.
generadorksat.generarkSat(v, c, dnf, path='files/')
