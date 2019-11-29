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
from Regression import Regression

class LinearRegression(Regression):
    def __init__(self,llist):
        self.llist = llist;
        self.threshLimit= 1.96 / (math.sqrt(len(llist[0])))
        self.elemCount=len(llist[0])
        
    def getThreshLimit(self):
        return round(self.threshLimit,3)
    
    """
    Return True if sample data is linear else False
    """    
    def IsLinear(self):
        reg = self.getRegCoeff()
        thr = self.threshLimit
        return reg > thr
    """
    Display Linear Regression equation with calculated m & c
    """       
    def displayEqn(self):
        tup = self.getCoeffM_C()
        valM = tup[0]
        valC = tup[1]
        eqns = 'y = '+ str(valM) + '*x' + '+' +'('+str(valC)+')'
        return eqns

    """
    Plot graph for Sample Data
    """    
    def displayOrigGraph(self):
        listX = self.llist[1]
        listY = self.llist[0]
           
        plt.plot(listX, listY)           
        plt.xlabel('x - axis') 
        plt.ylabel('y - axis') 
          
        plt.title('Graph as per the given data') 
          
        plt.show() 
 
    """
    Plot graph after applying Linear Regression
    """ 
    def displayLinearRegGraph(self):
        listX = self.llist[1]
        listY = self.llist[0]
        
        tup = self.getCoeffM_C()
        valM = tup[0]
        valC = tup[1]      
        
        listY_ = []
        i=0
        for j in range(self.elemCount):
            val = valM * self.llist[1][j] + valC
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
 
    """
    Return Constant C & variable M as tuble (m,c)
    """        
    def getCoeffM_C(self):
        numofM = (self.getSumOfXY() * self.elemCount) - (self.getSumOfX() * self.getSumOfY())
        denaofM = (self.elemCount * self.getSumOfXPower2()) - (self.getSumOfX())**2
        m = numofM / denaofM
        m = round(m,3)
        c = (self.getSumOfY() - m * self.getSumOfX())/self.elemCount
        c = round(c,3)
        return (m,c)
 
    """
    Return Covariance for X,Y
    """        
    def getCovXY(self):
        sum = 0
        for i in range(self.elemCount):
            sum = sum + (self.llist[1][i]-self.getXMean())*(self.llist[0][i]-self.getYMean())
        
        return (sum/(self.elemCount - 1))
 
    """
    Return Standard Deviation of X
    """        
    def getSx(self):
        val = (self.getSumOfX_MinusX_Bar_Pow2()) / (self.elemCount - 1)
        tmp = math.sqrt(val)
        tmp = round(tmp,3)
        return tmp

    """
    Return Standard Deviation of Y
    """       
    def getSy(self):
        val = (self.getSumOfY_MinusY_Bar_Pow2()) / (self.elemCount - 1)
        tmp = math.sqrt(val)
        tmp = round(tmp,3)
        return tmp
 
    """
    Return Regression Coefficient for X,Y
    """   
    def getRegCoeff(self):
        regCoeff = self.getCovXY() / (self.getSx() * self.getSy())
        tmp = round(regCoeff,3)
        return tmp
 
    """
    Return Sigma (X-X bar)
    """          
    def getSumOfX_MinusX_Bar(self):
        sum = 0
        for x in range(self.elemCount):
            sum = sum + (self.llist[1][x] - self.getXMean())
        return round(sum,3)   
    """
    Return Sigma (X-X bar)^2
    """    
    def getSumOfX_MinusX_Bar_Pow2(self):
        list = []
        i = 0
        for x in range(self.elemCount):
            val = ((self.llist[1][x] - self.getXMean()))**2
            val = round(val,3)
            list.insert(i,val)
            i = i+1
            
        ret = sum(list)
            
        return round(ret,3) 
    """
    Return Sigma (Y-Y bar)
    """     
    def getSumOfY_MinusY_Bar(self):
        list = []
        i=0
        for y in range(self.elemCount):
            val = (self.llist[0][y] - self.getYMean())
            val = round(val,3)
            list.insert(i,val)
            i = i+1

        ret = sum(list)
        return round(ret,3)  
    """
    Return Sigma (Y-Y bar)^2
    """      
    def getSumOfY_MinusY_Bar_Pow2(self):
        list = []
        i = 0
        for y in range(self.elemCount):
            val = ((self.llist[0][y] - self.getYMean()))**2
            val = round(val,3)
            list.insert(i,val)
            i = i+1
    
        ret = sum(list)
        return round(ret,3)
    """
    Return Sigma X
    """      
    def getSumOfX(self):
        val = sum(self.llist[1])
        return round(val,3) 
    """
    Return Sigma Y
    """   
    def getSumOfY(self):
        val = sum(self.llist[0])
        return round(val,3)
    """
    Return Sigma XY
    """   
    def getSumOfXY(self):
        sum = 0
        for i in range(self.elemCount):                
            sum = sum + self.llist[0][i] * self.llist[1][i]
        return round(sum,3)

    """
    Return Sigma X^2
    """    
    def getSumOfXPower2(self):
        sum = 0
        for i in range(len(self.llist[1])):
            sum = sum + (self.llist[1][i])**2
        return round(sum,3)
    """
    Return Mean X
    """            
    def getXMean(self):
        val = (sum(self.llist[1])) / self.elemCount
        return round(val,3)
    """
    Return Mean Y
    """      
    def getYMean(self):
        val = (sum(self.llist[0]) / self.elemCount)
        return round(val,3)
        