# users/algorithms.py
import os
import pandas as pd
import numpy as np
from django.conf import settings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import matplotlib
matplotlib.use('Agg')   # no GUI
import matplotlib.pyplot as plt
import seaborn as sns

MODEL_DIR = os.path.join(settings.MEDIA_ROOT, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

class ImplementAlgorithmsCodes:
    @staticmethod
    def _load_df(path=None):
        if path is None:
            path = os.path.join(settings.MEDIA_ROOT, "dataset.csv")
        df = pd.read_csv(path)
        return df

    @staticmethod
    def _preprocess(df):
        # Use the same mappings you used before
        df = df.copy()
        df['Genre'].replace({'Female': 0, 'Male': 1}, inplace=True)
        df['TypeEtab'].replace({'Public': 0, 'Private': 1}, inplace=True)
        df['Niveau'].replace({'Primary': 1, 'Secondary': 2, 'Tertiary': 3}, inplace=True)
        df['RetardSco'].replace({'1 year': 1, '2 years': 2, 'None': 0}, inplace=True)
        df['Provenance'].replace({'Rural': 1, 'Suburban': 2, 'Urban': 3}, inplace=True)
        df['Handicap'].replace({'Yes': 1, 'No': 0}, inplace=True)
        df['SocialAid'].replace({'Yes': 1, 'No': 0}, inplace=True)
        # Convert Result: Pass -> 0, Fail -> 1  (as your code used)
        df['Result'].replace({'Pass': 0, 'Fail': 1}, inplace=True)
        # If any NaNs in numeric columns, fill simple strategy
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        return df

    @staticmethod
    def _split(df):
        X = df.drop(columns=['Result'])
        y = df['Result']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
        return X_train, X_test, y_train, y_test

    @staticmethod
    def _scale(X_train, X_test):
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        # save scaler
        joblib.dump(scaler, os.path.join(MODEL_DIR, "scaler.joblib"))
        return X_train_scaled, X_test_scaled

    @staticmethod
    def _metrics(model, X_test, y_test):
        y_pred = model.predict(X_test)
        return {
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "precision": float(precision_score(y_test, y_pred, zero_division=0)),
            "recall": float(recall_score(y_test, y_pred, zero_division=0)),
            "f1": float(f1_score(y_test, y_pred, zero_division=0))
        }

    @staticmethod
    def train_models(save_models=True):
        df = ImplementAlgorithmsCodes._load_df()
        df = ImplementAlgorithmsCodes._preprocess(df)
        X_train, X_test, y_train, y_test = ImplementAlgorithmsCodes._split(df)
        X_train_s, X_test_s = ImplementAlgorithmsCodes._scale(X_train, X_test)

        results = {}

        # KNN
        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(X_train_s, y_train)
        results['knn'] = ImplementAlgorithmsCodes._metrics(knn, X_test_s, y_test)
        if save_models:
            joblib.dump(knn, os.path.join(MODEL_DIR, "knn.joblib"))

        # Random Forest
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(X_train, y_train)   # RF works fine without scaling
        results['rf'] = ImplementAlgorithmsCodes._metrics(rf, X_test, y_test)
        if save_models:
            joblib.dump(rf, os.path.join(MODEL_DIR, "rf.joblib"))

        # SVM (slow on big data — probability=True if you need predict_proba)
        svm = SVC(probability=True, kernel='rbf', random_state=42)
        svm.fit(X_train_s, y_train)
        results['svm'] = ImplementAlgorithmsCodes._metrics(svm, X_test_s, y_test)
        if save_models:
            joblib.dump(svm, os.path.join(MODEL_DIR, "svm.joblib"))

        # SGD
        sgd = SGDClassifier(max_iter=1000, tol=1e-3, random_state=42)
        sgd.fit(X_train_s, y_train)
        results['sgd'] = ImplementAlgorithmsCodes._metrics(sgd, X_test_s, y_test)
        if save_models:
            joblib.dump(sgd, os.path.join(MODEL_DIR, "sgd.joblib"))

        return results

    @staticmethod
    def knnResults():
        # train quick and return KNN result (keeps interface your view expects)
        res = ImplementAlgorithmsCodes.train_models(save_models=True)
        return res.get('knn', {})

    @staticmethod
    def randomForest():
        res = ImplementAlgorithmsCodes.train_models(save_models=True)
        return res.get('rf', {})

    @staticmethod
    def svmAlgorithm():
        res = ImplementAlgorithmsCodes.train_models(save_models=True)
        return res.get('svm', {})

    @staticmethod
    def sgdAlgorithm():
        res = ImplementAlgorithmsCodes.train_models(save_models=True)
        return res.get('sgd', {})

    @staticmethod
    def corrGraph():
        df = ImplementAlgorithmsCodes._load_df()
        df = ImplementAlgorithmsCodes._preprocess(df)
        corr = df.corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
        out = os.path.join(settings.MEDIA_ROOT, "corr.png")
        plt.tight_layout()
        plt.savefig(out)
        plt.close()
        return out
