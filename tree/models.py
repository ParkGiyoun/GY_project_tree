from django.db import models

class LinkInformation(models.Model):
    linkTitle = models.CharField(max_length=30)
    linkSubTitle = models.CharField(max_length=100)
    link = models.TextField()

    # 생성일자 필드
    created_at = models.DateTimeField(auto_now = True)

    # admin 페이지에서 보여줄 레코드 명 설정
    def __str__(self):
        return f'[{self.pk}] {self.linkTitle}'