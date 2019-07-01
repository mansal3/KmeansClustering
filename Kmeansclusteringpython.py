#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:30:30 2019

@author: manpreetsaluja
"""

#KMEANS CLUSTERING

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

data={'X':np.random.randint(1,100,50),'Y':np.random.randint(1,100,50)}
datadf=pd.DataFrame(data)

datadf.plot.scatter(x='X',y='Y',c='r')
km=KMeans(n_clusters=4)
km.fit(datadf)

km.cluster_centers_

km.labels_
plt.scatter(datadf['X'],datadf['Y'],c='b',marker='+')
plt.scatter(13.,30.1111111,c='r')
plt.scatter(72.15384615, 14.92307692,c='y')
plt.scatter(62.86666667, 53.6    ,c='g')
plt.scatter(42.53846154, 85.53846154  ,c='k')

Sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(datadf)
    Sum_of_squared_distances.append(km.inertia_)
    
    plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()