datos = read.csv("result2Tarea5.dat", sep=" ", header=FALSE)
a = aggregate(datos, by=list(datos$V2), mean)
plot(a$Group.1/(a$V1*a$V1-1), a$V5, col="blue", pch=16, type="l",main="Comparación densidad grafo vs tiempo de ejecucion de FF shortest augmenting path a 205 nodos",xlab="Densida grafo", ylab="Tiempo de ejecucion")
boxplot(datos$V5 ~ datos$V2)
plot(a$Group.1/(a$V1*a$V1-1), a$V4, col="blue", pch=16, type="l",main="Comparación densidad grafo vs flujo por FF shortest augmenting path a 205 nodos",xlab="Densida grafo", ylab="Flujo")
boxplot(datos$V4 ~ datos$V2)

datos = read.csv("result3Tarea5.dat", sep=" ", header=FALSE)
a = aggregate(datos, by=list(datos$V2), mean)
plot(a$Group.1/(a$V1*a$V1-1), a$V5, col="blue", pch=16, type="l",main="Comparación densidad grafo vs tiempo de ejecucion de FF shortest augmenting path a 105 nodos",xlab="Densida grafo", ylab="Tiempo de ejecucion")
boxplot(datos$V5 ~ datos$V2)
plot(a$Group.1/(a$V1*a$V1-1), a$V4, col="blue", pch=16, type="l",main="Comparación densidad grafo vs flujo por FF shortest augmenting path a 105 nodos",xlab="Densida grafo", ylab="Flujo")
boxplot(datos$V4 ~ datos$V2)

datos = read.csv("resultTarea5.dat", sep=" ", header=FALSE)
a = aggregate(datos, by=list(datos$V2), mean)
plot(a$Group.1/(a$V1*a$V1-1), a$V5, col="blue", pch=16, type="l",main="Comparación densidad grafo vs tiempo de ejecucion de FF shortest augmenting path a 1005 nodos",xlab="Densida grafo", ylab="Tiempo de ejecucion")
boxplot(datos$V5 ~ datos$V2)
plot(a$Group.1/(a$V1*a$V1-1), a$V4, col="blue", pch=16, type="l",main="Comparación densidad grafo vs flujo por FF shortest augmenting path a 1005 nodos",xlab="Densida grafo", ylab="Flujo")
boxplot(datos$V4 ~ datos$V2)


