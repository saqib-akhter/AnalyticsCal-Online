#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Text
from tkinter import filedialog as fd
from tkinter import messagebox as msg
from LinearRegression import LinearRegression as LinearRegr
from MultipleRegression import MultipleLinearRegression as MultiLinearRegr
from Regression import Regression
from csvToDict import csvToDict
from mpl_toolkits.mplot3d import Axes3D

import os
import math
import copy
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import plot, ion, show
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class InitDict:
    def __init__(self):
        self.dict = {};
        self.listX = []
        self.listY = []
        self.header_x = ""
        self.header_y = ""
        self.nvar = 2
    def initializeDict(self,Dict,listX,listY,header_x,header_y,nvar):
        self.dict = Dict
        self.listX = listX
        self.listY = listY
        self.header_x = header_x
        self.header_y = header_y
        self.nvar = nvar
        
    def getDict(self):
        return self.dict
    def getListX(self):
        return self.listX
    def getListY(self):
        return self.listY
    def getHeader_x(self):
        return self.header_x
    def getHeader_y(self):
        return self.header_y
    def getNoOfVar(self):
        return self.nvar
        
# Create instance
win = tk.Tk()   
myDict = InitDict()

# Add a title       
win.title("AnalyticsCal")
win.resizable(True, True) 

#-------------------------------------------------------------------------Plots

def reg_plot(x_plot,y_plot,y_predicted, equation_str, title, x_label, y_label, color = None):

    
    var = myDict.getNoOfVar()

    if(var == 2):   
        plt.clf()
        ion()
        raw_plot = plt.scatter(x_plot, y_plot, color = 'b')
        predict_plot = plt.plot(x_plot,y_predicted , '-',color = color)
        plt.title(title)					
        plt.xlabel(x_label)					
        plt.ylabel(y_label)
        plt.legend((raw_plot, predict_plot),('Raw Data', 'Prediction equation = ' + equation_str),loc=(-0.05,-0.20), scatterpoints=1, ncol=3, fontsize=8)
        plt.legend(fontsize='x-large')
        equation_str = 'Prediction equation : ' + equation_str
        
        plt.figtext(0.1, 0.009, equation_str, wrap=True, horizontalalignment='left', fontsize=12, clip_on=True)
        #fig = plt.figure()
        #fig.text(.5, .05, equation_str, ha='center')
        plt.tight_layout()
        plt.show()
    else:
        pass
    '''        
    elif(var == 3):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d') 
        p=ax.plot(x_plot[0],x_plot[1],y_predicted , c='b',marker='o')
        r=ax.scatter(x_plot[0], x_plot[0], y_plot, c='r', marker='o')
        ax.set_xlabel(x_label[0])
        ax.set_ylabel(x_label[1])
        ax.set_zlabel(y_label)
        ax.legend((r, p),('Raw Data', 'Prediction equation = ' + equation_str),loc=(-0.05,-0.20), scatterpoints=1, ncol=3, fontsize=8)
        plt.show()
    '''
    

    
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
# Menu
# Open file

def open_file():

    file = fd.askopenfile(mode='r', filetypes=[('CSV Files', '*.csv')]) # gets the filename as string
    if file:
        file_name = file.name
    print(file_name)
    dataDict,listX,listY,header_x,header_y,var = csvToDict(file_name)
    myDict.initializeDict(dataDict,listX,listY,header_x,header_y,var)

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit() 
    
# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command = open_file)
#file_menu.add_separator()
file_menu.add_command(label="Recent Files")
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------

tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Normal Analysis')      # Add the tab

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# LabelFrame using tab1 as the parent - for basic data Analysis
mighty = ttk.LabelFrame(tab1, text=' Basic Data Analysis')
mighty.grid(column=0, row=0, padx=8, pady=4)

# LabelFrame using tab1 as the parent - for output console
mighty1 = ttk.LabelFrame(tab1, text=' Output Console')
mighty1.grid(column=1, row=0,sticky=tk.N+tk.S, padx=16, pady=12, columnspan=7, rowspan = 10)


# Add big textbox
text_h= 20
text_w = 60
textBox = tk.Text(mighty1, height = text_h, width = text_w,wrap=tk.WORD)
textBox.grid(column=0, row=10, sticky=tk.N+tk.S)

textBox.pack(expand=True, fill='both')


# Modified Button statistics Function
def click_stats(textBox):
    textBox.delete(1.0, tk.END) # clear anything previously present
    ret = getStats()
    if(myDict.getNoOfVar() ==2):
        if(ret[4].IsLinear() != True):
            _stats_msgBox()

# stats_msgBox: Alert the user when corr_coeff < threshold
def _stats_msgBox():
    msg.INFO('AnalyticsCal Alert'," It appears that the data is not linear.")
    
