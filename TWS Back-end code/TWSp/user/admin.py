from django.contrib import admin
from .models import User   #같은 경로의 models.py에서 User라는 클래스를 임포트한다.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'pw', 'pwc', 'company', 'address', 'call', 'email')

admin.site.register(User, UserAdmin) #site에 등록