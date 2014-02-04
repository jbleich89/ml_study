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


# # Load data and initialize values
# data <- read.csv("http://www.statalgo.com/wp-content/uploads/2011/10/housing.csv")
 
# alpha <- 0.01
# m <- nrow(data)
# x <- matrix(c(rep(1,m), data$area), ncol=2)
# y <- matrix(data$price, ncol=1) / 1000
 
# # Z-Score the feature
# x.scaled <- x
# x.scaled[,2] <- (x[,2] - mean(x[,2]))/sd(x[,2])
 
# # Gradient descent function
# grad <- function(x, y, theta) {
#   gradient <- (t(x) %*% ((x %*% t(theta)) - y))
#   return(t(gradient))
# }
 
# gradient.path <- function(x) {
#     # Initialize the parameters
#     theta <- matrix(c(0, 0), nrow=1)
 
#     # Look at the values over each iteration
#     theta.path <- matrix(ncol=2)
#     for (i in 1:500) {
#       theta <- theta - alpha * 1/m * grad(x, y, theta)
# 	if(all(is.na(theta))) break
#       theta.path <- rbind(theta.path, theta)
#     }
#     theta.path
# }
 
# unscaled.theta <- gradient.path(x)
# scaled.theta <- gradient.path(x.scaled)
 
# summary(lm(y ~ x[, 2]))
# summary(lm(y ~ x.scaled[, 2]))
