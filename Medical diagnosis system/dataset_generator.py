import pandas as pd
import numpy as np
import random
import os

def generate_dataset(n_samples=3000):
    # Define 50 symptoms
    symptoms = [
        'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering',
        'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
        'vomiting', 'burning_micturition', 'spotting_urination', 'fatigue', 'weight_gain',
        'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
        'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever',
        'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion',
        'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite',
        'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
        'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure',
        'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision'
    ]

    # Define 20 diseases and their primary symptoms
    diseases = {
        'Fungal infection': ['itching', 'skin_rash', 'nodal_skin_eruptions'],
        'Allergy': ['continuous_sneezing', 'shivering', 'chills'],
        'GERD': ['stomach_pain', 'acidity', 'ulcers_on_tongue', 'vomiting'],
        'Chronic cholestasis': ['itching', 'vomiting', 'yellowish_skin', 'nausea', 'loss_of_appetite'],
        'Drug Reaction': ['itching', 'skin_rash', 'stomach_pain', 'burning_micturition', 'spotting_urination', 'patches_in_throat'],
        'Peptic ulcer diseae': ['vomiting', 'indigestion', 'loss_of_appetite', 'abdominal_pain', 'passage_of_gases', 'internal_itching'],
        'AIDS': ['muscle_wasting', 'patches_in_throat', 'high_fever', 'extra_marital_contacts'],
        'Diabetes': ['fatigue', 'weight_loss', 'restlessness', 'lethargy', 'irregular_sugar_level', 'blurred_and_distorted_vision', 'excessive_hunger', 'increased_appetite', 'polyuria'],
        'Gastroenteritis': ['vomiting', 'sunken_eyes', 'dehydration', 'diarrhoea'],
        'Bronchial Asthma': ['fatigue', 'cough', 'high_fever', 'breathlessness', 'family_history', 'mucoid_sputum'],
        'Hypertension': ['headache', 'chest_pain', 'dizziness', 'loss_of_balance', 'lack_of_concentration'],
        'Migraine': ['acidity', 'indigestion', 'headache', 'blurred_and_distorted_vision', 'excessive_hunger', 'stiff_neck', 'depression', 'irritability', 'visual_disturbances'],
        'Cervical spondylosis': ['back_pain', 'weakness_in_limbs', 'neck_pain', 'dizziness', 'loss_of_balance'],
        'Paralysis (brain hemorrhage)': ['vomiting', 'headache', 'weakness_in_one_body_side', 'altered_sensorium'],
        'Jaundice': ['itching', 'vomiting', 'fatigue', 'weight_loss', 'high_fever', 'yellowish_skin', 'dark_urine', 'abdominal_pain'],
        'Malaria': ['chills', 'vomiting', 'high_fever', 'sweating', 'headache', 'nausea', 'muscle_pain'],
        'Chicken pox': ['itching', 'skin_rash', 'fatigue', 'high_fever', 'headache', 'loss_of_appetite', 'mild_fever', 'swelled_lymph_nodes', 'malaise', 'red_spots_over_body'],
        'Dengue': ['skin_rash', 'chills', 'joint_pain', 'vomiting', 'fatigue', 'high_fever', 'headache', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'muscle_pain', 'red_spots_over_body'],
        'Typhoid': ['chills', 'vomiting', 'fatigue', 'high_fever', 'headache', 'nausea', 'constipation', 'abdominal_pain', 'diarrhoea', 'toxic_look_(typhos)', 'belly_pain'],
        'hepatitis A': ['joint_pain', 'vomiting', 'fatigue', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellowing_of_eyes', 'muscle_pain']
    }

    # Add missing primary symptoms to the main symptoms list if any
    all_symptoms = set(symptoms)
    for disease_symptoms in diseases.values():
        all_symptoms.update(disease_symptoms)
    
    symptoms = sorted(list(all_symptoms))
    print(f"Total symptoms: {len(symptoms)}")

    data = []
    disease_list = list(diseases.keys())

    for _ in range(n_samples):
        disease = random.choice(disease_list)
        row = {s: 0 for s in symptoms}
        row['prognosis'] = disease
        
        # Add primary symptoms (mostly)
        primary_symptoms = diseases[disease]
        for s in primary_symptoms:
            if s in row and random.random() > 0.1: # 90% chance for primary symptoms
                row[s] = 1
        
        # Add some random noise symptoms
        noise_symptoms = random.sample(symptoms, random.randint(0, 3))
        for s in noise_symptoms:
            row[s] = 1
            
        data.append(row)

    df = pd.DataFrame(data)
    df.to_csv('dataset.csv', index=False)
    print(f"Dataset generated with {n_samples} records and saved to dataset.csv")

if __name__ == '__main__':
    generate_dataset()
