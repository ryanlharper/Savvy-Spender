from django.contrib.auth.models import User
from django import forms
from budget.models import Categories, Subcategories, BudgetYear
from django.forms.widgets import DateInput

class CategoryForm(forms.Form):
   type = forms.ChoiceField(choices=[('IN', 'Income'), ('EX', 'Expense')])
   category_name =  forms.CharField()

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategories
        fields = ['subcategory_name', 'category']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Categories.objects.filter(user=user)

    subcategory_name = forms.CharField()

class BudgetItemForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['subcategory'].queryset = Subcategories.objects.filter(user=user)
    
    subcategory = forms.ModelChoiceField(queryset=Subcategories.objects.all())
    budget_year = forms.ModelChoiceField(queryset=BudgetYear.objects.all())
    frequency = forms.ChoiceField(choices=[('YR','Yearly'),('MN',"Monthly")])
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    notes = forms.CharField(max_length=128, required=False)

class BudgetYearForm(forms.ModelForm):
    year = forms.CharField(max_length=4)

    def clean_year(self):
        year = self.cleaned_data['year']
        if BudgetYear.objects.filter(year=year).exists():
            raise forms.ValidationError('This year already exists.')
        return year

    class Meta:
        model = BudgetYear
        fields = ['year']

class TransactionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['subcategory'].queryset = Subcategories.objects.filter(user=user)
    
    date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    subcategory = forms.ModelChoiceField(queryset=Subcategories.objects.all())
    notes = forms.CharField(max_length=128, required=False)

class UploadTransactionForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')