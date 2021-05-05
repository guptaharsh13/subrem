from django.contrib import admin
from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company_name', 'expire_date')
    search_fields = ('user__username', 'company_name',)
    ordering = ('expire_date', )

# Register your models here.
admin.site.register(Reminder, ReminderAdmin)