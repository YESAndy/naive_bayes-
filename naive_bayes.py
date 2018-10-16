# -*- coding: utf-8 -*-
#author: ANDY

import numpy as np
import random
from sklearn import cross_validation

class naive_bayes:

    def __init__(self,x,y,n,a,c):
    
    #define number of train data and the features of x and y for a and c respectively
        self.n=n
        self.c=c
        self.a=a
    #define x and y
        self.trainx,self.trainy,self.testx,self.testy=self.read(x,y)
        
   #read data from input     
    def read(self,filename):
        
        
        trainx,trainy,testx,testy=cross_validation=(x,y)
        return trainx,trainy,testx,testy
    
    #calculate the probability
    def cal_probab(m,n):

        return m/n
        
    #calculate the occurrence numbers of all possible probability events
    def cal_occur(self,x,y):
        #define a matrix to store the occurrence numbers
        countedlist=np.zeros(len(self.c),len(self.a))
        count=0
        n=self.n
        for feature in self.a:
            for i in range(n):                
                if feature==x[i] and y[i]==0:
                    countedlist[0][count]+=1
                else:
                    if feature==x[i] and y[i]==1:
                        countedlist[1][count]+=1
                    
            count+=1
            
        return countedlist
    
    # train the data                    
    def train(self):
        
        len_a=len(self.a)
        len_c=len(self.c)
        
        posteriori_event=self.cal_occur(self.trainx,self.trainy)
        y_event=np.zeros(len_c)        
        
        #calculate the number of each y events
        sum_event=0 
        for i in range(len_c):
            for j in range(len_a):                
                y_event[i]+=posteriori_event[i][j]
                
        #calculate the sum of the number of the posteriori events
        for i in range(len_c):
            sum_event+=y_event[i]
         
        #calculate the probability of each y event 
        y_probab=np.zeros(len_c)
        for i in range(len_c):
            y_probab[i]=self.cal_probab(y_event,sum_event)
            
        #calculate the probability of each posteriori event            
        posteriori_probab=np.zeros(len_c,len_a)
        for i in range(len_a):
            for j in range(len_c):
                posteriori_probab[i][j]=self.cal_probab(posteriori_event[i][j],sum_event)
        
        return posteriori_probab,y_probab
    
    
    def predict(self):
        
        
        posteriori_probab,y_probab=self.train()
        
        test_probab=np.zeros(self.c)
        test_probab+=1
        test_predict=0
        
        #predix
        len_testx=len(self.testx)
        
        for i in range(len_testx):
            for j in range(len(self.a)):
                if self.testx[i] == self.a[j]:
                    test_probab[0]=test_probab[0]*posteriori_probab[0][j]*y_probab[0]
                    test_probab[1]=test_probab[1]*posteriori_probab[1][j]*y_probab[1]
        
        #rank the most probable y and select it as predicted class
        if test_probab[0]>test_probab[1]:
            test_predict=test_probab[0]
        else:
            test_predict=test_probab[1]
            
        return test_predict
        
        
        def score(self):
            
             pass
                    
                    
       
        
        
        
