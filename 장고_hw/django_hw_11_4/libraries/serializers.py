from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class ReviewInBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content', 'score')

class BookSerializer(serializers.ModelSerializer):
    review_set = ReviewInBookSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class BookIsbnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('isbn',)

class ReviewListSerializer(serializers.ModelSerializer):
    book = BookIsbnSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('content', 'score', 'book')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)