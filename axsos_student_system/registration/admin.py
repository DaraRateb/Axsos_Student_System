from django.contrib import admin
from django.contrib.auth.models import Group
from registration.models import Role
from registration.models import User



admin.site.site_header="Axsos Academy Admin Site"
admin.site.register(User)



