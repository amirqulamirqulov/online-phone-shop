from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'brands/', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Phone (models.Model):
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    ram = models.IntegerField()
    memory = models.IntegerField()
    price = models.IntegerField()
    images = models.ImageField(upload_to = 'phones/', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.brand}  {self.name}  {self.ram}  {self.memory} {self.price} "


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    phone = models.ForeignKey(Phone, on_delete = models.DO_NOTHING)

    

