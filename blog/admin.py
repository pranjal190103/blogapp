from django.contrib import admin
from .models import Category,Post,Comment
# Register your models here.

#for configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','description','url','add_date')
    search_fields=('title',)

 #for configuration of Post admin   
class PostAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=10

    class Media:
        js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)


class CommentAdmin(admin.ModelAdmin) :
    list_display=('post','email','date_added','name','body') 
    search_fields=('date_added',) 
    list_filter=('post',) 
    list_per_page=10 


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
