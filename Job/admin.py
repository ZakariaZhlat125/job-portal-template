from django.contrib import admin
from .models import *


class ApplicantAdmin(admin.ModelAdmin):
    list_dispaly = ('job', 'user', 'create_at')


admin.site.register(Applicant, ApplicantAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'is_closed', 'date')


admin.site.register(Job, JobAdmin)
