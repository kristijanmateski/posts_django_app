from django.contrib import admin
from app.models import Post, Category


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'dateTime')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(PostAdmin, self).save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
