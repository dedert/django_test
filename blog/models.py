from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    """
    models.Model 은  해당 클래스가 장고 모델임을 의미함. 따라서 Post가 데이터베이스에 저장되어야 된다고 알게 됨
    Post라는 객체에는 author, tilte, text, dreated_date, published_date 라는 attribute가 있고,
    CharField / DateTimeField 등 데이터 타입 지정.
    """
    author = models.ForeignKey('auth.User') #다른 모델에 대한 링크
    title = models.CharField(max_length=200) # 글자수 제한된 텍스트
    text = models.TextField() # 글자 수 제한 없는 긴 텍스트
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
