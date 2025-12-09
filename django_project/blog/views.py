from django.shortcuts import render
from .models import Post
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin,
    )
# Create your views here.


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)

class PostListView(ListView):
    model = Post
    # Template name by default appname/modelname_viewtype.html => blog/post_list.html
    template_name = 'blog/home.html'

    # Contect_object_name by default post_list then we have to override it.
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    # for the template we wouldn't chang it as we are going to use the default name.
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # The default Template name is appname/modelname_form.html => blog/post_form.html
    # We could override template_name to make it anthing else, but we will keep it for now.
    
    # Here we need to over the form_valid to add the pk for the user who create the post to the post table
    # this will happen only if override the form_vaild function and add a new instance to this function
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # After creating a new post we have to tell the Django what is the next distnation so we have to override the success_url or implement get_absolute_url in the Post mode.
    


def about(request):
    return render(request, 'blog/about.html', {'title':'About'},)