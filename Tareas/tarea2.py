# generador de instancias de grafos
import files.graph
import files.InstanciesGenerator

dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 10, 2)
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 2, 5)
generador = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.complete,distribution_weight = dw,distribution_degree = dd, directed = True )
g = generador.generateInstance('Test', 10, 50)

print(g)
