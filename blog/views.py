from django.shortcuts import render

# Create your views here. --- "logic" of the application

def post_list(request):
    return render(request, 'blog/post_list.html', {})