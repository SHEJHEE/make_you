from django.contrib import admin
from .models import contents
from .models import templates
# Register your models here.
#admin.site.register(make_U_models.Contents)

admin.site.register(contents)
admin.site.register(templates)
