from django.contrib import admin
from .models import Posts , Category
# Register your models here.


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','views', 'publish','created_on')
    list_filter = ("publish","categories",'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    labels = {'title':'Post Title '}
    ## for autometically choose current user
    readonly_fields = ['author','last_modified_by']
    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        #Posts.author = request.user
        pass
        return super().get_form(request, obj, **kwargs)
    def save_model(self, request, obj, form, change):
        #obj.author = request.user
        obj.last_modified_by = request.user
        obj.save()
        
            


@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    pass
    

