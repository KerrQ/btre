from django.contrib import admin
from .models import Inquiry

# Register your models here.


class Inquiries(admin.ModelAdmin):
    readonly_fields = ['timestamp']
    list_filter = ['timestamp']
    list_display = ['__str__', 'email', 'listing']

    class Meta:
        model = Inquiry


admin.site.register(Inquiry, Inquiries)
