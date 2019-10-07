# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:08:12 2019

@author: Saqib Akhter
y=mx+c Implementation
Sum Y = m * Sum X + n * C
Sum XY = m* Sum X^2 + Sum X * C
m = (Sum Y - n *C) / Sum X
"""

import math
from collections import OrderedDict
import matplotlib.pyplot as plt 

class LinearRegression:
    def __init__(self,Dict):
        print("init")
        self.dict = OrderedDict(Dict);
        self.threshLimit= 1.96 / (math.sqrt(len(Dict)))
        self.elemCount=len(Dict)
        
    def main(self):
        return (self.dict)
    
    def IsLinear(self):
        reg = self.getRegCoeff()
        thr = self.threshLimit
        return reg > thr
    
    'def applyNormalization(): TBD'
    
    def displayEqn(self):
        tup = self.getVariablesM_C()
        valM = tup[0]
        valC = tup[1]
        eqns = 'y= '+ str(valM) + '*x' + '+' +str(valC)
        return eqns
    
    def displayOrigGraph(self):
        listX = []
        listY = []
        i = 0
        for x, y in self.dict.items():
            listX.insert(i,x)
            listY.insert(i,y)
            i = i+1
           
        plt.plot(listX, listY)           
        plt.xlabel('x - axis') 
        plt.ylabel('y - axis') 
          
        plt.title('Graph as per the given data') 
          
        plt.show() 
  
    def displayLinearRegGraph(self):
        listX = []
        listY = []
        i = 0
        for x, y in self.dict.items():
            listX.insert(i,x)
            listY.insert(i,y)
            i = i+1
        
        tup = self.getVariablesM_C()
        valM = tup[0]
        valC = tup[1]      
        
        listY_ = []
        i=0
        for x, y in self.dict.items():
            val = valM * x + valC
            listY_.insert(i,val)
            i = i+1
        
        plt.plot(listX, listY_)  
        plt.scatter(listX, listY_)  
        plt.plot(listX, listY) 
        plt.scatter(listX, listY)          
        plt.xlabel('x - axis') 
        plt.ylabel('y - axis') 
          
        plt.title('Linear Regression') 
          
        plt.show() 
        
    def getVariablesM_C(self):
        numofM = (self.getSumOfXY() * self.elemCount) - (self.getSumOfX() * self.getSumOfY())
        denaofM = (self.elemCount * self.getSumOfXPower2()) - (self.getSumOfX())**2
        m = numofM / denaofM
        m = round(m,3)
        c = (self.getSumOfY() - m * self.getSumOfX())/self.elemCount
        c = round(c,3)
        return (m,c)
        
    def getCovXY(self):
        sum = 0
        for x, y in self.dict.items():
            sum = sum + (x-self.getXMean())*(y-self.getYMean())
        
        return (sum/(self.elemCount - 1))
        
    def getSx(self):
        val = (self.getSumOfX_MinusX_Bar_Pow2()) / (self.elemCount - 1)
        return math.sqrt(val)
      
    def getSy(self):
        val = (self.getSumOfY_MinusY_Bar_Pow2()) / (self.elemCount - 1)
        return math.sqrt(val)
    
    def getRegCoeff(self):
        regCoeff = self.getCovXY() / (self.getSx() * self.getSy())
        return regCoeff
        
    def getSumOfX_MinusX_Bar(self):
        sum = 0
        for x, y in self.dict.items():
            sum = sum + (x - self.getXMean())
        return round(sum,3)   
    
    def getSumOfX_MinusX_Bar_Pow2(self):
        list = []
        i = 0
        for x, y in self.dict.items():
            val = ((x - self.getXMean()))**2
            val = round(val,3)
            list.insert(i,val)
            i = i+1
            
        ret = sum(list)
            
        return round(ret,3) 
    
    def getSumOfY_MinusY_Bar(self):
        list = []
        i=0
        for x, y in self.dict.items():
            val = (y - self.getYMean())
            val = round(val,3)
            list.insert(i,val)
            i = i+1

        ret = sum(list)
        return round(ret,3)  
    
    def getSumOfY_MinusY_Bar_Pow2(self):
        list = []
        i = 0
        for x, y in self.dict.items():
            val = ((y - self.getYMean()))**2
            val = round(val,3)
            list.insert(i,val)
            i = i+1
    
        ret = sum(list)
        return round(ret,3)
    
    def getSumOfX(self):
        val = sum(self.dict.keys())
        return round(val,3) 
    
    def getSumOfY(self):
        val = sum(self.dict.values())
        return round(val,3)
    
    def getSumOfXY(self):
        sum = 0
        for k, v in self.dict.items():
            sum = sum + k*v
        return round(sum,3)
    
    def getSumOfXPower2(self):
        sum = 0
        for i in self.dict:
            sum = sum + i**2
        return round(sum,3)
            
    def getXMean(self):
        val = (sum(self.dict.keys())) / self.elemCount
        return round(val,3)
        
    def getYMean(self):
        val = (sum(self.dict.values())) / self.elemCount
        return round(val,3)
    
    if __name__ == "__main__":
       ' main()'
        

d = {1:10, 2:12, 3:15, 4:17, 5:18, 6:20}
ld = LinearRegression(d)

print(ld.displayEqn())
print(ld.displayLinearRegGraph())

