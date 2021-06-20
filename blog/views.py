from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
class IndexView(ListView):
    template_name ='index.html'
    context_object_name = 'orderby_records'
    queryset = BlogPost.objects.order_by('-posted_at')
    paginate_by = 3

class BlogDetail(DetailView):
    template_name = 'post.html'
    model = BlogPost

class ScienceView(ListView):
    template_name = 'science_list.html'
    model = BlogPost
    context_object_name = 'science_records'
    queryset = BlogPost.objects.filter(category='science').order_by('-posted_at')
    paginate_by =2

class DailyLifeView(ListView):
    template_name = 'daylylife_list.html'
    model = BlogPost
    context_object_name = 'dailylife_records'
    queryset = BlogPost.objects.filter(category='dailylife').order_by('-posted_at')
    paginate_by =2

class MusicView(ListView):
    template_name = 'music_list.html'
    model = BlogPost
    context_object_name = 'music_records'
    queryset = BlogPost.objects.filter(category='music').order_by('-posted_at')
    paginate_by =2

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blog:contact')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request,'メールは正常に送信されました')
        return super().form_valid(form)
