# clear environment
rm(list=ls(all=TRUE))


Data<-read.table("./grad_descent_test_1.txt", header = TRUE, sep = " ", comment.char="")
# attach(Data)


library(lattice)
# splom(Data)


library(scatterplot3d)
# s3d<-scatterplot3d(X1,X2,y, pch=16, highlight.3d=TRUE)

library(rgl)

# rgl3d_12<-plot3d(Data, col="red", size=3)
# rgl3d_13<-plot3d(X1,X3,y, col="red", size=3)
# rgl3d_14<-plot3d(X1,X4,y, col="red", size=3)
# rgl3d_15<-plot3d(X1,X5,y, col="red", size=3)
# rgl3d_23<-plot3d(X2,X3,y, col="red", size=3)
# rgl3d_24<-plot3d(X2,X4,y, col="red", size=3)
# rgl3d_25<-plot3d(X2,X5,y, col="red", size=3)
# rgl3d_34<-plot3d(X3,X4,y, col="red", size=3)
# rgl3d_35<-plot3d(X3,X5,y, col="red", size=3)
# rgl3d_45<-plot3d(X4,X5,y, col="red", size=3)
# polygon3d(X1,X2,y)

# library(Rcmdr)
# rcmdr3d<-scatter3d(X1,X2,y)

library(GGally)
ggpairs(Data)