hello<-function() {
	cat(paste("Hello, ",system("whoami",T),"!\n",sep="",collapse=""))
	today<-as.list(unlist(strsplit(system("date",T)," ")))
	names(today)<-c("weekday","month","","day","time","timezone","year")
	return(today)
}

k=hello()
cat(paste("the time is ",k$time,"\n",sep="",collapse=""))