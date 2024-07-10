import pandas as pd 
import numpy as np 
import sklearn 
from sklearn import linear_model
import sklearn.model_selection
from sklearn.utils import shuffle

data = pd.read_csv("song popularity predictor/archive (3)/1950.csv")

dict = {}
num = 1
for x in range(len(data["top genre"])):
    if data["top genre"][x] in dict:
        pass
    else:
        dict[data["top genre"][x]] = num
        num = num + 1

for x in range(len(data["top genre"])):
    if data["top genre"][x] in dict:
        data["top genre"][x] = dict[data["top genre"][x]]


data = data[["top genre", "bpm", "nrgy", "dnce", "live", "val","acous", "spch", "popularity"]]

predict = "popularity"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train,x_test,y_train, y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)

accuracy = linear.score(x_test, y_test)
print("accuracy of the model is: ", accuracy)
