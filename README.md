# ALX Travel App

A property listing and booking application.

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install requirements: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Seed the database: `python manage.py seed`
6. Run the development server: `python manage.py runserver`

## Models

- **Listing**: Represents properties available for booking
- **Booking**: Represents user bookings for listings
- **Review**: Represents user reviews for listings

## API Endpoints

- `/api/listings/`: GET, POST listings
- `/api/listings/<id>/`: GET, PUT, PATCH, DELETE specific listing
- `/api/bookings/`: GET, POST bookings
- `/api/bookings/<id>/`: GET, PUT, PATCH, DELETE specific booking