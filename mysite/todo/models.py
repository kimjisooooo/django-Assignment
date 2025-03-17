from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)  # 제목
    description = models.TextField()  # 설명
    start_date = models.DateField()  # 시작일
    end_date = models.DateField()  # 마감일
    is_completed = models.BooleanField(default=False)  # 완료 여부
    created_at = models.DateTimeField(auto_now_add=True)  # 생성된 시간
    modified_at = models.DateTimeField(auto_now=True)  # 수정된 시간

    def __str__(self):
        return self.title