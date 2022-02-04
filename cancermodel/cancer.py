import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

logreg=LogisticRegression(max_iter=50000)

data=pd.read_csv(r'ml_health\cancermodel\cancer.csv')
data.drop(["Unnamed: 32"],axis="columns",inplace=True)
data.drop(["id"],axis="columns",inplace=True)
a=pd.get_dummies(data["diagnosis"])
cancer=pd.concat([data,a],axis="columns")
cancer.drop(["diagnosis","B"],axis="columns",inplace=True)
cancer.rename(columns={"M":"Malignant/Benign"},inplace=True)
y=cancer[["Malignant/Benign"]]
X=cancer.drop(["Malignant/Benign"],axis="columns")
print(X.shape[1])

X=np.array(X)
y=np.array(y)

logreg.fit(X,y.reshape(-1,))

joblib.dump(logreg,"cancer_model")


