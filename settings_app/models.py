from django.db import models
from django.db.models import TextField


class SeoSettings(models.Model):
    keywords = models.CharField(max_length=455)
    author = models.CharField(max_length=455)
    description = models.TextField()
    favicon = models.ImageField(upload_to='favicons')

    def __str__(self):
        return self.description

class SiteSettings(models.Model):
    title = models.CharField(max_length=455)
    header_logo = models.ImageField(upload_to='logos')
    footer_logo = models.ImageField(upload_to='logos')
    brand_name = models.CharField(max_length=455)

    def __str__(self):
        return self.title

class OneNavbar(models.Model):
    title = models.CharField(max_length=455)
    link = models.CharField(max_length=455)
    is_submenu = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class TwoNavbar(models.Model):
    one_navbar = models.ForeignKey(OneNavbar, on_delete=models.CASCADE)
    title = models.CharField(max_length=455)
    link = models.CharField(max_length=455)

    def __str__(self):
        return self.title

class FooterSettings(models.Model):
    note = models.TextField()
    copyright = TextField()
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.note

class FooterLinks(models.Model):
    title = models.CharField(max_length=455)
    link = models.CharField(max_length=455)
    is_useful = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class SocialSettings(models.Model):
    title = models.CharField(max_length=455)
    link = models.CharField(max_length=455)
    icon = models.CharField(max_length=455)

    def __str__(self):
        return self.title
