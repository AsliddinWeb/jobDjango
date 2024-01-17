from django.contrib.auth.models import User
from django.db import models

class JobCategory(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='job-category')

    def __str__(self):
        return self.title

class JobRegion(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='job-region')

    def __str__(self):
        return self.name

# class JobFile(models.Model):
#     title = models.CharField(max_length=255)
#     file = models.FileField(upload_to='job-file')
#
#     def __str__(self):
#         return self.title

STATUS_CHOICES = (
    ('Kutishda', 'Kutishda'),
    ('Aktiv', 'Aktiv'),
    ('Yakunlandi', 'Yakunlandi'),
)
class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons', null=True, blank=True)
    description = models.TextField()
    file = models.FileField(upload_to='files', null=True, blank=True)

    region = models.ForeignKey(JobRegion, on_delete=models.CASCADE)
    district = models.CharField(max_length=255, blank=True, null=True)

    price = models.BigIntegerField(blank=True, null=True)
    is_none_price = models.BooleanField(default=False)

    deadline = models.DateField(blank=True, null=True)
    is_none_deadline = models.BooleanField(default=False)

    status = models.CharField(max_length=255, default='Kutishda', choices=STATUS_CHOICES, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
