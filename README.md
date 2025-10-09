# Ashish Hospitals - Flask Web Application

A modern, responsive hospital management web application built with Flask, MongoDB, HTML, CSS, JavaScript, and Tailwind CSS.

## Quick Start

📋 **For detailed setup instructions including locally, Docker, AWS deployment with DocumentDB , see [setup.md](./setup.md)**

## Features

### Patient Features
- **Responsive Design**: Beautiful, mobile-friendly interface using Tailwind CSS
- **Online Appointment Booking**: Easy-to-use appointment scheduling system
- **Patient Information Management**: Secure storage of patient details
- **Service Information**: Comprehensive information about hospital services
- **Contact & Location**: Easy access to hospital contact information

### Admin Features
- **Appointment Management**: View, confirm, complete, or cancel appointments
- **Patient Database**: Access to patient information and appointment history
- **Export Functionality**: Export appointment data to CSV
- **Real-time Statistics**: Dashboard with appointment statistics
- **Status Management**: Update appointment statuses with ease

### Technical Features
- **Flask Backend**: Robust Python web framework
- **MongoDB Database**: NoSQL database for flexible data storage
- **Responsive UI**: Mobile-first design with Tailwind CSS
- **Form Validation**: Client-side and server-side validation
- **Flash Messages**: User feedback system
- **Modern JavaScript**: ES6+ features with proper error handling

## Tech Stack

- **Backend**: Python, Flask
- **Database**: MongoDB
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Tailwind CSS
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)

## Project Structure

```
ashish-heath-flask-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── static/               # Static files
│   ├── css/
│   │   └── style.css     # Custom CSS styles
│   ├── js/
│   │   └── main.js       # JavaScript functionality
│   └── images/           # Image assets
└── templates/            # HTML templates
    ├── base.html         # Base template
    ├── index.html        # Home page
    ├── about.html        # About page
    ├── services.html     # Services page
    ├── appointment.html  # Appointment booking
    ├── contact.html      # Contact page
    └── appointments.html # Admin appointments view
```
### For Patients

1. **Home Page**: Overview of hospital services and features
2. **About Page**: Information about the hospital, mission, and team
3. **Services Page**: Detailed information about medical services offered
4. **Book Appointment**: 
   - Fill out the patient information form
   - Select preferred date, time, and department
   - Receive confirmation
5. **Contact Page**: Hospital contact information and inquiry form


## API Endpoints

### Public Endpoints
- `GET /` - Home page
- `GET /about` - About page
- `GET /services` - Services page
- `GET /appointment` - Appointment booking form
- `GET /contact` - Contact page
- `POST /book_appointment` - Submit appointment booking

## Database Schema

### Appointments Collection
```javascript
{
  "_id": ObjectId,
  "patient_name": String,
  "phone_number": String,
  "email": String,
  "city": String,
  "appointment_date": String,
  "appointment_time": String,
  "department": String,
  "message": String,
  "created_at": DateTime,
  "updated_at": DateTime
}
```

## Customization

### Styling
- Modify `static/css/style.css` for custom styles
- Update Tailwind classes in HTML templates
- Change color scheme by updating CSS variables

### Functionality
- Add new routes in `app.py`
- Create new templates in `templates/` directory
- Extend JavaScript functionality in `static/js/main.js`

### Database
- Modify MongoDB connection string in `app.py`
- Add new collections or fields as needed
- Update validation rules in the Flask routes

## Troubleshooting

### Common Issues

1. **MongoDB Connection Error**:
   - Ensure MongoDB is running: `brew services list | grep mongodb` (macOS)
   - Check connection string in `app.py`
   - Verify MongoDB is accessible on port 27017

2. **Module Import Errors**:
   - Activate virtual environment
   - Install requirements: `pip install -r requirements.txt`
   - Check Python version compatibility

3. **Template Not Found**:
   - Verify template files are in `templates/` directory
   - Check template names in route functions
   - Ensure proper file extensions (.html)

4. **Static Files Not Loading**:
   - Check static files are in `static/` directory
   - Verify Flask static configuration
   - Clear browser cache

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support and questions:
- Email: javaforash@gmail.com
- Create an issue in the Repository.

**Ashish Hospitals** - Providing quality healthcare with modern technology.