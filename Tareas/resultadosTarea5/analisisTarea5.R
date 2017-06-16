datos = read.csv("result3Tarea5.dat", sep=" ", header=FALSE)
a = aggregate(datos, by=list(datos$V2), mean)
plot(a$Group.1/(a$V1*a$V1-1), a$V5, col="blue", pch=16, type="l",main="Comparación densidad grafo vs tiempo de ejecucion de FF shortest augmenting path a 205 nodos",xlab="Densida grafo", ylab="Tiempo de ejecucion")
