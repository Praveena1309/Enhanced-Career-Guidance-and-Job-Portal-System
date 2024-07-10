from django.contrib import admin
from .models import *



class BranchAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "qualification":
            kwargs["queryset"] = qulificationRfeild.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CourseDetailsAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "branch":
            kwargs["queryset"] = Branch.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(qulificationRfeild)
admin.site.register(Branch, BranchAdmin)
admin.site.register(CourseDetails, CourseDetailsAdmin)