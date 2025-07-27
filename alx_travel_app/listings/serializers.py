from rest_framework import serializers
from .models import Listing, Booking, Review


class BookingSerializer(serializers.ModelSerializer):
    guest_name = serializers.CharField(max_length=100)

    class Meta:
        model = Booking
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.CharField(max_length=100)

    class Meta:
        model = Review
        fields = '__all__'


class ListingSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    price_per_night = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'location',
            'price_per_night',
            'created_at',
            'bookings',
            'reviews',
        ]
