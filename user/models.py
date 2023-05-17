from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    user_type = models.IntegerField()   # 사장님: 0, 사용자: 1, 배달기사: 2