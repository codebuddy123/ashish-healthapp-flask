from flask import Flask, render_template, request, redirect, url_for, flash

from pymongo import MongoClient
from datetime import datetime
import re
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# MongoDB Configuration
try:
    mongodb_uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
    database_name = os.environ.get('DATABASE_NAME', 'ashish_hospital')
    client = MongoClient(mongodb_uri)
    db = client[database_name]
    appointments_collection = db['appointments']
    print(f"Connected to MongoDB at {mongodb_uri}, database: {database_name}")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number format"""
    pattern = r'^[+]?[\d\s\-\(\)]{10,15}$'
    return re.match(pattern, phone) is not None

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/services')
def services():
    """Services page"""
    return render_template('services.html')

@app.route('/appointment')
def appointment():
    """Appointment booking page"""
    return render_template('appointment.html')

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    """Handle appointment booking"""
    try:
        # Get form data
        patient_name = request.form.get('patient_name', '').strip()
        phone_number = request.form.get('phone_number', '').strip()
        email = request.form.get('email', '').strip()
        city = request.form.get('city', '').strip()
        appointment_date = request.form.get('appointment_date', '')
        appointment_time = request.form.get('appointment_time', '')
        department = request.form.get('department', '')
        message = request.form.get('message', '').strip()

        # Validation
        errors = []
        
        if not patient_name:
            errors.append('Patient name is required')
        elif len(patient_name) < 2:
            errors.append('Patient name must be at least 2 characters long')
            
        if not phone_number:
            errors.append('Phone number is required')
        elif not validate_phone(phone_number):
            errors.append('Please enter a valid phone number')
            
        if not email:
            errors.append('Email is required')
        elif not validate_email(email):
            errors.append('Please enter a valid email address')
            
        if not city:
            errors.append('City is required')
            
        if not appointment_date:
            errors.append('Appointment date is required')
            
        if not appointment_time:
            errors.append('Appointment time is required')
            
        if not department:
            errors.append('Department is required')

        if errors:
            for error in errors:
                flash(error, 'error')
            return redirect(url_for('appointment'))

        # Create appointment document
        appointment_data = {
            'patient_name': patient_name,
            'phone_number': phone_number,
            'email': email,
            'city': city,
            'appointment_date': appointment_date,
            'appointment_time': appointment_time,
            'department': department,
            'message': message,
            'created_at': datetime.now()
        }

        # Insert into MongoDB
        result = appointments_collection.insert_one(appointment_data)
        
        if result.inserted_id:
            flash('Appointment booked successfully! We will contact you soon.', 'success')
            return redirect(url_for('appointment'))
        else:
            flash('Error booking appointment. Please try again.', 'error')
            return redirect(url_for('appointment'))

    except Exception as e:
        print(f"Error booking appointment: {e}")
        flash('An error occurred while booking your appointment. Please try again.', 'error')
        return redirect(url_for('appointment'))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)