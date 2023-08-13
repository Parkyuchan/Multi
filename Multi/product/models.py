from django.db import models

# Create your models here.
class Category(models.Model):  # 카테고리 모델 생성
    # unique=True 코드를 넣으면 동일한 name을 갖는 카테고리를 만들 수 없다(길이 제한이 있는 문자열)
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, allow_unicode=True)

    def __str__(self):
        return self.category_name  # 카테고리 이름 리턴

    def get_absolute_url(self):
        # 카테코리 관리 페이지에서 view on site 버튼 생성 후 버튼 누르면 해당 카테고리 페이지로 이동
        return f'/product/category/{self.slug}/'

    class Meta:
        verbose_name_plural = '카테고리'  # 관리자 페이지에서 카테고리 목록 이름을 categorys에서 categories로 변경
        
class Product(models.Model) :
    name = models.CharField(max_length=50, blank=True) # 이건 뭐여 있던디
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    manu_f =  models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    price_buy = models.CharField(max_length=50, blank=True)
    price_borrow = models.CharField(max_length=50, blank=True)
    url_go = models.URLField()

    def __str__(self) :
        return f'[{self.pk}]{self.name}'