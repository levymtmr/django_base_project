from django.contrib import admin

from accounts.models import UserAccount

from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.postgres.forms.ranges import DateRangeField, RangeWidget

class UserAccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserAccount, UserAccountAdmin)
