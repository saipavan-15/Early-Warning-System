from django.conf import settings
import pandas as pd
import math
# Import modules
import matplotlib.pyplot as mp
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

path = settings.MEDIA_ROOT + "\\" + "dataset.csv"
df = pd.read_csv(path)
df['Genre'].replace({'Female': 0, 'Male': 1}, inplace=True)
df['TypeEtab'].replace({'Public': 0, 'Private': 1}, inplace=True)
df['Niveau'].replace({'Primary': 1, 'Secondary': 2, 'Tertiary': 3}, inplace=True)
df['RetardSco'].replace({'1 year': 1, '2 years': 2, 'None': 0}, inplace=True)
df['Provenance'].replace({'Rural': 1, 'Suburban': 2, 'Urban': 3}, inplace=True)
df['Handicap'].replace({'Yes': 1, 'No': 0}, inplace=True)
df['SocialAid'].replace({'Yes': 1, 'No': 0}, inplace=True)
df['Result'].replace({'Pass': 0, 'Fail': 1}, inplace=True)

X = df.iloc[:, :-1].values  # indipendent variable
y = df.iloc[:, -1].values  # Dependent variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)


def knnResults():
    from sklearn.neighbors import KNeighborsRegressor
    knn = KNeighborsRegressor()
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    mae = mean_absolute_error(y_pred, y_test)
    rmse = math.sqrt(mae)
    r2_knn = r2_score(y_pred,y_test)
    print(f"KNN Results MAE:{mae} RMSE: {rmse} R2-Score:{r2_knn}")
    # print(self.df.head())
    return {'mae':mae, 'rmse':rmse, 'r2_knn':r2_knn}


def randomForest():
    from sklearn.ensemble import RandomForestRegressor
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    mae = mean_absolute_error(y_pred, y_test)
    rmse = math.sqrt(mae)
    r2_knn = r2_score(y_pred,y_test)
    print(f"RandomForest Results MAE:{mae} RMSE: {rmse} R2-Score:{r2_knn}")
    return {'mae':mae, 'rmse':rmse, 'r2_knn':r2_knn}


def svmAlgorithm():
    from sklearn.svm import SVR
    svm = SVR()
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_test)
    mae = mean_absolute_error(y_pred, y_test)
    rmse = math.sqrt(mae)
    r2_knn = r2_score(y_pred,y_test)
    print(f"SVM Results MAE:{mae} RMSE: {rmse} R2-Score:{r2_knn}")
    return {'mae':mae, 'rmse':rmse, 'r2_knn':r2_knn}


def sgdAlgorithm():
    from sklearn.linear_model import SGDRegressor
    sgd = SGDRegressor(max_iter=1000, alpha=0.0001, l1_ratio=0.15, learning_rate='invscaling', random_state=42)
    sgd.fit(X_train, y_train)
    y_pred = sgd.predict(X_test)
    mae = mean_absolute_error(y_pred, y_test)
    rmse = math.sqrt(mae)
    r2_knn = r2_score(y_pred,y_test)
    print(f"SGD Results MAE:{mae} RMSE: {rmse} R2-Score:{r2_knn}")
    return {'mae':mae, 'rmse':rmse, 'r2_knn':r2_knn}


def corrGraph():
    print(df.corr())
    # Displaying heatmap
    # fig, ax = mp.subplots(figsize=(15, 10))
    # dataplot = sb.heatmap(df.corr(), annot=True, linewidths=.5, ax=ax)
    # mp.savefig("assets/static/images/corr.png")
    # mp.show()
