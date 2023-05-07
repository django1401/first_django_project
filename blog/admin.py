from django.contrib import admin
from .models import Post,Category,Tags

# Register your models here.
admin.site.register(Category)
admin.site.register(Tags)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','status', 'created_date']
    list_filter = ['status']
    search_fields = ['title']
    empty_value_display = 'empty_value'