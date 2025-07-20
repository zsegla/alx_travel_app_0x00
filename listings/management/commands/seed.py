from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with sample listings data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        self.create_users()
        self.create_listings()
        self.stdout.write(self.style.SUCCESS('Successfully seeded data!'))

    def create_users(self):
        if not User.objects.filter(email='owner1@example.com').exists():
            User.objects.create_user(
                username='owner1',
                email='owner1@example.com',
                password='password123'
            )
        
        if not User.objects.filter(email='owner2@example.com').exists():
            User.objects.create_user(
                username='owner2',
                email='owner2@example.com',
                password='password123'
            )

    def create_listings(self):
        owners = User.objects.all()
        property_types = ['AP', 'HO', 'VI', 'CO', 'TH']
        amenities = [
            "WiFi,Kitchen,Washer,Air conditioning",
            "WiFi,Kitchen,Pool,Hot tub",
            "WiFi,Parking,Heating,TV",
            "WiFi,Kitchen,Washer,Dryer",
            "WiFi,Kitchen,Washer,Air conditioning,Pool"
        ]
        
        titles = [
            "Cozy apartment in city center",
            "Modern house with great view",
            "Luxury villa with private pool",
            "Comfortable condo near beach",
            "Spacious townhouse for families"
        ]
        
        descriptions = [
            "Beautiful place with all amenities you need for a comfortable stay.",
            "Perfect location with easy access to all major attractions.",
            "Relax and enjoy your vacation in this wonderful property.",
            "Great place for families or groups of friends.",
            "Recently renovated property with modern furniture and appliances."
        ]
        
        addresses = [
            "123 Main St, New York, NY",
            "456 Park Ave, Los Angeles, CA",
            "789 Ocean Dr, Miami, FL",
            "101 Mountain View, Denver, CO",
            "202 Lake Shore, Chicago, IL"
        ]
        
        if Listing.objects.count() == 0:
            for i in range(5):
                Listing.objects.create(
                    title=titles[i],
                    description=descriptions[i],
                    address=addresses[i],
                    property_type=property_types[i],
                    price_per_night=random.randint(50, 300),
                    bedrooms=random.randint(1, 5),
                    bathrooms=random.randint(1, 3),
                    max_guests=random.randint(2, 10),
                    amenities=amenities[i],
                    is_available=True,
                    owner=owners[i % len(owners)]
                )