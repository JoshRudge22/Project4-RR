from django.contrib import admin
from .models import Job, AvailableTime, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'address', 'hired')
    list_filter = ('hired',)
    def hired(self, obj):
        return obj.hired
        hired.short_description = 'Filled'
        hired.boolean = True

admin.register(AvailableTime)


admin.site.register(JobApplication)

