from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# 类之中的每一个变量都表示模型中一个数据库字段
# 每一个字段都是Field类的实例
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    #models.CASCADE-->级联查询，删除主表的时候从表也会一并删除对应的数据
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
