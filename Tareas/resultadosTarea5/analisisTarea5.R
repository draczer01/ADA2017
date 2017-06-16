datos = read.csv("resultTarea5.dat", sep=" ", header=FALSE)
a = aggregate(datos, by=list(datos$V2), mean)
plot(a$Group.1*100/a$V1, a$V5, col="blue", pch=16, type="l",main="Comparación tiempo entre la densidad del grafo",xlab="Densidad", ylab="Tiempo")
boxplot(datos$V5 ~ datos$V2)
