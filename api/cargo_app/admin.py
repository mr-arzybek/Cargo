from django.contrib import admin
from .models import TrackCode, Status


class TrackCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'status')
    list_filter = ('status',)
    search_fields = ('code',)
    list_per_page = 15


admin.site.register(TrackCode, TrackCodeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name_status',)
    search_fields = ('name_status',)
    list_per_page = 15


admin.site.register(Status, StatusAdmin)
