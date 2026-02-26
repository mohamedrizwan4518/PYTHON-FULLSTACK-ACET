from app import create_app, db
from app.models import User, Diagnosis, Doctor, Appointment

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Diagnosis': Diagnosis, 'Doctor': Doctor, 'Appointment': Appointment}

if __name__ == '__main__':
    app.run(debug=True)
