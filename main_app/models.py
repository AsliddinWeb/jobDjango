from django.db import models

class HomeSearch(models.Model):
    title = models.CharField(max_length=455)
    body = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "1. Qidiruv"

class HomeSearchCounter(models.Model):
    title = models.CharField(max_length=455)
    count = models.BigIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "2. Qidiruv kounteri"

class HomeStep(models.Model):
    title = models.CharField(max_length=455)
    icon = models.CharField(max_length=455)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "3. Qadamlar"

class HomeReklama(models.Model):
    title = models.CharField(max_length=455)
    body = models.TextField()
    image = models.ImageField(upload_to='images')

    button_title = models.CharField(max_length=455)
    button_link = models.CharField(max_length=455)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "4. Reklama"

class HomeResume(models.Model):
    title = models.CharField(max_length=455)
    body = models.TextField()
    image = models.ImageField(upload_to='images')
    button_title = models.CharField(max_length=455)
    button_link = models.CharField(max_length=455)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "5. Resume"

class HomeApp(models.Model):
    cap_title = models.CharField(max_length=455)
    title = models.CharField(max_length=455)
    image = models.ImageField(upload_to='images')

    app_store_link = models.CharField(max_length=455)
    play_market_link = models.CharField(max_length=455)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "6. Mobil ilova"

class HomeAppDivs(models.Model):
    title = models.CharField(max_length=455)
    body = models.TextField()
    icon = models.CharField(max_length=455)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "7. Mobil ilova qulayliklari"
