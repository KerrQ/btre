from django.db import models

# Create your models here.


class Inquiry(models.Model):
    listing = models.CharField(max_length=120)
    listing_id = models.IntegerField()
    user_id = models.IntegerField()
    name = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'inquiries'
