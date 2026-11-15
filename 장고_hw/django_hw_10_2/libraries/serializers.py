from rest_framework import serializers
from .models import Book

# 전체 목록용: 제목만
class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)

# 상세 정보용: 전부
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'