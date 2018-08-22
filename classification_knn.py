from math import sqrt
import numpy as np
import pandas as pd
import random

def dataset(filename,drop_name,class_name,split_size):
    df=pd.read_csv(filename);
    if drop_name!='':
        df.drop(drop_name,1,inplace=True);
    x1=np.array(df);
    #y1=np.array(df[class_name]);
    train_set=[]
    test_set=[]
    for i in range(len(x1)):
            if i<(split_size*len(x1)):
                train_set.append(x1[i])
            else:
                test_set.append(x1[i])
    train_set=np.array(train_set,dtype=np.float64)
    test_set=np.array(test_set,dtype=np.float64)
    return train_set,test_set

def min_dist(distance,avoid):
    min2=distance[0][0]
    for i in range(len(distance)):
        if distance[i][0]==avoid:
            continue;
        if min2>distance[i][0]:
            min2=distance[i][0]
    return min2

def k_nearest_neighbours(distance,k):
    a=0
    a_bar=0
    least_dist=[]
    least_dist.append(-1)
    krr=[]
    for i in range(1,k+1):
        least=min_dist(distance,least_dist[i-1]);
        least_dist.append(least)
    for j in range(1,k+1):
        for i in range (len(distance)):
            if distance[i][0]==least_dist[j]:
                krr.append(distance[i][1])
    for i in range(5):
        if krr[i]==0:
            a_bar+=1;
        else:
            a+=1;
    if(a_bar>a):
        return 0;
    else:
        return 1;

def accuracy(krr_test,test):
    tp=0
    fp=0
    for i in range(len(krr_test)):
        if krr_test[i]==test[i][len(test[0])-1]:
            tp+=1
        else:
            fp+=1
    return int((tp/(tp+fp))*100);

def euclidian_dist(train_set,test_set):
    krr_test=[]
    for x in range(len(test_set)):
        distance=[]
        for features in train_set:
            e_distance=0.0
            for i in range(len(features)-1):
                e_distance+=((features[i]-test_set[x][i])**2)
            distance.append([sqrt(e_distance),features[len(features)-1]])
        krr_test.append(k_nearest_neighbours(distance,5))
    for i in range(len(krr_test)):
        print(krr_test[i],test_set[i][len(test_set[0])-1])
    return accuracy(krr_test,test_set);

def main():
    filename='ex2data1.csv'         
    drop_name=''
    class_name='class'
    train,test=dataset(filename,drop_name,class_name,split_size=0.8)
    acc=euclidian_dist(train,test)
    print(acc)
main()
