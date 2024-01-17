from django.contrib import admin

from .models import *

class HomeSearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image')
admin.site.register(HomeSearch, HomeSearchAdmin)

class HomeSearchCounterAdmin(admin.ModelAdmin):
    list_display = ('title', 'count')
admin.site.register(HomeSearchCounter, HomeSearchCounterAdmin)

class HomeStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'icon')
admin.site.register(HomeStep, HomeStepAdmin)

class HomeReklamaAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image')
admin.site.register(HomeReklama, HomeReklamaAdmin)

class HomeResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image', 'button_title', 'button_link')
admin.site.register(HomeResume, HomeResumeAdmin)

class HomeAppAdmin(admin.ModelAdmin):
    list_display = ('title', 'cap_title', 'image', 'app_store_link', 'play_market_link')
admin.site.register(HomeApp, HomeAppAdmin)

class HomeAppDivsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'icon')
admin.site.register(HomeAppDivs, HomeAppDivsAdmin)