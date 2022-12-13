from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Posts , Category
from django.core.paginator import Paginator
# Create your views here.
def blog(request):
    return render(request,'blog/sw.js')

class HomePage(generic.ListView):
    paginate_by = 4
    model = Posts
    c = Category
    queryset = Posts.objects.filter(publish=True).order_by('-created_on')
    template_name = 'blog/multiplepost.html'
    context_object_name ="posts"
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['pop_post'] = self.model.objects.filter(publish = True).order_by('views')[:4]
        context['category'] = self.c.objects.all()
        print(context['category'])
        return context

    

class PostDetail(generic.DetailView):
    paginate_by = 1
    model = Posts
    c = Category

    template_name = 'blog/singlepost.html'
    context_object_name ="post"
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        c = context['post'].categories.all()
        context['post'].views += 1
        context['post'].save()
        context['all'] = self.model.objects.filter(publish = True,categories = c[0].id).order_by('views')[0:3]
        context['pop_post'] = self.model.objects.filter(publish = True).order_by('views')[0:4]
        context['category'] = self.c.objects.all()
        return context

class Category(generic.ListView):
    queryset = Posts.objects.filter(publish = True).order_by('-created_on')
    template_name = 'blog/multiplepost.html'
    context_object_name ="posts"

def category(request, pk):
    posts = Posts.objects.filter(publish = True,categories = pk).order_by('-created_on')
    p_post = Posts.objects.filter(publish = True).order_by('views')[0:4]
    contact_list = Posts.objects.all()
    paginator = Paginator(contact_list, 2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/multiplepost.html' , {'posts':page_obj,'pop_post':p_post})
