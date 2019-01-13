from django.contrib import admin
from .models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time')
    list_filter = ('title', 'start_time', 'end_time')
    search_fields = ('title', 'start_time', 'end_time')


admin.site.register(Event, EventAdmin)
