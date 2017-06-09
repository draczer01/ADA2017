# generador de instancias de grafos
from files import graph
from files import InstanciesGenerator
import time
#Nombre
name = 'test'
direct = False
#Numero de vertices
n= 100
#Numero de aristas
m05=round(n*0.15*n)
m1=round(n*0.3*n)
m2=round(n*0.5*n)
m3=round(n*0.7*n)

dl, du = 1 , n
wl, wu = 1, 10

# Distribucion de los grados
dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, dl, du)
#Distribucion de los pesos
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, wl, wu)

generadorcomplete = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.complete,distribution_weight = dw,distribution_degree = dd, directed = direct )

generadorconnected = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.connected,distribution_weight = dw,distribution_degree = dd, directed = direct )

generadortree = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.tree,distribution_weight = dw,distribution_degree = dd, directed = direct )


g0 = generadortree.generateInstance(name + ' tree', n, m1)
g0.connected
g0.complete
g0.tree
tt0 = time.clock()
cct =g0.closenesscentrality()
tt1 = time.clock()
print(g0.to_string(sv=False))
print('time cc: ', str(tt1-tt0) +'\n')
tt0 = time.clock()
bfst =g0.breadthfirstsearch()
tt1 = time.clock()
print('timebfs: ', str(tt1-tt0) +'\n')
tt0 = time.clock()
dfst =g0.deepfirstsearch()
tt1 = time.clock()
print('timedfs: ', str(tt1-tt0) +'\n')
del g0


g05 = generadorconnected.generateInstance(name + ' connected', n, m05)
g05.connected
g05.complete
g05.tree
tk0 = time.clock()
cck =g05.closenesscentrality()
tk1 = time.clock()
print(g05.to_string(sv=False))
print('time cc 15: ', str(tk1-tk0) +'\n')
tk0 = time.clock()
bfsc =g05.breadthfirstsearch()
tk1 = time.clock()
print('time bfs: ', str(tk1-tk0) +'\n')
tk0 = time.clock()
dfsc =g05.deepfirstsearch()
tk1 = time.clock()
print('time dfs: ', str(tk1-tk0) +'\n')
del g05

g1 = generadorconnected.generateInstance(name + ' connected', n, m1)
g1.connected
g1.complete
g1.tree
tk0 = time.clock()
cck =g1.closenesscentrality()
tk1 = time.clock()
print(g1.to_string(sv=False))
print('time cc 30: ', str(tk1-tk0))
tk0 = time.clock()
bfsc =g1.breadthfirstsearch()
tk1 = time.clock()
print('time bfs: ', str(tk1-tk0) +'\n')
tk0 = time.clock()
dfsc =g1.deepfirstsearch()
tk1 = time.clock()
print('time dfs: ', str(tk1-tk0) +'\n')
del g1

g2 = generadorconnected.generateInstance(name + ' connected', n, m2)
g2.connected
g2.complete
g2.tree
tk0 = time.clock()
cck =g2.closenesscentrality()
tk1 = time.clock()
print(g2.to_string(sv=False))
print('time cc 50: ', str(tk1-tk0))
tk0 = time.clock()
bfsc =g2.breadthfirstsearch()
tk1 = time.clock()
print('time bfs: ', str(tk1-tk0) +'\n')
tk0 = time.clock()
dfsc =g2.deepfirstsearch()
tk1 = time.clock()
print('time dfs: ', str(tk1-tk0) +'\n')
del g2

g3 = generadorconnected.generateInstance(name + ' connected', n, m3)
g3.connected
g3.complete
g3.tree
tk0 = time.clock()
cck =g3.closenesscentrality()
tk1 = time.clock()
print(g3.to_string(sv=False))
print('time cc 70: ', str(tk1-tk0) +'\n')
tk0 = time.clock()
bfsc =g3.breadthfirstsearch()
tk1 = time.clock()
print('time bfs: ', str(tk1-tk0) +'\n')
tk0 = time.clock()
dfsc =g3.deepfirstsearch()
tk1 = time.clock()
print('time dfs: ', str(tk1-tk0) +'\n')
del g3

g4 = generadorcomplete.generateInstance(name + ' complete', n, m1)
g4.connected
g4.complete
g4.tree
tc0 = time.clock()
ccc = g4.closenesscentrality()
tc1 = time.clock()
print(g4.to_string(sv=False))
print('time cc 100: ', str(tc1-tc0) +'\n')
tk0 = time.clock()
bfsc =g4.breadthfirstsearch()
tk1 = time.clock()
print('time bfs: ', str(tk1-tk0) +'\n')
tk0 = time.clock()
bfsc =g4.deepfirstsearch()
tk1 = time.clock()
print('time dfs: ', str(tk1-tk0) +'\n')
del g4

