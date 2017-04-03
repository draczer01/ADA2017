datos = read.csv("~/pyprojects/ADA2017/Ejercicios/val.dat", sep=" ", header=FALSE)
a = aggregate(datos, by=list(datos$V2), mean)
plot(a$Group.1, a$V1, col="blue", pch=16)
points(a$Group.1, (a$Group.1* log(a$Group.1)), col="red", pch=16)
points(a$Group.1, (a$Group.1* a$Group.1), col="green", pch=16)


