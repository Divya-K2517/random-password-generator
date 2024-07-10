import sklearn
import sklearn.model_selection
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("cars_K-Nearest Neighbors/car.data")

a = preprocessing.LabelEncoder() #replaces non numerical values with numbers

buying = a.fit_transform(list(data["buying"])) #turns the entire buying column into a list, and then transforms then into integer values, returns an array
maint = a.fit_transform(list(data["maint"]))
door = a.fit_transform(list(data["door"]))
persons = a.fit_transform(list(data["persons"]))
lug_boot = a.fit_transform(list(data["lug_boot"]))
safety = a.fit_transform(list(data["safety"]))
cls = a.fit_transform(list(data["class"]))

predict = "class" #label
x = list(zip(buying, maint, door, persons, lug_boot, safety)) #zip produces tuples where each element in the tupe is a value from one of the columns
y = list(cls)


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y, test_size=0.1)

bot = KNeighborsClassifier(n_neighbors=9)
bot.fit(x_train, y_train)

acc = bot.score(x_test, y_test)
print("accuracy of the model is: ", acc)

predicted = bot.predict(x_test) #returns a array
names = ["unacc", "acc", "good", "vgood"]
print(predicted)

for x in range(len(predicted)):
    print("predicted: ", names[predicted[x]], "data: ", x_test[x], "acutal: ", names[y_test[x]])
    n = bot.kneighbors_graph([x_test[x]], 9, "distance")
    print(n)
