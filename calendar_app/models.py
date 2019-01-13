from django.db import models
from django.urls import reverse


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def get_start_time(self):
        return self.start_time.strftime('%H:%M')

    @property
    def get_html_url(self):
        url = reverse('calendar_app:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
