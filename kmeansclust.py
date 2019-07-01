#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#KMEANS CLUSTERING
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

iris = datasets.load_iris()
##iris.keys()


df= pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                 columns= iris['feature_names'] + ['target'])

df

wcss=[];
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
    km=kmeans.fit(df)
    wcss.append(km.inertia_)


plt.scatter(range(1,11),wcss)
plt.plot(range(1,11),wcss)
plt.title("EBLOW CURVE")
plt.xlabel('NO OF CLUSTER(K)')
plt.ylabel('DISTANCE')
plt.legend('inertia')
plt.legend('K value')

#found for k=3 has maximum elbw hence 3 will be optimum value for k

#now lets fit kmenas to the dataset
kmean=KMeans(n_clusters=3,random_state=0,init='k-means++')
y_kmeans=kmean.fit_predict(df)


plt.scatter(df[y_kmeans==0,0],df[y_kmeans==0,1],s=100,c='r',label='cluster1')