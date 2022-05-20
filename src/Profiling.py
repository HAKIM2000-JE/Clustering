import pandas as pd
from bson import ObjectId

from sklearn.preprocessing import LabelEncoder
from tabulate import tabulate
import time

import Profile
from sklearn.cluster import KMeans





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def getProfiles(df):

    cols = ['_id',"adults","children","babies","doubleBeds","singleBeds","sofaBeds","babyBeds","startDate"]
    df = df[cols]

    df['_id'] = df['_id'].apply(
        lambda x: str(x))

    encode = LabelEncoder()
    encoded = encode.fit_transform(df.iloc[:, 0])
    df['_id'] = encoded
    print(encoded)

    df['startDate'] = df['startDate'].apply(
        lambda x: pd.datetime.strptime(str(x), '%Y-%m-%d').month if type(x) == str else 1)

    #df["startDate"] = df["startDate"].astype(float)



    ###############################################
    Sum_of_squared_distances = []

    K = range(1,15)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(df)
        Sum_of_squared_distances.append(km.inertia_)


    plt.plot(K, Sum_of_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    plt.show()
    ################################################

    #Example of 5 profile
    kmeans = KMeans(n_clusters=5).fit(df)

    # Generated Profiles
    labels = kmeans.labels_


    #Means value of profiles
    centroids = kmeans.cluster_centers_

    print(pd.Series(labels).value_counts())
    ProfilingResult = []
    for i in np.unique(labels):
        print("#########################################################")
        print( df[labels == i])
        encoded_reverse = encode.inverse_transform(df.iloc[:, 0])

        print("Lit of Ids")

        objectIdList= [ObjectId(x) for x in encoded_reverse.tolist() ]
        ProfilingResult.append(objectIdList)

        print(encoded_reverse.tolist())


    print("Centroide",centroids)

    return ProfilingResult



