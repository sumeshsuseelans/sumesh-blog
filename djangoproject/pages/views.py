from django.shortcuts import render,redirect
from .models import List
from .models import Books
from .models import MoviesList
from .forms import ListForm
from .forms import BookForm
from .forms import MoviesListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.utils import timezone



def home(request):
	return render(request, "home.html", {})

def about(request):
	return render(request, "about.html", {})

def contact(request):
	return render(request, "contact.html", {})

def movies(request):
    movie_all = MoviesList.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(movie_all, 3)
    now = timezone.now()
    print(now)
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render(request, "movies.html", { 'movies': movies },{ 'date':now })

def books(request):
    
    if request.method =='POST':
    	form = BookForm(request.POST or None)
    	
    	if form.is_valid():
    	    form.save()
    	    comments = Books.objects.all
    	    return render(request, 'books.html', {'all_comments': comments})
    
    else:
        comments = Books.objects.all
        return render(request, "books.html", {'all_comments': comments})

def order(request):
    
    if request.method =='POST':
    	form = ListForm(request.POST or None)
    	
    	if form.is_valid():
    	    form.save()
    	    all_items = List.objects.all
    	    messages.success(request, ('Item has been added to the list!'))
    	    return render(request, 'order.html', {'all_items': all_items})
    
    else:
        all_items = List.objects.all
        return render(request, "order.html", {'all_items': all_items})

def edit(request, list_id):
    
    if request.method =='POST':
    	item= List.objects.get(pk=list_id)

    	form = ListForm(request.POST or None, instance=item)
    	
    	if form.is_valid():
    	    form.save()
    	    all_items = List.objects.all
    	    messages.success(request, ('Item has been added edited'))
    	    return redirect('order')
    
    else:
        item = List.objects.get(pk=list_id)
        return render(request, "edit.html", {'item': item})

def items(request):
	return render(request, "items.html", {})

def delete(request, list_id):
	item=List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item has been deleted from the list'))
	return redirect('order')

def cross_off(request, list_id):
        item=List.objects.get(pk=list_id)
        item.completed = True
        item.save()
        return redirect('order')

def uncross(request, list_id):
        item=List.objects.get(pk=list_id)
        item.completed = False
        item.save()
        return redirect('order')
