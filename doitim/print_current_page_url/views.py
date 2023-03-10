from django.shortcuts import render

# Create your views here.
def index(request):
    print('hello')
    return render(request, 'print_current_page_url/index.html')