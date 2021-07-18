from django.contrib import admin

from .models import AnalysisLog


@admin.register(AnalysisLog)
class UserAdmin(admin.ModelAdmin):
    pass
