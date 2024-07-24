import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#path="C://Users//Administrator//Desktop//Python//insurance_data.csv"
def MarvellousLogistic(path):
    df=pd.read_csv(path)
    print("_"*50)
    print("First 5 entries of dataset")
    print(df.head())
    print("_"*50)
    plt.scatter(df.age,df.bought_insurance,marker='+',color='red')
    plt.show()
    X_train,X_test,y_train,y_test=train_test_split(df[['age']],df.bought_insurance,train_size=0.5)
    print("Independant variable for training:")
    print(X_train)
    print("_"*50)
    print("Dependent variable for training:")
    print(y_train)
    print("_*50")
    print("Independent variable for testing:")
    print(X_test)
    print("_"*50)
    print("Dependent variab;e for testing:")
    print(y_test)
    model=LogisticRegression()
    model.fit(X_train,y_train)
    print("_"*50)
    print("Expected dependent variable:")
    print(y_test)
    print("_"*50)
    data=model.predict_proba(X_test)
    print("Probability of above model is:")
    print(data)
    print("_"*50)
    print("Classification report classification_report of Logistic regression is:")
    print(classpfication_report(y_test,y_predicted))
    print("_"*50)
    print("Confusion matrix of Logistic Regression is:")
    print(confusion_matrix(y_test,y_predicted))
    print("_"*50)
    print("Accuracy of logistic regression is:")
    print(accuracy_score(y_test,y_predicted))
def main():
    print("_"*50)
    print("Supervised machine learining")
    print("Logistic regression on Insurance set")
    print("_"*50)
MarvellousLogistic("C://Users//Administrator//Desktop//Python//insurance_data.csv")
if __name__=="__maim__":
  main()
