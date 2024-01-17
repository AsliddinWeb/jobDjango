from django.contrib import admin

from .models import *

class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
admin.site.register(JobCategory, JobCategoryAdmin)

class JobRegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
admin.site.register(JobRegion, JobRegionAdmin)

# class JobFileAdmin(admin.ModelAdmin):
#     list_display = ('title', 'file')
# admin.site.register(JobFile, JobFileAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'category', 'region', 'price', 'created_at', 'status')
    list_filter = ['category', 'region', 'status']
    # filter_horizontal = ('files', )
admin.site.register(Job, JobAdmin)