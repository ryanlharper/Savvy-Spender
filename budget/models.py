from django.db import models
from django.contrib.auth.models import User

class BudgetYear(models.Model):
    year = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.year

class Categories(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=128)
    TYPE_CHOICES = [
        ("IN", "Income"),
        ("EX", "Expense"),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES
    )

    unique_together = ('user' , 'category_name')

    def __str__(self):
        return self.category_name

class Subcategories(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=128)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    unique_together = ('user' , 'subcategory_name')

    def __str__(self):
        return self.subcategory_name

class BudgetItem(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    budget_year = models.ForeignKey(BudgetYear, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)	
    notes = models.CharField(max_length=128, null=True)

class Transaction(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    notes = models.CharField(max_length=128, null=True)