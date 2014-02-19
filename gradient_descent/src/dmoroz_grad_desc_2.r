import_matrix <- function(path){
    imported <- data.matrix(read.table(path, header = TRUE, sep = " ", comment.char=""))
    Y <- imported[,1] # y is first column of imported matrix
    X <- cbind(1,imported[,-1]) #remove the first column and then attach as the first column all 1s. 
    my_list <- list("X"=X, "Y"=Y)
    return (my_list)
}

normal_equation_solution <- function(X,Y) {
    Theta <- solve(t(X) %*% X) %*% t(X) %*% Y
    return (Theta) #
}

r_provided_lm <- function(X,Y) {
    Theta <- lm(Y~X)
    return (Theta)
}

regular_grad_desc <- function(X,Y,alpha_init, alpha_sched, min_change_init, type, lambda) {

    if (type == "ridge") {
        cost <- function(X, Y, Theta, lambda) {
          (sum( (X %*% Theta - Y)^2 ) + lambda * norm(Theta, "2")) / (2*length(Y))
        }
    } else if (type == "lasso") {
        cost <- function(X, Y, Theta, lambda) {
          (sum( (X %*% Theta - Y)^2 ) + lambda * norm(Theta, "1")) / (2*length(Y))
        }
    } else {
        cost <- function(X, Y, Theta) {
          sum( (X %*% Theta - Y)^2 ) / (2*length(Y))
        }
    }

    alpha <- alpha_init
    min_change <- min_change_init
    Theta <- matrix(0, nrow=ncol(X))
    prev_Theta <- matrix(1, nrow=ncol(X))

    # gradient descent
    i <- 0
    while( abs(sum(prev_Theta-Theta)) > min_change) { 
        i <- i + 1

        if (alpha_sched == "dec_by_1_over_alpha") {
            alpha <- alpha - 1/(alpha*i)
        } else if (alpha_sched == "dec_by_1_over_sqrt_iter") {
            alpha <- alpha_init / sqrt(i)
            min_change <- min_change_init / sqrt(i)
        } 

        prev_Theta <- Theta      
        error <- (X %*% Theta - Y)
        delta <- t(X) %*% error / length(Y)

        if (type == "ridge") {
            Theta <- Theta * (1 - alpha*lambda/length(Y)) - alpha * delta
        } else if (type == "lasso") {
            Theta <- Theta * (1 - alpha*lambda/length(Y)) - alpha * delta
        } else {
            Theta <- Theta - alpha * delta
        }
    }
    return (Theta)
}

path_1 <- "./ml_study/gradient_descent/grad_descent_test_1.txt"

vars <- import_matrix(path_1)
print(normal_equation_solution(vars$X, vars$Y))
print(r_provided_lm(vars$X, vars$Y))

start <- proc.time()
norm <- normal_equation_solution(vars$X, vars$Y)
norm_time <- proc.time() - start

start <- proc.time()

#regular_grad_desc <- function(X,Y,alpha_init, alpha_sched, min_change, type, lambda) {
#lin_reg <- regular_grad_desc(vars$X, vars$Y, 0.001, "dec_by_1_over_iter", 0.001, "ridge", 0.01)
lin_reg <- regular_grad_desc(vars$X, vars$Y, 0.01, "reg", 0.001, "ridge", 0)
lin_reg_time <- proc.time() - start

print(norm_time)
print(lin_reg_time)
print(norm)
print(lin_reg)

#BUGS: Problem is that when you decrease alpha, the change goes under the min_value, a const. So if alpha is to change, min value should change too?
# how do you know what "convergence" is?
