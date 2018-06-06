from django.db import models

# Create your models here.
from django.utils import timezone


class Message(models.Model):
    title = models.CharField(u'留言人', max_length=32, null=True)
    phone = models.CharField(u'联系人',max_length=222)
    content = models.TextField(u'内容')
    create_date = models.DateTimeField(u'时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(default=timezone.now)
    is_delete = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'message'
        ordering = ['-update_time']
        verbose_name = '文章表'
        verbose_name_plural = verbose_name
