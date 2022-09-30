from django.contrib import admin
from .models import exam,section


# Register your models here.
admin.site.register(exam)
# admin.site.register(section)

@admin.register(section)
class sectionAdmin(admin.ModelAdmin):

    #for list paage to display, show the following fields
    list_display=["section","test"]

    #to filter based on test
    list_filter=["test"]

    #to list field order of fields displayed on edit page
    fields= ["test","section","order","time","questions"]
