from django.contrib import admin
from .models import Compliance, Finance, Legal, Competition

admin.site.register(Compliance)
admin.site.register(Finance)
admin.site.register(Legal)
admin.site.register(Competition)