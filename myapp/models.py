from django.db import models

# Create your models here.
class Product_mst(models.Model):
    name=models.TextField(unique=True)


    def __str__(self):
        return self.name
class Product_category(models.Model):
   name= models.ForeignKey(Product_mst,on_delete=models.CASCADE)
   product_model= models.CharField(max_length=10)
   product_price=models.IntegerField()
   product_ram= models.IntegerField()
   product_image=models.FileField(upload_to="product_photo")

   def __str__(self):
       return self.product_model


