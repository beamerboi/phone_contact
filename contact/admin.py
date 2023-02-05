from django.contrib import admin

# Register your models here.
from contact.models import Numbers, Contact

admin.site.register(Contact)
admin.site.register(Numbers)

