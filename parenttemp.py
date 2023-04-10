class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', null=True, blank=True, related_name='child_categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


debt = Category.objects.create(name='Debt')
credit_cards = Category.objects.create(name='Credit Cards', parent_category=debt)
loans = Category.objects.create(name='Loans', parent_category=debt)

housing = Category.objects.create(name='Housing')
rent = Category.objects.create(name='Rent', parent_category=housing)


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, limit_choices_to={'parent_category__isnull': False})


<select name="category">
    {% for category in root_categories %}
        <option value="{{ category.id }}">{{ category.name }}</option>
        {% for subcategory in category.child_categories.all %}
            <option value="{{ subcategory.id }}">- {{ subcategory.name }}</option>
        {% endfor %}
    {% endfor %}
</select>
