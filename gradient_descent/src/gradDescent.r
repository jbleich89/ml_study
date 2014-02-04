# clear environment
rm(list=ls(all=TRUE))

stochasticGD=0
sequentialGD=1
pseudoInvGD=2


gradient <- function(x,y,theta){
	grad <- ( t(x) %*% ( (x %*% t(theta)) - y ) )
	return( t(theta) )
}

gradientSequential <- function(X,Y,theta, i){
	print("todo fill in")
}


runStochasticGD <- function( data, alpha, initialVals){
	Thetas=initialVals
	Y=data$y 
	rows=nrow(data)
	cols=ncol(data)



	print("TODO: implement runStochasticGD")
}

runSequentialGD <- function( data, alpha, initialVals){
	print("TODO: implement runSequentialGD")
}

runPseudoInvGD <- function( data ){
	print("TODO: implement runPseudoInvGD")
}



alpha=.001
GDform=stochasticGD
DataFile="./grad_descent_test_1.txt"

Data<-read.table( DataFile, header = TRUE, sep = " ", comment.char="")
library(GGally)
ggpairs(Data)

if ( GDform==stochasticGD ){
	newTheta<-runStochasticGD(Data, alpha, c(0,0,0,0,0) )
} else if( GDform==sequentialGD){
	newTheta<-runSequentialGD(Data, alpha, c(0,0,0,0,0) )
}else if (GDform==pseudoInvGD){
	newTheta<-runPseudoInvGD(Data )
}



