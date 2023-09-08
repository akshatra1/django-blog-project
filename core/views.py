from django.shortcuts import render
# blog/views.py
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.db.models import Q

from .forms import BlogSearchForm

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'posts'
    ordering = ['-timestamp']

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
    context_object_name = 'post'

def blog_search(request):
    if request.method == "GET":
        form = BlogSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('search_query')
            if query:
                results = BlogPost.objects.filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                )
            else:
                results = []
        else:
            # Handle form errors here if needed
            results = []
        context = {
            'form': form,
            'results': results,
        }
    
        return render(request, 'search_results.html', context)
    else:
        return render(request, 'search_results.html', {'form': BlogSearchForm()})