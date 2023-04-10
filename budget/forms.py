from django.contrib.auth.models import User
from django import forms
from budget.models import Categories
from django.contrib.auth import get_user_model
User = get_user_model()


class CategoryForm(forms.Form):
   type = forms.ChoiceField(choices=[('IN', 'Income'), ('EX', 'Expense')])
   category_name =  forms.CharField()

class SubcategoryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Categories.objects.filter(user=user)

    category = forms.ModelChoiceField(queryset=Categories.objects.all())
    subcategory_name = forms.CharField()