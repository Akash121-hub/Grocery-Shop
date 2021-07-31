from django.contrib.auth import login, authenticate
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from . forms import RegisterForm
from django.contrib.auth.decorators import login_required
from . models import Items
# from .filters import DateFilter
def registerPage(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			obj = User.objects.create_user(username=username,email=email,password=password)
			obj.save()
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request,'grocery/register.html',{'form':form})






def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login (request, user)
			return redirect('index')
		else:
			messages.info(request, 'username or password is incorrect')
			return render(request, 'grocery/Login.html')
	context = {}
	return render(request, 'grocery/Login.html', context)



@login_required(login_url='login')
def logoutPage(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def index(request):

	item_objs = Items.objects.all().order_by('-ordered_date')
	
	return render(request, 'grocery/index.html', {'item_objs':item_objs})

@login_required(login_url='login')
def add_products(request):
	if request.method == "POST":
		item_name = request.POST.get('item name')
		item_quantity = request.POST.get('item quantity')
		item_status = request.POST.get('item status')
		date = request.POST.get('date')
		item_obj = Items(name=item_name,quantity=item_quantity,status=item_status,ordered_date=date)
		user = request.user
		item_obj.user = user
		item_obj.save()
		return redirect('index')
	context = {}
	return render(request,'grocery/add.html', context)

@login_required(login_url='login')
def upadte_item(request,order_id):
	order_objs = Items.objects.get(pk=order_id)
	context = {'order_objs':order_objs}
	return render(request,'grocery/update.html', context)



@login_required(login_url='login')
def upadte_item_and_save(request,pk):
	order_obj = Items.objects.get(pk=pk)

	order_obj.name = request.POST.get('Item name')
	order_obj.quantity = request.POST.get('Item quantity')
	order_obj.status = request.POST.get('status')
	order_obj.ordered_date = request.POST.get('date')
	order_obj.save()
	context = {'order_obj':order_obj}
	return redirect('/update/{}/'.format(order_obj.pk),context)



@login_required(login_url='login')
def delete_item(request,pk):
	Items.objects.filter(pk=pk).delete()
	return redirect('index')



    
@login_required(login_url='login')
def search(request):
	if request.method == "POST":
		user_input_date = request.POST.get('date_search')
		search_result = Items.objects.filter(ordered_date=user_input_date)
		return render(request,"grocery/search.html",{'date':search_result})
	else:
		return HttpResponse("No values for the Given Input")
