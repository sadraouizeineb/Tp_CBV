from django.contrib import admin
from .models import BlogPost, Author 

# admin.site.register(Author)
# admin.site.register(BlogPost) 
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass 





@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_on")  
    list_editable = ("title",)  
    list_display_links = ("author",)  
    search_fields = ("title", "content")  
    list_filter = ("created_on", "author")  
    list_per_page = 10  