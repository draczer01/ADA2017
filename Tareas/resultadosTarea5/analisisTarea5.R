<<<<<<< HEAD
datos = read.csv("result3Tarea5.dat", sep=" ", header=FALSE)
a = aggregate(datos, by=list(datos$V2), mean)
plot(a$Group.1/(a$V1*a$V1-1), a$V5, col="blue", pch=16, type="l",main="Comparación densidad grafo vs tiempo de ejecucion de FF shortest augmenting path a 205 nodos",xlab="Densida grafo", ylab="Tiempo de ejecucion")
=======
datos = read.csv("resultTarea5.dat", sep=" ", header=FALSE)
a = aggregate(datos, by=list(datos$V2), mean)
plot(a$Group.1*100/a$V1, a$V5, col="blue", pch=16, type="l",main="Comparación tiempo entre la densidad del grafo",xlab="Densidad", ylab="Tiempo")
boxplot(datos$V5 ~ datos$V2)
>>>>>>> 56b72785ca48a714cdd687fd63f244fe1e3b66bf
