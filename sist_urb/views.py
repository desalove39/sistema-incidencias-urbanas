from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'sist_urb/index.html')

def error_404_view(request, exception):
    return render(request, 'sist_urb/404.html', status=404)