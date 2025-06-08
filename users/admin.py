from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)
admin.site.site_header = "SyncRao Admin Dashboard"
admin.site.site_title = "SyncRao"
admin.site.index_title = " "

