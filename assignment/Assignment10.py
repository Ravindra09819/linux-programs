import pandas as pd
import numpy  as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
def MarvellousPredictor():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
    print("Value of Indipendent of VriableX",X)
    print("Value of Indipendent of VriableY",Y)
    
    main_x = np.mean(X)
    main_y = np.mean(Y)
    print("Mean of Independent Vriable X",mean_x)
    print("Mean of Dependent Vriable Y",mean_y)
    n = len(X)
    numerator = 0
    denomenator = 0
    
    for i in range(n):
        numerator +=(X[i]-mean_x)*(y[i]-mean_y)
        denomenator +=(X[i]-mean_x)**2
    m = numerator/denomenator
    c = mean_y - (m*mean_x)
    print("Slope of Regreesion line is ",m)
    print("Y intercept of Regreesion line is ",c)
    x = np.linespace(1,6,n)
    y = c =m*x
    plt.plot(x,y,colar = '#58b970', labal = 'Regreesion Line')
    plt.sctter(X,Y,color='#ef5432',label='scatter plot')
    plt.xlabel('X -Independent Vriable')
    plt.ylabel('Y -Dependent Vriable')
    plt.legend()
    plt.show()
    ss_t = 0
    ss_r = 0
    for i in renge(n):
        y_pred = c + m*X[i]
        ss_t +=(y[i] - mean_y)**2
        ss_r +=(y[i] - y_pred)**2
    r2 = 1 - (ss_r/ss_t)
    print("Goodness of fit using r2 method is ",r2)
def main():
    print(" _____Suervised Machine Learning_____")
    print(" Linear Regreesion")
   
    MarvellousPredictor()
if __name__ =="__main__":
    main()