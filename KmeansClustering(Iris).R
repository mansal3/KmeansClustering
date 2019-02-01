#import the dataset
data(iris)
data<-iris
plot(iris)

#scale data
irisScaled<-scale(iris[,-5])
irisScaled

#kmeans clustering
kmeansmodel<-kmeans(irisScaled,3)
kmeansmodel
str(kmeansmodel)
plot(iris,col=kmeansmodel$cluster)

#choosing k..
k<-list()
for(i in 1:10){
  k[[i]]<-kmeans(irisScaled,i)
}
k

#determining sum of distance between clusters
betweenss_totlss<-list()
for(i in 1:10){
  
  betweenss_totlss[[i]]<-k[[i]]$betweenss/k[[i]]$totss
}
betweenss_totlss

#ploting it against cluster nd finding the optimal no of cluster at distance
plot(1:10,betweenss_totlss,type = "b",ylab = "betweenss_totlss",xlab = "clusters")

for(i in 1:4)
{
  plot(iris,col=k[[i]]$cluster)
  
}
