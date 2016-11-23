from django.shortcuts import render, redirect
from zhidaily.models import Article, Category, Best, Advert

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


def paging(request, **kwargs):
    tempdict = kwargs.keys()
    for temp in tempdict:
        page_robot = Paginator(kwargs[temp], 5)
        page_num = request.GET.get('page')
        try:
            article_list = page_robot.page(page_num)
        except EmptyPage:
            article_list = page_robot.page(page_robot.num_pages)
        except PageNotAnInteger:
            article_list = page_robot.page(1)
        return article_list


def advert():
    ad = Advert.objects.filter(display=True).all()
    return ad


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def category(request, cate_id):
    context = {}
    bestlist = Best.objects.filter(select_reason='编辑推荐').order_by('sort').all()
    catefory = Category.objects.all()
    if cate_id.isdigit():
        article = Article.objects.filter(category=cate_id).order_by('-publish_time').all()
        context['article'] = paging(request, article=article)
    else:
        return redirect('index')

    context['ad'] = advert()
    context['catefory'] = catefory
    context['bestlist'] = bestlist
    return render(request, 'categories.html', context=context)

def detail(request, article_id):
    context = {}

    if request.GET.get('abstract', 1) == 1:  # 默认显示摘要
        return render(request, 'detail-abstract.html', context=context)
    else:  # 不显示摘要
        return render(request, 'detail-noabstract.html', context=context)


def login(request):
    context = {}
    return render(request, 'login.html', context=context)


def regester(request):
    context = {}
    return render(request, 'regester.html', context=context)


def edit(request):
    context = ()
    return render(request, 'edit.html', context=context)
