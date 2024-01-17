from django.contrib import admin

from .models import *

class SeoSettingsAdmin(admin.ModelAdmin):
    list_display = ('keywords', 'author', 'description', 'favicon')
admin.site.register(SeoSettings, SeoSettingsAdmin)

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'header_logo', 'footer_logo', 'brand_name')
admin.site.register(SiteSettings, SiteSettingsAdmin)

class OneNavbarAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'is_submenu')
admin.site.register(OneNavbar, OneNavbarAdmin)

class TwoNavbarAdmin(admin.ModelAdmin):
    list_display = ('one_navbar', 'title', 'link')
admin.site.register(TwoNavbar, TwoNavbarAdmin)

class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ('note', 'copyright')
admin.site.register(FooterSettings, FooterSettingsAdmin)

class FooterLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'is_useful')
admin.site.register(FooterLinks, FooterLinksAdmin)

class SocialSettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'icon')
admin.site.register(SocialSettings, SocialSettingsAdmin)