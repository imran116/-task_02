from django.contrib import admin

from website.models import Management, ManagementFeature

# Register your models here.
admin.site.register(Management)
admin.site.register(ManagementFeature)
