from django.contrib import admin
from .models import Email

# Register your models here.


class EmailAdmin(admin.ModelAdmin):
    list_display = ('email','subject', 'sendtime')
admin.site.register(Email, EmailAdmin)
