from django.shortcuts import render,redirect
from .models import Items
from .forms import ItemsForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.utils import timezone

def Ecomhome(request):
	print(request.session.get("first_name"))
	return render(request, "Ecomhome.html", {})

def contgect_page(request):
	return render(request, "contact_page.html", {})

def JohnOrder(request):
	 key = request.session.session_key
	 #print(key)
	 request.session['first_name']="Sumesh"
	 items_all = Items.objects.all()
	 page = request.GET.get('page', 2)
	 paginator = Paginator(items_all, 3)
	 now = timezone.now()
	 print(now)
	 try:
	 	items = paginator.page(page)
	 except PageNotAnInteger:
	 	items = paginator.page(1)
	 except EmptyPage:
	 	items = paginator.page(paginator.num_pages)
	 return render(request, "JohnOrder.html", { 'items': items })
