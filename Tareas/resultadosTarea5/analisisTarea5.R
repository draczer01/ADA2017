datos = read.csv("resultTarea5.dat", sep=" ", header=FALSE)
a = aggregate(datos, by=list(datos$V1), mean)
plot(a$Group.1, a$V2, col="blue", pch=16, type="l",main="Comparación quicksort vs prune and search",xlab="Tamaño cadena (n)", ylab="Cant. de comparaciones")
lines(a$Group.1, a$V3, col="red", pch=16)
lines(a$Group.1, (a$Group.1* log(a$Group.1,2)), col="black", pch=16)
lines(a$Group.1, (a$V1**2), col="green", pch=16)
legend("topright", inset=.05, title="Comparaciones",
   c("ps","qs", "nlog(n)","n^2"),lty=c(1,1,1,1),col=c("blue","red","black", "green") )
