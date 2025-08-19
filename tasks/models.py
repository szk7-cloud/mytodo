
from django.db import models

class Task(models.Model):

    #ステータス（状態）の選択肢を定義
    STATUS_CHOICES = [
        ('pending', '未完了'),
        ('done', '完了'),
    ]

    #優先度の選択肢を定義
    PRIORITY_CHOICES = [
        ('low', '低'),
        ('medium', '中'),
        ('high', '高'),
    ]

    title = models.CharField(max_length=200)#タスクのタイトル
    completed = models.BooleanField(default=False)#完了チェック
    due_date = models.DateField(null=True, blank=True)#締切日
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    memo = models.TextField(blank=True)

    def __str__(self):
        return self.title
