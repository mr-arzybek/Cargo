from django.contrib import admin
from .models import GroupTrackCodes, Status, TrackCode


class GroupTrackCodeAdmin(admin.ModelAdmin): # Add other fields you want to display in the admin list view
    search_fields = ('statuses__name_status',)  # Add fields you want to be searchable
    def get_statuses(self, obj):
        return ", ".join([status.name_status for status in obj.statuses.all()])
    get_statuses.short_description = 'Statuses'

    list_display = ('get_statuses',)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('name_status', 'pk')  # Display the status name and primary key
    search_fields = ('name_status',)  # Make the status name searchable


class TrackCodeAdmin(admin.ModelAdmin):
    list_display = ('track_code_name', 'pk', 'created_at', 'updated_at')
    search_fields = ('track_code', )

# Register your models here.
admin.site.register(GroupTrackCodes, GroupTrackCodeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(TrackCode, TrackCodeAdmin)
