from django.contrib import admin
from .models import Article

# Register your models here.
# admin site에 등록한다. Aritle 클래스를
admin.site.register(Article)
