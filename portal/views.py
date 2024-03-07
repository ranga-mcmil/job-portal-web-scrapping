from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobPost, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchForm
from django.urls import reverse
from django.db.models import Q
from . import utils
import json

# Create your views here.
def home(request, category_slug=None):
    posts_list = JobPost.objects.all().order_by('?')
    category = None
    try:
        if request.user.is_authenticated:
            category = Category.objects.get(slug=request.user.category.slug)
            posts_list = category.posts.all().order_by('?')
    except:
        posts_list = JobPost.objects.all().order_by('?')

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        posts_list = category.posts.all().order_by('?')
    


    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 20)
    categories = Category.objects.all()
    

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'categories': categories[:8],
        'category': category
    }

    return render(request, 'portal/home.html', context)


def category_list(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'portal/category_list.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_val = form.get_info()
            return redirect(reverse('portal:search') + f'?search={search_val}')

    else:
        try:
            search_val = request.GET['search']
        except:
            return redirect(reverse('portal:home'))

        categories = Category.objects.filter(Q(name__icontains=search_val))
        posts_list = JobPost.objects.filter(Q(title__icontains=search_val)).order_by('?')
        page = request.GET.get('page', 1)
        paginator = Paginator(posts_list, 20)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)


        obj = {
            'categories': categories,
            'posts': posts
        }

        context = {
            'posts': posts,
            'categories': categories,
            'search_val': search_val
        }

        return render(request, 'portal/search.html', context)

def about(request):
    return render(request, 'portal/about.html')

def scrap(request):
    utils.scrap()
    return redirect(reverse('portal:home'))
