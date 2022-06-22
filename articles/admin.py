from django.contrib import admin

# Register your models here.  This allows you to edit in the admin page
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_diplay= ['id', 'title']
    search_field= ['title','content']
    

admin.site.register(Article, ArticleAdmin)
