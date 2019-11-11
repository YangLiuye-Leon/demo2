from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def view1(self, request):
    return HttpResponse('This is view1')

def view2(self, request):
    return render(request, 'app1/test.html')