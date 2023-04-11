from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from budget.forms import SubcategoryForm, CategoryForm, BudgetItemForm, BudgetYearForm, TransactionForm
from budget.models import Categories, Subcategories, BudgetItem, BudgetYear, Transaction

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
        form = SubcategoryForm(request.POST, user=user)
        if form.is_valid():
            subcategory = Subcategories(
                user = user,
                subcategory_name=form.cleaned_data['subcategory_name'],
                category = form.cleaned_data['category']
            )
            subcategory.save()
    else:
        form = SubcategoryForm(user=user)
    return render(request, 'create_subcategory.html', {'form': form, 'user': user})

def create_budget_item(request):
    user = request.user
    if request.method == 'POST':
        form =BudgetItemForm(request.POST)
        if form.is_valid():
            subcategory=form.cleaned_data['subcategory']
            category = subcategory.category
            budget_item = BudgetItem(
                user = user,
                budget_year = form.cleaned_data['budget_year'],
                subcategory=subcategory,
                category=category,
                frequency=form.cleaned_data['frequency'],
                amount=form.cleaned_data['amount'],
                notes=form.cleaned_data['notes'],                
            )
            budget_item.save()
            return redirect('create_budget_item')
    else:
        form = BudgetItemForm(user=user)
    return render(request, 'budget/create_budget_item.html', {'form': form})

def add_budget_year(request):
    if request.method == 'POST':
        form = BudgetYearForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            budget_year = BudgetYear(year=year)
            budget_year.save()
            return redirect('create_budget_item')
    else:
        form = BudgetYearForm()
    return render(request, 'budget/add_budget_year.html', {'form': form})

@login_required
def my_budget(request):
    user = request.user
    budget_items = BudgetItem.objects.filter(user=user).order_by('category')

    context = {'budget_items': budget_items}
    return render(request, 'budget/budget.html', context)

@login_required
def my_categories(request):
    user = request.user
    categories = Categories.objects.filter(user=user)

    context = {'categories': categories}
    return render(request, 'my_categories.html', context)

@login_required
def my_subcategories(request):
    user = request.user
    subcategories = Subcategories.objects.filter(user=user).order_by('category')

    context = {'subcategories': subcategories}
    return render(request, 'my_subcategories.html', context)

@login_required
def reports(request):
    return render(request, 'reports.html')

@login_required
def create_transaction(request):
    user = request.user
    if request.method == 'POST':
        form =TransactionForm(request.POST)
        if form.is_valid():
            subcategory=form.cleaned_data['subcategory']
            category = subcategory.category
            transaction = Transaction(
                user = user,
                date = form.cleaned_data['date'],
                subcategory=subcategory,
                category= category,
                amount=form.cleaned_data['amount'],
                notes=form.cleaned_data['notes'],                
            )
            transaction.save()
            return redirect('create_transaction')
    else:
        form = TransactionForm(user=user)
    return render(request, 'create_transaction.html', {'form': form})

@login_required
def my_transactions(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user).order_by('date')

    context = {'transactions': transactions}
    return render(request, 'my_transactions.html', context)