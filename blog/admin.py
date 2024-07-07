from django.contrib import admin
from .models import blog,category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug",)
    list_editable = ("is_active","is_home",)
    search_fields = ("title", "description","slug")
    readonly_fields = ("description",)
    


admin.site.register(blog, BlogAdmin)
admin.site.register(category)
