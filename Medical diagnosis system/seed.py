from app import create_app, db
from app.models import User, Doctor, Diagnosis, Appointment
from datetime import datetime, date
import json

def seed_db():
    app = create_app()
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # 1. Create Admin
        admin = User(username='admin', email='admin@hospital.com', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)

        # 2. Create Doctors
        doctors = [
            Doctor(name='Sarah Johnson', specialization='General Medicine', available_days='Mon,Wed,Fri', bio='Board-certified internist with 10 years experience.'),
            Doctor(name='Michael Chen', specialization='Infectious Diseases', available_days='Tue,Thu', bio='Specialist in viral and fungal infections.'),
            Doctor(name='Elena Rodriguez', specialization='Dermatology', available_days='Mon,Tue,Wed,Thu,Fri', bio='Expert in skin conditions and allergies.')
        ]
        for d in doctors:
            db.session.add(d)

        # 3. Create Patient
        patient = User(username='patient1', email='patient@example.com', role='patient')
        patient.set_password('patient123')
        db.session.add(patient)
        db.session.commit()

        # 4. Create sample diagnoses for Analytics
        d1 = Diagnosis(user_id=patient.id, risk_score=15, timestamp=datetime.utcnow())
        d1.set_symptoms({'headache': 2, 'fatigue': 1})
        d1.set_predictions([{'disease': 'Migraine', 'probability': 85.5}])
        
        d2 = Diagnosis(user_id=patient.id, risk_score=85, timestamp=datetime.utcnow())
        d2.set_symptoms({'chest_pain': 5, 'breathlessness': 5})
        d2.set_predictions([{'disease': 'Hypertension', 'probability': 92.0}])

        db.session.add_all([d1, d2])
        
        # 5. Create sample appointment
        appt = Appointment(
            patient_id=patient.id,
            doctor_id=1,
            date=date.today(),
            time_slot='10:00 AM',
            status='Pending'
        )
        db.session.add(appt)

        db.session.commit()
        print("Database seeded successfully with sample accounts:")
        print("Admin: admin / admin123")
        print("Patient: patient1 / patient123")

if __name__ == '__main__':
    seed_db()
