from django.contrib import admin
from .models import News,Category,Contact,Email
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title',"slug"]
    list_filter = ['status','created_time']
    prepopulated_fields = {"slug": ("title", )}

admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Email)