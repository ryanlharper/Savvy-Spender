"""savvy_spender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 
from savvy_spender.views import SignUpView
from budget.views import create_category, create_subcategory, create_budget_item, create_transaction
from budget.views import add_budget_year, my_budget, my_categories, my_subcategories, reports, my_transactions
from budget.views import upload_transactions_csv, save_transactions
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('register/', SignUpView.as_view(), name='register'),
    path('categories/', create_category, name = 'categories'),
    path('subcategories/', create_subcategory, name= 'subcategories'),
    path('budget/create', create_budget_item, name= 'create_budget_item'),
    path('budget/add-year', add_budget_year, name= 'add_budget_year'),
    path('budget/my_budget', my_budget, name= 'my_budget'),
    path('my_categories', my_categories, name= 'my_categories'),
    path('my_subcategories', my_subcategories, name= 'my_subcategories'),
    path('reports/', reports, name= 'reports'),
    path('create_transaction/', create_transaction, name= 'create_transaction'),
    path('my_transactions/', my_transactions, name= 'my_transactions'),
    path('upload_transactions/', upload_transactions_csv, name= 'upload_transactions'),
    path('save_transactions/', save_transactions, name= 'save_transactions'),
]