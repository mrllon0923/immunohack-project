from django.contrib import admin
from .models import Vaccine, AgeGroup, Disease


admin.site.register(Vaccine)
admin.site.register(AgeGroup)
admin.site.register(Disease)
