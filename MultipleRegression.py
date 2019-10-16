
# coding: utf-8

"""
Created on Wed Oct 9 10:15:19 2019
@author: Gourav Pattanaik
Multiple (3 variable) Regression
y= m1x1 + m2x2 + c Implementation
Sum YX1 = m1*Sum X1^2 + m2*Sum (X1*X2) + C*Sum X1
Sum YX2 = m2*Sum X2^2 + m1*Sum (X1*X2) + C*Sum X2
Sum Y   = m1*Sum X1   + m2*Sum X2 + C*n
"""

import math
from collections import OrderedDict
class MultipleLinearRegression:
    def __init__(self,Dict):
        #print("init")
        self.dict = OrderedDict(Dict);
        self.threshLimit= 1.96 / (math.sqrt(len(Dict)))
        self.elemCount=len(Dict)
        
    def main(self):
        return (self.dict)

    def getSumOfX1(self):
        val = 0
        for i in d.items(): 
            val = val + i[1][0] 
        return round(val,3) 

    def getSumOfX2(self):
        val = 0
        for i in d.items(): 
            val = val + i[1][1] 
        return round(val,3) 
    
    def getSumOfY(self):
        val = sum(self.dict.keys())
        return round(val,3)
    
    def getSumOfX1Y(self):
        sum = 0
        for k, v in self.dict.items():
            sum = sum + k*v[0]
        return round(sum,3)
    
    def getSumOfX2Y(self):
        sum = 0
        for k, v in self.dict.items():
            sum = sum + k*v[1]
        return round(sum,3)
    
    def getSumOfX1X2(self):
        sum = 0
        for k, v in self.dict.items():
            sum = sum + (v[0]*v[1])
        return round(sum,3)    
      
    def getSumOfX1Power2(self):
        sum = 0
        for k, v in self.dict.items():
            sum = sum + v[0]**2
        return round(sum,3)

    def getSumOfX2Power2(self):
        sum = 0
        for k, v in self.dict.items():
            sum = sum + v[1]**2
        return round(sum,3)
    
    def getVariablesM1_M2_C(self):
        numofM1 = (self.getSumOfX2Power2() * self.getSumOfX1Y()) - (self.getSumOfX1X2()*self.getSumOfX2Y())
        denaofM1 = (self.getSumOfX1Power2() * self.getSumOfX2Power2()) - (self.getSumOfX1X2()**2)
        m1 = numofM1 / denaofM1
        m1 = round(m1,3)
        
        numofM2 = (self.getSumOfX1Power2() * self.getSumOfX2Y()) - (self.getSumOfX1X2()*self.getSumOfX1Y())
        denaofM2 = (self.getSumOfX1Power2() * self.getSumOfX2Power2()) - (self.getSumOfX1X2()**2)
        m2 = numofM2 / denaofM2
        m2 = round(m2,3)
      
        numofC = self.getSumOfY() - m1*self.getSumOfX1() - m2*self.getSumOfX2()
        denofC = self.elemCount
        c = numofC / denofC
        c = round(c,3)
        
        return (m1,m2,c)
    
    def displayMultiEqn(self):
        tup = self.getVariablesM1_M2_C()
        valM1 = tup[0]
        valM2 = tup[1]
        valC  = tup[2]
        eqns = 'y= '+ str(valM1) + '*x1' + ' + ' + str(valM2) + '*x2' + ' + ' +str(valC)
        return eqns
    
    if __name__ == "__main__":
       ' main()'
        

##d = {1:(10,20), 2:(20,30), 3:(30,40), 4:(40,50), 5:(50,60), 6:(60,70)}
d = {64:(57,8), 71:(59,10), 53:(49,6), 67:(62,11), 55:(51,8), 58:(50,7),77:(55,10),57:(48,9),56:(52,10),51:(42,6),76:(61,12),68:(57,9)}
##print(d)
ld = MultipleLinearRegression(d)

print(ld.displayMultiEqn())