mighty_width = 26
# Add button to output basic statistics
Statistics = ttk.Button(mighty, text="Statistics", command= lambda : click_stats(textBox), width = mighty_width)   
Statistics.grid(column=0, row=0, sticky='W')
#----------------------------------------------------------------------Basic Plot
# Modified Button Click Plot
def click_plot():
    ion()
    print(myDict.getNoOfVar)
    if(myDict.getNoOfVar() == 2):
        plt.scatter(myDict.getListX(), myDict.getListY(),alpha=1)					
        plt.title('Scatter plot of x and y')					
        plt.xlabel(myDict.getHeader_x())					
        plt.ylabel(myDict.getHeader_y())
        plt.tight_layout()
        plt.show()
    elif(myDict.getNoOfVar() == 3):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        mylist = myDict.getListX()
        ax.scatter(mylist[0], mylist[0], myDict.getListY(), c='r', marker='o')
        lab = myDict.getHeader_x()
        ax.set_xlabel(lab[0])
        ax.set_ylabel(lab[1])
        ax.set_zlabel(myDict.getHeader_y())
        plt.show()
    else:
        pass
# Add button for plot
plot = ttk.Button(mighty, text="Plot", command=click_plot, width = mighty_width)   
plot.grid(column=0, row=1, sticky='W')
#----------------------------------------------------------------------Linear Regression
def click_linear_regression():
    stats = getStats()  
    reg_plot(stats[0],stats[1],stats[2], stats[3], "LinearRegression", myDict.getHeader_x(), myDict.getHeader_y())
    

# Add button to Regression
linear_Regression = ttk.Button(mighty, text="Linear Regression", command=click_linear_regression,width = mighty_width)   
linear_Regression.grid(column=0, row=2, sticky='W')

def clearScreen():
     textBox.delete(1.0, tk.END)
# Add button to cleanup console
clearscr = ttk.Button(mighty, text="Reset", command=clearScreen,width = mighty_width)   
clearscr.grid(column=0, row=3, sticky='W')
    

def getStats():
    dic = myDict.getDict()
    listX = myDict.getListX()
    listY = myDict.getListY()
    listY_predicted = []  
    eqn = ""
    regObj = Regression()
    textBox.delete(1.0, tk.END)
    
    if(myDict.getNoOfVar() == 2):
        regObj = LinearRegr(dic)
        m,c=regObj.getCoeffM_C()
        for x, y in dic.items():
            val = m * x + c
            listY_predicted.append(val)
    
        eqn = regObj.displayEqn()
        textBox.insert(tk.INSERT, 'Regression equation: '+ eqn +'\n')
        textBox.insert(tk.INSERT, 'Threshold Limit is '+ (str(regObj.getThreshLimit())+'\n'))
        textBox.insert(tk.INSERT, "Mean of X is "+ str(regObj.getXMean()) +'\n')
        textBox.insert(tk.INSERT, 'Mean of Y is '+ (str(regObj.getYMean())+'\n'))
        textBox.insert(tk.INSERT, 'Standard Deviation of X = '+ (str(regObj.getSx())+'\n'))
        textBox.insert(tk.INSERT, 'Standard Deviation of Y = '+ (str(regObj.getSy())+'\n'))
        textBox.insert(tk.INSERT, 'Correlation Coefficient r(xy) = '+ (str(regObj.getRegCoeff())+'\n'))
    elif(myDict.getNoOfVar() == 3):
        regObj = MultiLinearRegr(dic)
        m1,m2,c=regObj.getCoeffM1_M2_C()
  
        for k, v in dic.items():
            val = m1 * v[0] + m2*v[1] + c
            listY_predicted.append(val)
    
        eqn = regObj.displayMultiEqn() 
        textBox.insert(tk.INSERT, 'Regression equation: '+ eqn +'\n')
        textBox.insert(tk.INSERT, 'Threshold Limit is '+ (str(regObj.getThreshLimit())+'\n'))
        textBox.insert(tk.INSERT, 'Mean of X1 is '+ (str(regObj.getX1Mean())+'\n'))
        textBox.insert(tk.INSERT, 'Mean of X2 is '+ (str(regObj.getX2Mean())+'\n'))
        textBox.insert(tk.INSERT, 'Mean of Y is '+ (str(regObj.getYMean())+'\n'))
        textBox.insert(tk.INSERT, 'Standard Deviation of X1 = '+ (str(regObj.getSx1())+'\n'))
        textBox.insert(tk.INSERT, 'Standard Deviation of X2 = '+ (str(regObj.getSx2())+'\n'))
        textBox.insert(tk.INSERT, 'Standard Deviation of Y = '+ (str(regObj.getSy())+'\n'))
        textBox.insert(tk.INSERT, 'Partial Correlation Coefficient r(yx1).x2 = '+ (str(regObj.getRYx1_x2())+'\n'))
        textBox.insert(tk.INSERT, 'Partial Correlation Coefficient r(yx2).x1 = '+ (str(regObj.getRYx2_x1())+'\n'))
        textBox.insert(tk.INSERT, 'Partial Correlation Coefficient r(yx1) = '+ (str(regObj.getRyx1())+'\n'))
        textBox.insert(tk.INSERT, 'Partial Correlation Coefficient r(yx2) = '+ (str(regObj.getRyx2())+'\n'))
        textBox.insert(tk.INSERT, 'Partial Correlation Coefficient r(x1x2) = '+ (str(regObj.getRx1x2())+'\n'))
    else:
        pass
    
    return listX,listY,listY_predicted,eqn,regObj
#======================
# Start GUI
#======================
win.mainloop()
