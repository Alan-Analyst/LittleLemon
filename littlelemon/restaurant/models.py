from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200) 
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField()


class Menu(models.Model):
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory = models.IntegerField() 

    def __str__(self):
        return f'{self.title} : {str(self.price)}'