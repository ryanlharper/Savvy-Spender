from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from budget.forms import SubcategoryForm, CategoryForm, BudgetItemForm, BudgetYearForm, TransactionForm, UploadTransactionForm
from budget.models import Categories, Subcategories, BudgetItem, BudgetYear, Transaction
import csv, codecs
from datetime import datetime

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

@login_required
def upload_transactions_csv(request):
    if request.method == 'POST':
        form = UploadTransactionForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the CSV file
            csv_file = request.FILES['csv_file']
            # Open the file in text mode using codecs module
            reader = csv.reader(codecs.iterdecode(csv_file, 'utf-8'))

            # Specify the field names
            field_names = ['date', 'amount', 'skip1', 'skip2', 'notes']

            # Loop over the rows and create a new Transaction instance for each row
            transactions = []
            for row in reader:
                # Create a dictionary with the field names as keys and the row values as values
                data_dict = dict(zip(field_names, row))
                amount = float(data_dict['amount'])
                if amount < 0:
                    amount = abs(amount)
                transaction = Transaction(
                    user=request.user,
                    date=data_dict['date'],
                    amount=amount,
                    notes=data_dict['notes']
                )
                transactions.append(transaction)

            subcategories = Subcategories.objects.filter(user=request.user)
            return render(request, 'edit_transactions.html', {'transactions': transactions, 'subcategories': subcategories})
    else:
        form = UploadTransactionForm()
    
    subcategories = Subcategories.objects.filter(user=request.user)
    return render(request, 'upload_transactions.html', {'form': form})

@login_required
def save_transactions(request):
    if request.method == 'POST':
        # Get the form data
        subcategory_ids = request.POST.getlist('subcategory')
        print(subcategory_ids)
        notes = request.POST.getlist('notes')
        transaction_ids = request.POST.getlist('transaction_id')
        transaction_dates = request.POST.getlist('transaction_date')
        transaction_amounts = request.POST.getlist('transaction_amount')

        # Loop over the transaction data and update the database
        for i, transaction_id in enumerate(transaction_ids):
            # Get the corresponding Transaction object
            transaction = Transaction.objects.get(id=transaction_id)

            # Get the corresponding Subcategories object
            subcategory_id = subcategory_ids[i]
            subcategories = Subcategories.objects.get(id=subcategory_id)

            # Get the Category object associated with the Subcategories
            category = subcategories.category

            # Update the transaction with the selected subcategory, category, and notes
            transaction.subcategories = subcategories
            transaction.category = category
            transaction.notes = notes[i]

            # Update the transaction with the original date and amount
            transaction.date = transaction_dates[i]
            transaction.amount = transaction_amounts[i]

            # Save the updated transaction to the database
            transaction.save()

        # Redirect the user to the transactions page
        return redirect('my_transactions')