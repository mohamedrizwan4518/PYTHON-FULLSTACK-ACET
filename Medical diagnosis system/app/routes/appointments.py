from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_required, current_user
from app import db
from app.models import Doctor, Appointment
from app.forms import AppointmentForm
from datetime import datetime

bp = Blueprint('appointments', __name__)

@bp.route('/appointments', methods=['GET', 'POST'])
@login_required
def book():
    form = AppointmentForm()
    doctors = Doctor.query.all()
    form.doctor.choices = [(d.id, f"Dr. {d.name} ({d.specialization})") for d in doctors]

    if form.validate_on_submit():
        appointment = Appointment(
            patient_id=current_user.id,
            doctor_id=form.doctor.data,
            date=form.date.data,
            time_slot=form.time_slot.data,
            status='Pending'
        )
        db.session.add(appointment)
        db.session.commit()
        flash('Appointment request submitted successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    appointments = Appointment.query.filter_by(patient_id=current_user.id).all()
    return render_template('appointments/book.html', form=form, appointments=appointments)

@bp.route('/appointments/doctor')
@login_required
def doctor_dashboard():
    if current_user.role != 'doctor':
        flash('Access denied.', 'danger')
        return redirect(url_for('main.dashboard'))
    
    # Simple logic: doctors see all appointments for now
    appointments = Appointment.query.all()
    return render_template('appointments/doctor_dashboard.html', appointments=appointments)

@bp.route('/appointments/update_status/<int:appointment_id>/<string:status>')
@login_required
def update_status(appointment_id, status):
    if current_user.role not in ['doctor', 'admin']:
        flash('Access denied.', 'danger')
        return redirect(url_for('main.dashboard'))
    
    appointment = Appointment.query.get_or_404(appointment_id)
    appointment.status = status
    db.session.commit()
    flash(f'Appointment #{appointment_id} updated to {status}.', 'success')
    
    if current_user.role == 'doctor':
        return redirect(url_for('appointments.doctor_dashboard'))
    return redirect(url_for('main.dashboard'))
