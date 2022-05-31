from django.shortcuts import render, redirect
from .models import CategoryModel, ArticleModel

# Create your views here.
def new_article(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    elif request.method == 'POST':
        title = request.POST.get('my-article-title', '')
        category = request.POST.get('my-article-category', '')
        content = request.POST.get('my-article-content', '')

        new_article = ArticleModel.objects.create(title=title, category=category, content=content)
        new_article.save()
        
        return render(request, 'article.html')


def show_categories(request):
    all_categories = CategoryModel.objects.all()
    return render(request, 'category.html', {'categories': all_categories})
