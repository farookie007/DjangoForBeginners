import imp
from django.views.generic import ListView, TemplateView

from .models import Post

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts_list'


class AboutView(TemplateView):
    template_name = 'posts/about.html'
