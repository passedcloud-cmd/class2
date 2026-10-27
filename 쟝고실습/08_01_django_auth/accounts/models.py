from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # 빌트인 유저 모델 대신 이 모델 유저를 쓰겠다
    pass
