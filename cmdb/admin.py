from django.contrib import admin
from .models import Host

# Register your models here.
class HostAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip', 'os', 'cpu', 'memory', 'disk', 'description')

admin.site.register(Host, HostAdmin)