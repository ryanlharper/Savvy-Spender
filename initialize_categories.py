from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Initialize default categories and subcategories'

    def handle(self, *args, **options):
        from categories.models import Categories, Subcategories
        # Create categories
        housing_category = Categories.objects.create(id=1,name='Housing')
        automobile_category = Categories.objects.create(id=2,name='Automobile')
        food_category = Categories.objects.create(id=3,name='Food')
        healthcare_category = Categories.objects.create(id=4,name='Healthcare')
        education_category = Categories.objects.create(id=5,name='Education')
        insurance_category = Categories.objects.create(id=6,name='Insurance')
        taxes_category = Categories.objects.create(id=7,name='Taxes')
        leisure_category = Categories.objects.create(id=8,name='Leisure')
        debt_payment_category = Categories.objects.create(id=9,name='Debt Payment')
        investments_category = Categories.objects.create(id=10,name='Investments')
        income_category = Categories.objects.create(id=11,name='Income')
        miscellaneous_category = Categories.objects.create(id=12,name='Miscellaneous')

        # Create subcategories
        Subcategories.objects.create(category_id=housing_category.id, name='Rent / Mortgage')
        Subcategories.objects.create(category_id=housing_category.id, name='Utilities')
        Subcategories.objects.create(category_id=housing_category.id, name='Furnishings')
        Subcategories.objects.create(category_id=housing_category.id, name='Internet / TV')
        Subcategories.objects.create(category_id=housing_category.id, name='Telephone')                                                       
        Subcategories.objects.create(category_id=automobile_category.id, name='Gas')
        Subcategories.objects.create(category_id=automobile_category.id, name='Maintenance')
        Subcategories.objects.create(category_id=automobile_category.id, name='Parking')
        Subcategories.objects.create(category_id=food_category.id, name='Groceries')
        Subcategories.objects.create(category_id=food_category.id, name='Dining Out')
        Subcategories.objects.create(category_id=healthcare_category.id, name='Health Insurance')
        Subcategories.objects.create(category_id=healthcare_category.id, name='Co-pays')
        Subcategories.objects.create(category_id=healthcare_category.id, name='Prescriptions')
        Subcategories.objects.create(category_id=healthcare_category.id, name='Other Healthcare')
        Subcategories.objects.create(category_id=education_category.id, name='Tuition')
        Subcategories.objects.create(category_id=education_category.id, name='Books')
        Subcategories.objects.create(category_id=education_category.id, name='Student Loans')
        Subcategories.objects.create(category_id=insurance_category.id, name='Life Insurance')
        Subcategories.objects.create(category_id=insurance_category.id, name='Homeowners/Renters Insurance')
        Subcategories.objects.create(category_id=insurance_category.id, name='Auto Insurance')
        Subcategories.objects.create(category_id=taxes_category.id, name='Income Tax')
        Subcategories.objects.create(category_id=taxes_category.id, name='Other Tax')
        Subcategories.objects.create(category_id=leisure_category.id, name='Travel')
        Subcategories.objects.create(category_id=leisure_category.id, name='Going Out')
        Subcategories.objects.create(category_id=debt_payment_category.id, name='Credit Card Payment')
        Subcategories.objects.create(category_id=debt_payment_category.id, name='Loan Payment')
        Subcategories.objects.create(category_id=investments_category.id, name='Investment Purchase')
        Subcategories.objects.create(category_id=income_category.id, name='Wages')
        Subcategories.objects.create(category_id=income_category.id, name='Investment Income')
        Subcategories.objects.create(category_id=income_category.id, name='Tax Refund')
        Subcategories.objects.create(category_id=income_category.id, name='Other Income')
        Subcategories.objects.create(category_id=income_category.id, name='Investment Sale')
        Subcategories.objects.create(category_id=miscellaneous_category.id, name='Misc. Expense')
        Subcategories.objects.create(category_id=miscellaneous_category.id, name='Clothing')