from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from budget.forms import SubcategoryForm, CategoryForm
from budget.models import Categories, Subcategories

@login_required
def create_category(request):
    user = request.user
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Categories(
            user=user,
            category_name=form.cleaned_data['category_name'],
            type=form.cleaned_data['type']
            )
            category.save()
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form, 'user': user})

@login_required
def create_subcategory(request):
    user = request.user
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            subcategory = Subcategories(
                user = user,
                subcategory_name=form.cleaned_data['subcategory_name'],
                category = form.cleaned_data['category']
            )
            subcategory.save()
    else:
        form = SubcategoryForm()
    return render(request, 'create_subcategory.html', {'form': form, 'user': user})

def CreateBudgetItem(request):
    pass

def CreateTransaction(request):
    pass