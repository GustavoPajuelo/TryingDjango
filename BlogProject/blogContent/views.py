from django.shortcuts import render

def blog_content(request):
    return render(request, 'blogs/content.html')
