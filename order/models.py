from django.db import models

class Shop(models.Model):
    shop_name = models.CharField(max_length=20) # 가게 이름
    shop_address = models.CharField(max_length=40) # 가게 주소

class Menu(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)    # shop 테이블의 외래키를 받아옴
    food_name = models.CharField(max_length=20) # 실제로는 음식에 대한 것들도 따로 테이블을 만들어서 id값을 할당함.

class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)    # shop 테이블의 외래키를 받아옴
    order_date = models.DateTimeField('date ordered')   # 주문 날짜를 날짜형식으로 받음
    address = models.CharField(max_length=40)   # 배달지 주소
    estimated_time = models.IntegerField(default=-1)  # 배송되는데 걸리는 시간
    deliver_finish = models.BooleanField(default=0) # 배달 완료 상태
    
class Orderfood(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # 주문에 대한 외래키
    foods_name = models.CharField(max_length=20) # 주문된 음식 정보