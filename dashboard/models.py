from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY = (
    ('Stationary','Stationary'),
    ('Electronic','Electronic'),
    ('Food','Food')
)

class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=20,choices=CATEGORY,null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name} - {self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} Order by {self.staff.username}'