
# coding: utf-8

"""
Created on Wed Oct 9 10:15:19 2019
@author: Saqib Akhter
Multiple (3 variable) Regression
y= m1x1 + m2x2 + c Implementation
Sum YX1 = m1*Sum X1^2 + m2*Sum (X1*X2) + C*Sum X1
Sum YX2 = m2*Sum X2^2 + m1*Sum (X1*X2) + C*Sum X2
Sum Y   = m1*Sum X1   + m2*Sum X2 + C*n
"""

import math
from collections import OrderedDict
from Regression import Regression
from LinearRegression import LinearRegression as LR
  
class MultipleLinearRegression(Regression):
    def __init__(self,Dict):
        self.dict = OrderedDict(Dict);
        self.threshLimit= 1.96 / (math.sqrt(len(Dict)))
        self.elemCount=len(Dict)

    def getThreshLimit(self):
        return round(self.threshLimit,3)
    
    def getDictYX1(self):
        tup= self.get2PairDict()
        return tup[0]

    def getDictYX2(self):
        tup= self.get2PairDict()
        return tup[1]
    
    def getDictX1X2(self):
        tup= self.get2PairDict()
        return tup[2]
      
    def get2PairDict(self):
        dict_yx1 = {}
        dict_yx2 = {}
        dict_x1x2 = {}
        for k, v in self.dict.items():
            dict_yx1.update({v[0]:k})
            dict_yx2.update({v[1]:k})
            dict_x1x2.update({v[0]:v[1]})
        return dict_yx1,dict_yx2,dict_x1x2

    def getRyx1(self):
        regObj = LR(self.getDictYX1())
        val = regObj.getRegCoeff()
        return round(val,3)
    
    def getRyx2(self):
        regObj = LR(self.getDictYX2())
        val = regObj.getRegCoeff()
        return round(val,3)
  
    def getRx1x2(self):
        regObj = LR(self.getDictX1X2())
        val = regObj.getRegCoeff()
        return round(val,3)

    def getRYx1_x2(self):
        rval = (self.getRyx1() - self.getRyx2() * self.getRx1x2()) / math.sqrt((1-(self.getRyx2())**2)*(1-(self.getRx1x2())**2))
        return round(rval,3)
    def getRYx2_x1(self):
        rval = (self.getRyx2() - self.getRyx1() * self.getRx1x2()) / math.sqrt((1-(self.getRyx1())**2)*(1-(self.getRx1x2())**2))
        return round(rval,3)
       
    def getSx1(self):
        list = []
        for k, v in self.dict.items():
            val = (v[0] - self.getX1Mean())**2
            val = round(val,3)
            list.append(val)
            
        ret = sum(list)
        sx1 = math.sqrt(ret / self.elemCount-1) 
        return round(sx1,3)  

    def getSx2(self):
        list = []
        for k, v in self.dict.items():
            val = (v[1] - self.getX2Mean())**2
            val = round(val,3)
            list.append(val)
            
        ret = sum(list)
        sx2 = math.sqrt(ret / self.elemCount-1) 
        return round(sx2,3) 
 
    def getSy(self):
        list = []
        for k, v in self.dict.items():
            val = (k - self.getYMean())**2
            val = round(val,3)
            list.append(val)
            
        ret = sum(list)
        sy = math.sqrt(ret / self.elemCount-1) 
        return round(sy,3) 
    
    def getX1Mean(self):
        val = self.getSumOfX1() / self.elemCount
        return round(val,3)

    def getX2Mean(self):
        val = self.getSumOfX2() / self.elemCount
        return round(val,3)
    
    def getYMean(self):
        val = (sum(self.dict.keys())) / self.elemCount
        return round(val,3)
    
    def getSumOfX1(self):
        val = 0
        for i in self.dict.items(): 
            val = val + i[1][0] 
        return round(val,3) 

    def getSumOfX2(self):
        val = 0
        for i in self.dict.items(): 
            val = val + i[1][1] 
        return round(val,3) 
    
    def getSumOfY(self):
        val = sum(self.dict.keys())
        return round(val,3)
    
    def getSumOfX1Y(self):
        _sum = 0
        for k, v in self.dict.items():
            _sum = _sum + k*v[0]

        return round(_sum,3)
    
    def getSumOfX2Y(self):
        _sum = 0
        for k, v in self.dict.items():
            _sum = _sum + k*v[1]

        return round(_sum,3)
    
    def getSumOfX1X2(self):
        _sum = 0
        for k, v in self.dict.items():
            _sum = _sum + (v[0]*v[1])

        return round(_sum,3)    
      
    def getSumOfX1Power2(self):
        _sum = 0
        for k, v in self.dict.items():
            _sum = _sum + v[0]**2
            
        return round(_sum,3)

    def getSumOfX2Power2(self):
        _sum = 0
        for k, v in self.dict.items():
            _sum = _sum + v[1]**2
            
        return round(_sum,3)
    
    def getCoeffM1_M2_C(self):
        a1= (self.elemCount * self.getSumOfX1X2()) - (self.getSumOfX1() * self.getSumOfX2())
        a2= (self.elemCount * self.getSumOfX1Power2()) - (self.getSumOfX1())**2
        a3= (self.elemCount * self.getSumOfX1Y()) - (self.getSumOfX1() * self.getSumOfY())
        a4= (self.elemCount * self.getSumOfX2Power2()) - (self.getSumOfX2())**2
        a5= (self.elemCount * self.getSumOfX1X2()) - (self.getSumOfX1() * self.getSumOfX2())
        a6= (self.elemCount * self.getSumOfX2Y()) - (self.getSumOfX2() * self.getSumOfY())

        numofM2 = a2*a6 - a3*a5
        denaofM2 = a2*a4 - a1*a5
        m2 = numofM2 / denaofM2
        m2 = round(m2,3)
        
        m1 = (a6 / a5) - ((a4/a5)*m2)
        m1 = round(m1,3)
      
        numofC = self.getSumOfY() - m1*self.getSumOfX1() - m2*self.getSumOfX2()
        denofC = self.elemCount
        c = numofC / denofC
        c = round(c,3)
        
        return (m1,m2,c)
    
    def displayMultiEqn(self):
        tup = self.getCoeffM1_M2_C()
        valM1 = tup[0]
        valM2 = tup[1]
        valC  = tup[2]
        eqns = 'y = '+ '('+str(valM1) +')'+ '*x1' + ' + ' + '('+str(valM2) +')'+ '*x2' + ' + ' +'('+str(valC)+')'
        return eqns      
        
'''
d = {64:(57,8), 71:(59,10), 53:(49,6), 67:(62,11), 55:(51,8), 58:(50,7),77:(55,10),57:(48,9),56:(52,10),51:(42,6),76:(61,12),68:(57,9)}
ld = MultipleLinearRegression(d)
print(ld.getSy())
'''
