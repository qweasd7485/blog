from django.shortcuts import render, redirect, get_list_or_404,\
    get_object_or_404
from django.contrib import messages

from article.models import Article, Comment
from article.forms import ArticleForm
from django.db.models.query_utils import Q
# Create your views here.
def article(request):
    articles = Article.objects.all()
    itemsList = []
    for article in articles:
        items = [article]
        items.extend(list(Comment.objects.filter(article=article)))
        itemsList.append(items)
        context = {'itemsList':itemsList}
    return render(request, 'article/article.html', context)

def articleCreate(request):
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        return render(request, template, {'articleForm':ArticleForm()})
    #POST
    articleForm = ArticleForm(request.POST)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})
    articleForm.save()
    messages.success(request, '文章已新增')
    return redirect('article:article')

def articleRead(request, articleId):
    articleToRead = get_object_or_404(Article, id=articleId)
    context = {
        'article': articleToRead,
        'comments': Comment.objects.filter(article=articleToRead)
        }
    return render(request, 'article/articleRead.html', context)

def articleUpdate(request, articleId):
    articleToUpdate = get_object_or_404(Article, id=articleId)
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        articleForm = ArticleForm(instance=articleToUpdate)
        return render(request, template, {'articleForm':articleForm, 'article':articleToUpdate})
    # POST
    articleForm = ArticleForm(request.POST, instance=articleToUpdate)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm, 'article':articleToUpdate})
    articleForm.save()
    messages.success(request, '文章已修改')
    return redirect('article:articleRead', articleId=articleId)

def articleDelete(request, articleId):
    if request.method == 'GET':
        return article(request)
    # POST
    articleToDelete = get_object_or_404(Article, id=articleId)
    articleToDelete.delete()
    messages.success(request, '文章已刪除')
    return redirect('article:article')

def articleSearch(request):
    searchTerm = request.GET.get('searchTerm')
    articles = Article.objects.filter(Q(title__icontains=searchTerm) | Q(content__icontains=searchTerm))
    context = {'articles':articles, 'searchTerm0':searchTerm}
    return render(request, 'article/articleSearch.html', context)