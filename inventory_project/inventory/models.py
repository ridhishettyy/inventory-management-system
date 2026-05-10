from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    description=models.TextField(blank=True)
    reorder_level=models.IntegerField(default=5)

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()

    status=models.CharField(
        max_length=20,
        choices=[
            ('Pending','Pending'),
            ('Shipped','Shipped'),
            ('Delivered','Delivered')
        ],
        default='Pending'
    )
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"