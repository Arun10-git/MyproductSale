from django.db import models

class prodsales(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    desc = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name
 
class cart(models.Model):
    product=models.ForeignKey(prodsales,null=True,on_delete=models.CASCADE)
    buyer=models.CharField(max_length=100,default="unknown")
    quantity=models.IntegerField()
    total_amount=models.IntegerField(null=True, blank=True)

   

