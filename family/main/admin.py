from django.contrib import admin

# Register your models here.
from .models import Member, Family, Assessment, Wish

admin.site.register([
    Member, Family, Assessment, Wish
])
