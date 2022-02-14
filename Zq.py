import random as random
class Zq:
    
    def __init__(self,q):
        self.q = q        

    def __modulo (self,a,b):
        return a%b # residuo div entera entre a y b

    def suma(self,a,b):
        r= self.__modulo((a+b),self.q)
        return r

    def resta(self,a,b):
        r = self.__modulo (a-b,self.q)
        return r

    def producto (self,a,b):
        r= self.__modulo(a*b,self.q)
        return r 

    def division (self,a,b):
        invM_b= self.invMulti(b)
        r= self.__modulo(a*invM_b,self.q)
        return r

    def invMulti(self,a):
        r= self.__gcdExtended(a,self.q)[1]
        return r    

    def __gcdExtended(self,a, b): 
    # Base Case 
        if a == 0 :  
            return b,0,1             
        gcd,x1,y1 = self.__gcdExtended(b%a, a) 
        # Update x and y using results of recursive 
        # call 
        x = y1 - (b//a) * x1 
        y = x1      
        return gcd,x,y        

    def getRandomElement(self):
        return random.randint(0,self.q-1)
        