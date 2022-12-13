from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
#current user
from django_currentuser.db.models import CurrentUserField
# Create your models here.
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
class Posts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    #author = models.ForeignKey(User, on_delete= models.CASCADE)
    author = CurrentUserField(related_name="created")
    last_modified_by = CurrentUserField(on_update=True,related_name="updated")
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to = "media/blog/Image",default='NULL')
    content = HTMLField()
    categories = models.ManyToManyField(Category)
    publish = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default = 0)
    #models.ManyToManyField("app.Model", verbose_name=_(""))

    class Meta:
        ordering = ['-created_on']
        

    def __str__(self):
        return self.title
 



class PopolarPosts(models.Model):
    name = models.CharField(max_length=50)
