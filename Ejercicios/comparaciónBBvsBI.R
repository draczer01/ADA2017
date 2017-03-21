datos = read.csv("~/PycharmProjects/ADA2017/Ejercicios/algo.txt", sep=" ", header=FALSE)
x = datos[datos$V2 == "wey" & datos$V4 == "True",]
y = datos[datos$V2 == "wey" & datos$V4 == "False",]
xb = datos[datos$V2 == "bin" & datos$V4 == "True",]
yb = datos[datos$V2 == "bin" & datos$V4 == "False",]
a = aggregate(datos, by=list(datos$V2, datos$V3), mean)
aw = a[a$Group.1 == "wey",]
bw = a[a$Group.1 == "bin",]
largo = bw$Group.2
peor = aw$V1
mejor = bw$V1
plot(largo, peor, col="green", pch=16)
#par(new=TRUE)
points(largo, mejor, col="red", pch=16)
