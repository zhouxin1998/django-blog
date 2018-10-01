# coding:utf-8
from django.shortcuts import render
from .models import TypeInfo,BowenInfo
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    # print('test2')
    """首页"""
    typelist = TypeInfo.objects.all()
    boweninfo = BowenInfo.objects.all()

    boweninfo0 = boweninfo.order_by('-id')[0:10]#首页
    boweninfo1 = boweninfo.order_by('-id')[0:6]#最新
    boweninfo2 = boweninfo.order_by('-bClick')[0:6]#最多查看
    boweninfo3 = boweninfo.order_by('-bComment')[0:6]#最多评论
    bowen_top = boweninfo.filter(bIstop=True).order_by('id')[0:6]#置顶文章

    type_title = []
    for t in boweninfo0:
        type_title.append(t.bType.tTitle)

    context = {
        'title': "首页",
        'navs': typelist,
        'boweninfo':boweninfo0,
        'bowen_top': bowen_top,
        'boweninfo1': boweninfo1,
        'boweninfo2': boweninfo2,
        'boweninfo3': boweninfo3,
        'bowentype':type_title,
    }
    return render(request,'index/index.html',context=context)


def list(request,list_id,index_page):
    """列表页面"""

    boweninfo = BowenInfo.objects.all()
    boweninfo1 = boweninfo.order_by('-id')[0:6]  # 最新
    boweninfo2 = boweninfo.order_by('-bClick')[0:6]  # 最多查看
    boweninfo3 = boweninfo.order_by('-bComment')[0:6]  # 最多评论
    bowen_top = boweninfo.filter(bIstop=True).order_by('id')[0:6]#置顶文章

    try:
        typelist = TypeInfo.objects.all()
        typelist1 = typelist.get(pk=int(list_id))
        boweninfo_page = typelist1.boweninfo_set.all().order_by('-id')
        # boweninfo_page = BowenInfo.objects.filter(bType_id=list_id).order_by('-id')
    except Exception as e:
        print(e)
        typelist = None
        typelist1 = None
        boweninfo_page = None

    # 分页
    pageinator = Paginator(boweninfo_page, 12)
    page = pageinator.page(int(index_page))


    context = {
        'title':'列表',
        'navs': typelist,
        'bowen_top': bowen_top,
        'boweninfo1': boweninfo1,
        'boweninfo2': boweninfo2,
        'boweninfo3': boweninfo3,
        'current_title': typelist1.tTitle,
        'url_id': typelist1.id,
        'pageinator': pageinator,
        'page':page,
    }
    # print("*******************")
    # print(pageinator)
    # print(boweninfo_page)
    # print(page)
    return render(request, 'index/list.html', context=context)


def info(request, id):
    # 本条数据
    typelist = TypeInfo.objects.all()
    blog_info = BowenInfo.objects.all()
    bowen_top = blog_info.filter(bIstop=True).order_by('id')[0:6]#置顶文章
    try:
        current_blog_info = blog_info.get(pk=int(id))
    except Exception as e:
        print(e)
        current_blog_info = None
    try:
        typeinfo_id = current_blog_info.bType.id
    except Exception as e:
        print(e)
        typeinfo_id = None
    try:
        typeinfo_obj = TypeInfo.objects.get(pk=typeinfo_id)
    except Exception as e:
        print(e)
        typeinfo_obj = None
    # 上一条
    try:
        prev_blog_info = typeinfo_obj.boweninfo_set.get(pk=int(id)-1)
    except:
        prev_blog_info = None
    # 下一条
    try:
        next_blog_info = typeinfo_obj.boweninfo_set.get(pk=int(id)+1)
    except:
        next_blog_info = None

    # 最新文章
    boweninfo1 = blog_info.order_by('-id')[0:6]

    #点击率加１
    current_blog_info.bClick += 1
    current_blog_info.save()

    # 相关文章
    title = current_blog_info.bTitle
    type_title = current_blog_info.bType.tTitle

    correlation = BowenInfo.objects.filter(bContent__icontains=title).order_by('-id')[0:12]
    # print('************'*8)
    # print(title)
    # print(correlation)

    context = {
        'title': '详情',
        'navs': typelist,
        'bowen_top': bowen_top,
        'type_title': type_title,
        'blog_info': current_blog_info,
        'boweninfo1': boweninfo1,
        'prev_blog_info': prev_blog_info,
        'next_blog_info': next_blog_info,
        'correlation': correlation,
    }
    return render(request, 'index/info.html', context=context)



# 全文检索
from haystack.views import SearchView

class MySearchView(SearchView):
    """搜索"""
    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        # print('*****************************8888')
        if self.request.method == 'GET':
            get = self.request.GET
            search_txt = get.get('q')
        else:
            search_txt = None

        typelist = TypeInfo.objects.all()
        boweninfo = BowenInfo.objects.all()
        bowen_top = boweninfo.filter(bIstop=True).order_by('id')[0:6]#置顶文章

        context['title']= '搜索'
        boweninfo = BowenInfo.objects.all()
        boweninfo1 = boweninfo.order_by('-id')[0:6]  # 最新
        boweninfo2 = boweninfo.order_by('-bClick')[0:6]  # 最多查看
        boweninfo3 = boweninfo.order_by('-bComment')[0:6]  # 最多评论
        context['boweninfo1'] = boweninfo1
        context['boweninfo2'] = boweninfo2
        context['boweninfo3'] = boweninfo3
        context['bowen_top'] = bowen_top
        context['search_txt'] = search_txt
        context['navs'] = typelist
        # context['cart_count']=cart_count(self.request)
        return context