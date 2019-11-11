from django.shortcuts import render,HttpResponse

# Create your views here.

def Leon(request):
	print('Leon')
	return HttpResponse('Leon')