datos = read.csv("resultTarea8.txt", sep=" ", header=FALSE)
plot(datos$V1, datos$V2, type="l")
lines(datos$V1, datos$V3, col='red')