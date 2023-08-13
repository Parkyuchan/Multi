from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category

# Create your views here.

def center(request) :
    return render(request, 'product/center_info.html')

class ProductList(ListView):
    model = Product
    ordering = '-pk'
    #paginate_by = 5

    # 카테고리 뷰 함수 생성(딕셔너리로 처리한다 - 첫번째 게시물의 카테고리는 ??이다 관계 형성)
    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data()
        context['category_name'] = Category.objects.all()  # 카테고리가 있는 게시물 개수
        return context  # 카테고리 저장된 변수 리턴


def category_page(request, slug):  # 카테고리 별로 정렬된 페이지
    # 카테고리가 없으면(category_page함수의 slug인자로 'no_category'가 넘어오는 경우)
        # category_page함수의 인자로 받은 slug와 동일한 slug를 갖는 카테고리를 불러온다.
    category = Category.objects.get(slug=slug)
        # 동일한 카테고리인 게시물을 보여준다.

    product_list = Product.objects.filter(category=category).order_by('-pk')

    return render(  # render함수는 방문자에게 blog/post_list.html을 보내준다.(장고가 기본적으로 제공하는 함수)
        request,
        'product/product_list.html',  # 템플릿은 post_list.html 사용
        {
            'product_list': product_list,
            'category': Category.objects.all()  # 모든 카테고리 레코드를 categories 저장
        }
    )