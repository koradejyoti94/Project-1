import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
#sns.countplot(x='Survived',data=titanic_data)
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def MarvellousTitanicLogistic():
    #step 1:load data
    titanic_data=pd.read_csv(r"C:\Users\Administrator\Desktop\Python\titanic.csv")

    print("first 5 entries from loaded dataset")
    print(titanic_data.head())

    print("Number of passangers are"+str(len(titanic_data)))
    ax=sns.countplot(x='Survived',data=titanic_data)

    #step 2:Analyze data
    print("visualization:survived and non survived passenger")
    figure()
    target="Survived"

    countplot(data=titanic_data,x=target).set_title("Marvellous imfosystem:survived and non survived passenger")
    show()

    print("visualization:survived and non survived passanger based on gender")
    figure()
    target="Survived"

    countplot(data=titanic_data,x=target,hue="Sex").set_title("Marvellous Infosystem:Survived and non survied passanger based on gender")
    show()

    print("visualization:survived and non survied passanger based on the passenger class")
    figure()
    target="Survived"

    countplot(data=titanic_data,x=target,hue="Pclass").set_title("Marvellous Infosystem: Survived and non survived passengers based on the passanger class")
    show()

    print("Visualisation:Survived and non survived passangers based on the age")
    figure()
    titanic_data["Age"].plot.hist().set_title("Marvellous Infosystem:survived and non survied passangers based on age")
    show()
    print("Visualisation:Survived and non survied passangers based on the fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Marvellous Infosystem:survived and non survived passangers based on fare")
    show()
    #step 3:Data cleaining
    titanic_data.drop(['zero'],axis=1 ,inplace=True)

    print("First five entries from loaded dataset after removing zero column")
    print(titanic_data.head(5))

    print("Values of sex column")
    print(pd.get_dummies(titanic_data['Sex']))

    print("Values of sex column after removing one field")
    Sex=pd.get_dummies(titanic_data["Sex"],drop_first=True)
    print(Sex.head(5))

    print("Values of Pclass column after removing one field")
    Pclass=pd.get_dummies(titanic_data["Pclass"],drop_first=True)
    print(Pclass.head(5))
    print("Values of dataset after concatenating new columns")
    titanic_data=pd.concat([titanic_data,Sex,Pclass],axis=1)
    print(titanic_data.head(5))

    print("Values of dataset after removing irrelevent columns")
    titanic_data.drop(["Sex","sibsp","Parch","Embarked"],axis=1,inplace=True)
    print(titanic_data.head(5))

    x=titanic_data.drop("Survived",axis=1)
    y=titanic_data["Survived"]

    #step 4:Data training
    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5)
    logmodel=LogisticRegression()
    logmodel.fit(xtrain,ytrain)
    #step 4:Data testing
    prediction=logmodel.predict(xtest)

    #step 5:Calculate Accuracy

    print("Classification report of logistic regression is:")
    print(classification_report(ytest,prediction))
    print("Confusion matrix of logistic regrssion is:")
    print(confusion_matrix(ytest,prediction))
    print("Accuracy of logistic regression is:")
    print(accuracy_score(ytest,prediction))
def main():
    print("Supervised machine learining")
    print("Logistic Regression on Titanic data set")
    MarvellousTitanicLogistic()

if __name__=="__main__":
    main()











