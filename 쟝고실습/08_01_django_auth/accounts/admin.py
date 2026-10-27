from django.contrib import admin
from  .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# 이제 우리는 기본 User 클래스가 아니라 커스텀 User class로 대체했기 때문에
#  amin에 새롭게 등록해줄 필요가 있음
admin.site.register(User, UserAdmin)