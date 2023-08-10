from django.db import models
from accounts.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)  # title은 문자열로 최대 길이 30(게시물 제목)
    content = models.TextField()  # content는 텍스트형(게시물 내용)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    started_at = models.CharField(max_length=30)
    arrive_place = models.CharField(max_length=30)
    
    ending = models.BooleanField(default=False, blank = True)


    def __str__(self):  # [제목번호]제목 :: 작성자명 <-- 이와 같은 형식으로 나올 수 있도록 설정(관리자 페이지)
        return f'[{self.pk}]{self.title} :: {self.user}'
    # pk는 각 레코드의 고유값(1,2....)
    # self.title로 제목 나타내기

    def get_absolute_url(self):  # 게시물 관리 페이지에서 view on site 버튼 생성 후 버튼 누르면 해당 게시물 페이지로 이동
        return f'/post/{self.pk}/'

    class Meta:
        verbose_name_plural = '게시물'  # 관리자 페이지에서 카테고리 목록 이름을 categorys에서 categories로 변경