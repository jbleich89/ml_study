# animationEx.r


library(animation)
library
ani.options(interval=.05)
ani.options(outdir=getwd())
library(animation)

#Set delay between frames when replaying
ani.options(interval=.05)

# Set up a vector of colors for use below 
col.range <- heat.colors(15)


generatePts <- function(dx1=-.0,dy1=-.0,dx2=.25,dy2=.20, numPts=500){
	Tpts=rbind(rnorm(numPts/2)+dx1,rnorm(numPts/2)+dy1)
	Fpts=rbind(rnorm(numPts/2)+dx2,rnorm(numPts/2)+dy2)
	TptColors=c( rep( 1,numPts/2) )
	FptColors=c( rep(-1,numPts/2) )
	# Tpts=matrix( c(Tvals) ,nrow=2 )
	# Fpts=matrix( c(Fvals) ,nrow=2 )
	Tdata=rbind(TptColors,Tpts)
	Fdata=rbind(FptColors,Fpts)
	data <- cbind(Fdata, Tdata )
	data[,sample.int(ncol(data))]

	# print(pts)
	data[2,] = data[2,]-mean(data[2,])
	data[3,] = data[3,]-mean(data[3,])
	return(data)
}
	
normalize <-function(mat){
	d<-dim(mat)
	# rows<-d[1]
	# print('mat');	print(mat)
	# print('d');	print(d)
	# print('elementSqrs'); print(mat^2)
	# print('col norm');	print(sqrt(colSums( mat^2 )))
	# mat<-mat*1/sqrt( colSums(mat[1:rows,]^2) )
	mat<- apply(mat,2, function(x){x/sqrt(sum(x^2))})
	# print('col norm');	print(sqrt(colSums( mat^2 )))
	# print('res');	print (mat)
	return ( mat)
} 




findW <-function(dataN,data, wIterations=1000){
	dData=dim(dataN)
	ptsN=dataN[2:dData[1],]
	pts=data[2:dData[1],]
	class=dataN[1,]
	d=dim(ptsN)
	rows=d[1]
	cols=d[2]
	w=matrix(rep( rep(c(0),each=rows),each=wIterations),ncol=wIterations)
	w[1,1]=.01
	i=1
	misClasExist=TRUE
	lastVect=0
	selected=1
	while ( i < wIterations && misClasExist){
		# print('here')
		j=0
		noBadFound=TRUE
		misClasExist=FALSE
		while (j<=cols && noBadFound) { 
			j=j+1
			selected=(lastVect + j )%%cols+1
			projection=sum( w[,i]*ptsN[,selected])
			if ( 0 > class[selected]*projection ){
				# print(class[selected]*ptsN[,selected])
				noBadFound=FALSE
				misClasExist=TRUE
				i=i+1
				w[,i]=w[,i-1]-class[selected]*(ptsN[,selected])
				if(i%%100==0){
					plot(pts[1,],pts[2,], col=ifelse(class[]==1,'red','black'))
					abline(0,w[2,i]/w[1,i])
				}
				# Sys.sleep(.025)
			}
		}
		lastVect=selected
	}
	return (w)
}

numPts=100
data <- generatePts( numPts=numPts)
# data
plot(data[2,],data[3,], col=ifelse(data[1,]==1,'red','black'))
Sys.sleep(1)
dataN<-data
dataN[2:3,] <- normalize(dataN[2:3,])
plot(dataN[2,],dataN[3,], col=ifelse(dataN[1,]==1,'red','black'))
Sys.sleep(1)
w=findW(dataN,data)

# Begin animation loop
# Note the brackets within the parentheses
saveGIF({
	
	# For the most part, it’s safest to start with graphical settings in 
	# the animation loop, as the loop adds a layer of complexity to 
	# manipulating the graphs. For example, the layout specification needs to 
	# be within animation loop to work properly.
	# layout(matrix(c(1, rep(2, 5)), 6, 1))
	
	# Adjust the margins a little
	par(mar=c(4,4,2,1) + 0.1)
	# Begin the loop that creates the (frames) individual graphs
	frames =1000
	for (i in 1:frames) {
		
		# Pull 100 observations from a normal distribution
		# and add a constant based on the iteration to move the distribution
		
		# Reset the color of the top chart every time (so that it doesn’t change as the 
		# bottom chart changes)
		par(fg=1)
		
		# Set up the top chart that keeps track of the current frame/iteration
		# Dress it up a little just for fun
		
		# Bring back the X axis
		# axis(1)
		
		# Set the color of the bottom chart based on the distance of the distribution’s mean from 0
		# par(fg = col.range[mean(chunk)+3])
		
		# Set up the bottom chart
		# plot(density(chunk), main = '', xlab = 'X Value', xlim = c(-5, 15), ylim = c(0, .6))	
		# Add a line that indicates the mean of the distribution. Add additional lines to track
		# previous means
		abline(v=mean(chunk), col = rgb(255, 0, 0, 255, maxColorValue=255))
		if (exists('lastmean')) {abline(v=lastmean, col = rgb(255, 0, 0, 50, maxColorValue=255)); prevlastmean <- lastmean;}
		if (exists('prevlastmean')) {abline(v=prevlastmean, col = rgb(255, 0, 0, 25, maxColorValue=255))}
		#Fix last mean calculation
		lastmean <- mean(chunk)
	}
})