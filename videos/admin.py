from django.contrib import admin

# Register your models here.
from . import models

class MovieAdmin(admin.ModelAdmin):
    # ordering of fields (detail view)
    fields = ['title','release_year','length']

    # fields to search
    search_fields = ['title','length']

    list_filter = ['release_year','length','title']

    list_display = ['title','release_year','length']

    list_editable = ['length']

admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)