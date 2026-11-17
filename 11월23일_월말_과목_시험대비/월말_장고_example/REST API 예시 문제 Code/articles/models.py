from django.db import models

# 모델 정보는 수정하지 않습니다.
# 모델 정보 수정 시 주어진 db.sqlite3 와 맞지 않아 서버가 정상 동작하지 않을 수 있습니다.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번 : {self.title}'
