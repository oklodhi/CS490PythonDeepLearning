import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier

## read the csv
data = pd.read_csv('glass.csv')

## print basic information about data such as what values it holds and data description
print(data.columns.values)
print('_'*100)
print(data[data.isnull().any(axis=1)])
print('_'*100)
#print(data.info())
#print('_'*100)
print(data.corr())

## make x and y axis vairables
xaxis = data.drop('Type', axis=1)
yaxis = data['Type']

#print(xaxis)
#print(yaxis)

## main SVC method implementation
xtrain, xtest, ytrain, ytest = train_test_split(xaxis, yaxis, test_size=0.3, random_state=0, stratify=yaxis)
svc = SVC()
svc.fit(xtrain, ytrain)
yprediction = svc.predict(xtest)

## print off accuracy for model
finalsvc = round(svc.score(xtest, ytest)*100, 2)
print("svm accuracy is:", finalsvc, "%")
print("_"*100)
print(classification_report(ytest, yprediction))