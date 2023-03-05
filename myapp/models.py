from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Budget_Years(models.Model):
    name = models.CharField(max_length=4)

class Categories(models.Model):
    CATEGORY_CHOICES = (
        ('housing','Housing'),
        ('automobile','Automobile'),
        ('food','Food'),
        ('healthcare','Healthcare'),
        ('education','Education'),
        ('insurance','Insurance'),
        ('taxes','Taxes'),
        ('leisure','Leisure'),
        ('debt payment','Debt Payment'),
        ('investments','Investments'),
        ('income','Income'),
        ('miscellaneous','Miscellaneous'),
    )
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

class Subcategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    SUBCATEGORY_CHOICES = (
        ('gas','Gas'),
        ('maintenance','Maintenance'),
        ('parking','Parking'),
        ('credit_cards','Credit Cards'),
        ('loan_payments','Loan Payments'),
        ('books','Books'),
        ('student loans','Student Loans'),
        ('tuition','Tuition'),
        ('groceries','Groceries'),
        ('dining out','Dining Out'),
        ('co-pays','Co-Pays'),
        ('insurance','Insurance'),
        ('other_healthcare','Other Healthcare'),
        ('prescriptions','Prescriptions'),
        ('clothing','Clothing'),
        ('furnishings','Furnishings'),
        ('internet_tv','Internet / TV'),
        ('rent','Rent'),
        ('telephone','Telephone'),
        ('utilities','Utilities'),
        ('other income','Other Income'),
        ('wages','Wages'),
        ('investment income','Investment Income'),
        ('auto','Auto'),
        ('home','Home'),
        ('life','Life'),
        ('going out','Going Out'),
        ('vacation','Vacation'),
        ('investment purchase','Investment Purchase'),
        ('misc. expenses','Misc. Expenses'),
        ('investment sale','Investment Sale'),
        ('income_tax','Income Tax'),
        ('tax_refund','Tax Refund'),
        ('other_tax','Other Tax'),
    )
    name = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES)

class Budget_Items(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    year_id = models.ForeignKey(Budget_Years, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class Transactions(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(auto_now=False, null=False)
    description = models.CharField(max_length=100)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class User_Category_Subcategory_Selections(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)    
