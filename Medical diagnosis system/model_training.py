import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os

def train_models():
    # Load dataset
    if not os.path.exists('dataset.csv'):
        print("dataset.csv not found. Please run dataset_generator.py first.")
        return

    df = pd.read_csv('dataset.csv')
    
    # Prepare features and target
    X = df.drop('prognosis', axis=1)
    y = df['prognosis']
    
    # Symptoms list for reference in the app
    symptoms = X.columns.tolist()
    joblib.dump(symptoms, 'models/symptoms_list.pkl')

    # 1. Train RandomForest for Diagnosis
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    y_pred = rf_model.predict(X_test)
    
    print("--- Classification Model Performance ---")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}")
    print(f"Recall: {recall_score(y_test, y_pred, average='weighted'):.4f}")
    print(f"F1-score: {f1_score(y_test, y_pred, average='weighted'):.4f}")
    
    # Save RF model
    joblib.dump(rf_model, 'models/disease_model.pkl')
    print("Diagnosis model saved to models/disease_model.pkl")

    # 2. Train KMeans for Similarity Clustering
    # We'll use the unique disease-symptom matrix for clustering
    disease_matrix = df.groupby('prognosis').mean()
    
    kmeans = KMeans(n_clusters=6, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(disease_matrix)
    
    # Save cluster information
    disease_similarity = {
        'model': kmeans,
        'disease_matrix': disease_matrix,
        'disease_names': disease_matrix.index.tolist(),
        'cluster_labels': clusters.tolist()
    }
    
    joblib.dump(disease_similarity, 'models/cluster_model.pkl')
    print("Clustering model saved to models/cluster_model.pkl")

if __name__ == '__main__':
    if not os.path.exists('models'):
        os.makedirs('models')
    train_models()
