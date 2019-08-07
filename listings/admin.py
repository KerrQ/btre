from django.contrib import admin
from .models import Listing
# Register your models here.


class ListingsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'realtor', 'is_published', 'state', 'city']
    list_filter = ['price', 'list_date']
    search_fields = ('title', 'state', 'city')
    list_per_page = 20

    class Meta:
        model = Listing


admin.site.register(Listing, ListingsAdmin)
