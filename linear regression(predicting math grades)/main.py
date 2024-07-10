import pandas as pd 
import numpy as np 
import sklearn 
from sklearn import linear_model
import sklearn.model_selection
from sklearn.utils import shuffle

data = pd.read_csv("linear regression(predicting math grades)/student+performance(dataset)/student/student-math class.csv", sep = ";")

for x in range(len(data["schoolsup"])):
    if data["schoolsup"][x] == "yes":
        data["schoolsup"][x] = 1
    elif data["schoolsup"][x] == "no":
        data["schoolsup"][x] = 0
for x in range (len(data["paid"])):
    if data["paid"][x] == "yes":
        data["paid"][x] = 1
    elif data["paid"][x] == "no":
        data["paid"][x] = 0


data = data [["G1", "G2", "G3", "studytime", "failures", "schoolsup", "paid", "absences"]] #cuts out all the columns and only includes the ones we care about

predict = "G3" #label, it is defining which attribute we are trying to predict, in this case it is grade #3

x = np.array(data.drop([predict], 1)) #makes an array of all the attributes, except the label
y = np.array(data[predict]) #only the G3 values of each row/student

x_train,x_test,y_train, y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)
#^takes all the attributes and labels and splits into 4 arrays. test_size = 0.1 makes 10% of data into test samples

linear = linear_model.LinearRegression() #creating the model
linear.fit(x_train, y_train) #finds a best fit line using the training data and stores that line in linear 

accuracy = linear.score(x_test, y_test) #returns a value that defines the accuracy of the model
print ("accuracy of the model is: ", accuracy)

print("cooefficients: ", linear.coef_) #prints the coefficents, like m in y=mx+b only 1 cooefficent is printed if the line is in 2D space, if the space has more dimensions then more coefficents
print("intercept: ", linear.intercept_) #prints the intercept, like b in y=mx + b

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])