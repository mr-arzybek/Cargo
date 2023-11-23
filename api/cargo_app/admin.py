from django.contrib import admin
from .models import GroupTrackCodes, Status, TrackCode


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name_status', 'pk')  # Display the status name and primary key
    search_fields = ('name_status',)  # Make the status name searchable


class TrackCodeAdmin(admin.ModelAdmin):
    list_display = ('track_code_name', 'pk', 'created_at', 'updated_at')
    search_fields = ('track_code',)


# Register your models here.
admin.site.register(GroupTrackCodes)
admin.site.register(Status, StatusAdmin)
admin.site.register(TrackCode, TrackCodeAdmin)
