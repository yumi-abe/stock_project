from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100) #銘柄名
    acquisition_date = models.DateField() #取得日
    quantity = models.IntegerField() #株数
    fee = models.DecimalField(max_digits=10, decimal_places=2) #手数料
    
    def __str__(self):
        return f"{self.name} ({self.quantity}株)"
