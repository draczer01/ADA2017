datos = read.csv("resultTarea8.txt", sep=" ", header=FALSE)
a = aggregate(datos, by=list(datos$V1), mean)
plot(a$Group.1, a$V2, type="l")
