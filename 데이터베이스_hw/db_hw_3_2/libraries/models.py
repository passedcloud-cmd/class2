from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    birth = models.DateField()
    nationality = models.CharField(max_length=100)

    def __str__(self): # 관리자 페이지에서 저자 이름이 보이게 하는 매직 메서드
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #1:N 관계
    title = models.CharField(max_length=100)
    description = models.TextField()
    adult = models.BooleanField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
    