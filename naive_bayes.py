# -*- coding: utf-8 -*-
#author: ANDY

import numpy as np
import random
from sklearn import cross_validation

class naive_bayes:

    def __init__(self,k,n,a):
        self.k=k
        self.n=n
        self.x=np.zeros(self.n)
        self.y=np.zeros(self.n)
        self.c=[0,1]
        self.a=a

    
    def read():
        pass
    
    
    def cal_probab(m,n):

        return m/n
        
    
    def cal_occur(self,features,x,y):
        
        countedlist=np.zeros(len(self.c),len(self.a))
        count=0
        
        for feature in features:
            for i in range(self.n):                
                if feature==x[i] and y[i]==0:
                    countedlist[0][count]+=1
                else:
                    if feature==x[i] and y[i]==1:
                        countedlist[1][count]+=1
                    
            count+=1
            
        return countedlist
    
                        
    def train(self):
        
        posteriori_event=self.cal_occur(self.a,self.x,self.y)
                
        sum_event=0        
        for i in range(self.a):
            for j in range(self.c):                
                if posteriori_event[i][j]!=0:
                    sum_event+=1
                    
        posteriori_probab=np.zeros(len(self.c),len(self.a))
        for i in range(self.a):
            for j in range(self.c):
                posteriori_probab=self.cal_probab(posteriori_event[i][j],sum_event)
        
        return posteriori_probab
    
    
    def predict():
        pass
