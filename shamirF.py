import random
import numpy as np
import Zq as zq_ 

class shamirF:    
    
    def __init__(self,q, s,t):        
        self.s =s
        self.t =t
        self.fq = zq_.Zq(q)   
        
    def setAlfa(self,alfa):
        self.alfa=alfa
        
    def __hornerInZq(self,poly, n, x):     
        result = poly[0]       
        for i in range(1, n):             
            result = self.fq.suma(self.fq.producto(result,x) , poly[i]) 
        return result
    
    def __makePolynomial (self):
        # Seleccionar t-1 elementos aleatorios de zq
        self.poly = [self.fq.getRandomElement() for i in range(0,self.t-1) ]               
        self.poly.append(self.alfa)
        
    def generateParts(self):
        self.__makePolynomial()
        parts=[]
        for x in range (1, self.s+1):
            y = self.__hornerInZq(self.poly,len(self.poly),x) 
            parts.append((x,y))
        return parts    
        
    def makeSecret(self,tParts):
        alfa_g0=0
        for i in range (0,self.t) :       
            coef=1
            for j in range (0,self.t):
                if (j!=i):                                  
                    nu = self.fq.resta(0,tParts[j][0])
                    den = self.fq.resta(tParts[i][0],tParts[j][0])
                    coef = self.fq.producto(coef ,self.fq.division (nu,den))                                
            alfa_g0 = self.fq.suma (alfa_g0 , self.fq.producto(coef,tParts[i][1]))
        return alfa_g0            


        
