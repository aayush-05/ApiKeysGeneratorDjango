from django.contrib import admin
from keys_api.models import RandomKey, AvailableKey
# Register your models here.
admin.site.register(RandomKey)
admin.site.register(AvailableKey)
