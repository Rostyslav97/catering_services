from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=70, unique=True)
    description = models.TextField()
    spicy = models.BooleanField(null=True, blank=True, default=None)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    output = models.CharField(max_length=20)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Category(models.Model):

    CATEGORY_CHOICES = (
        ('CS', 'Cold Snack'),
        ('HS', 'Hot Snack'),
        ('S', 'Salads'),
        ('PD', 'Pork dishes'),
        ('CD', 'Chicken dishes'),
        ('BD', 'Bird dishes'),
        ('SD', 'Side dishes'),
        ('D', 'Desserts'),
        ('DR', 'Drinks'),
        ('SN', 'Snacks')
    )

    name = models.CharField(max_length=2, choices=CATEGORY_CHOICES)