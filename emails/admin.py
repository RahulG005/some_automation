from django.contrib import admin
from .models import List, Subscriber, Email, EmailTracking, Sent
# Register your models here.

class EmailTrackingAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscriber', 'opened_at', 'clicked_at')

class subscriberadmin(admin.ModelAdmin):
    list_display = ('email_address', 'email_list')

class listadmin(admin.ModelAdmin):
    list_display = ('email_list', 'count_emails')

admin.site.register(List, listadmin)
admin.site.register(Subscriber, subscriberadmin)
admin.site.register(Email)
admin.site.register(EmailTracking, EmailTrackingAdmin)
admin.site.register(Sent)