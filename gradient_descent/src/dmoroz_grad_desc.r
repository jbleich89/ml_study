import_matrix <- function(path){
    imported <- data.matrix(read.table(path, header = TRUE, sep = " ", comment.char=""))
    Y <- imported[,1] # y is first column of imported matrix
    X <- cbind(1,imported[,-1]) #remove the first column and then attach as the first column all 1s. 
    my_list <- list("X"=X, "Y"=Y)
    # print(my_list)
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

regular_grad_desc <- function(X,Y) {

    # squared error cost function
    cost <- function(X, Y, Theta) {
      sum( (X %*% Theta - Y)^2 ) / (2*length(Y)) # WHY * 1/(2*length(Y)) ?
    }

    # learning rate and iteration limit
    alpha <- 0.01
    num_iters <- 1000

    # keep history
    cost_history <- double(num_iters)
    Theta_history <- list(num_iters)

    # initialize coefficients
    Theta <- matrix(0, nrow=ncol(X))

    # gradient descent
    for (i in 1:num_iters) {
      error <- (X %*% Theta - Y)
      delta <- t(X) %*% error / length(Y)
      Theta <- Theta - alpha * delta
      cost_history[i] <- cost(X, Y, Theta)
      Theta_history[[i]] <- Theta
    }
    #report distance from closed form
    #determine proper alpha
    return (Theta)
}

stochastic_grad_desc <- function(X,Y) {

    # learning rate and iteration limit
    alpha <- 0.0001
    num_iters <- 1000
    min_change <- 0.001
    n <- ncol(X)
    m <- nrow(X)

    # initialize coefficients
    Theta <- matrix(0, nrow=ncol(X))
    prev_Theta <- matrix(1, nrow=ncol(X))

    # gradient descent
    while( abs(sum(prev_Theta-Theta)) > min_change) { 
        prev_Theta <- Theta
        for(i in 1:m){
            error <- (X[i,] %*% Theta - Y[i])
            delta <- X[i,] * error #in the matrix v above, mult each row in X by its error term
            Theta <- Theta - alpha * delta
        }
        #print(Theta[1])
    }
    return (Theta)
}

path_1 <- "../grad_descent_test_1.txt"
path_2 <- "../grad_descent_test_2.txt"

vars <- import_matrix(path_1)
print(normal_equation_solution(vars$X, vars$Y))
print(r_provided_lm(vars$X, vars$Y))
print(regular_grad_desc(vars$X, vars$Y))
print(stochastic_grad_desc(vars$X, vars$Y))

start <- proc.time()
vars <- import_matrix(path_2)
import_time <- proc.time() - start

ones <- matrix(1,ncol=ncol(vars$X))

start <- proc.time()
norm <- normal_equation_solution(vars$X, vars$Y)
norm_time <- proc.time() - start

start <- proc.time()
stoch <- stochastic_grad_desc(vars$X, vars$Y)
stoch_time <- proc.time() - start

print(import_time)
print(norm_time)
print(stoch_time)
print(ones %*% norm)
print(ones %*% stoch)
#print(dist(rbind(norm,stoch)))
print(abs(sum(norm-stoch)))


#BUG NOTES
#BUG 1: careful about the return syntax. return(return_val)
#BUG 2: careful about the sum function and 1:m s and getting too fancy. use for loop
#Bug 3: you need to set the thetas all at once. Since calc of theta[2] involves all of theta, can't update one theta at a time
#Question: why is it ok to do stochastic grad desc? you're basically optimizing one theta at a time, but it might not be the right theta since the others are off. Answer: you're not doing one theta at a time. Doing all thetas at a time, one data point at a time.
# If you get that comparisons not working, check what theta is. Perhaps it's expanding too fast and has overflowed. Try changing alpha smaller
#Having trouble getting nrows on vars$Y. Returns NULL for some reason but length() works


# dans_regular_grad_desc <- function(X,Y) {

#     # learning rate and iteration limit
#     alpha <- 0.01
#     min_change <- 0.00001 #smallest amount that thetas should be changing
#     n <- ncol(X)
#     m <- nrow(X)
#     Theta <- matrix(0, nrow=n)
#     next_Theta <- matrix(1, nrow=n)


#     # gradient descent
#     while( abs(sum(next_Theta-Theta)) > min_change) { 
#         Theta <- next_Theta
#         for (j in 1:n) {
#             delta <- 0
#             for(i in 1:m){
#                 delta <- delta + (Y[i] - X[i,] %*% Theta) %*% X[i,j]
#             }
#             next_Theta[j] <- Theta[j] + alpha * delta
#         }
#     }
#     return (Theta)
# }

# dans_stoch_grad_desc <- function(X,Y) {

#     # learning rate and iteration limit
#     alpha <- 0.01
#     min_change <- 1 #smallest amount that thetas should be changing
#     n <- ncol(X)
#     m <- nrow(X)
#     Theta <- matrix(0, nrow=n)
#     next_Theta <- matrix(1, nrow=n)


#     # gradient descent
#     while( abs(sum(next_Theta-Theta)) > min_change) { 
#         print(abs(sum(next_Theta-Theta)))
#         Theta <- next_Theta
#         for (j in 1:n) {
#             temp_Theta <- Theta
#             for(i in 1:m){
#                 delta <- (Y[i] - X[i,] %*% Theta) %*% X[i,j]
#                 temp_Theta[j] <- temp_Theta[j] + alpha * delta
#             }
#             next_Theta[j] = temp_Theta[j]
#         }
#     }
#     return (Theta)
# }