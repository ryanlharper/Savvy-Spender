from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

class UserSelection(db.Model):
    __tablename__ = 'user_category_subcategory_selections'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), primary_key=True)
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategories.id'), primary_key=True)
    selected = db.Column(db.Boolean)

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)

    def __init__(self, name: str):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
        
class Subcategory(db.Model):
    __tablename__ = 'subcategories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __init__(self, name: str, category_id: int):
        self.name = name
        self.category_id = category_id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'category_id': self.category_id,
        }

class BudgetYear(db.Model):
    __tablename__ = 'budget_years'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.String(4), nullable=False)

class Budget(db.Model):
    __tablename__ = 'budget_items'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    year_id = db.Column(db.Integer, db.ForeignKey('budget_years.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategories.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, amount: float, year_id: int, category_id: int, subcategory_id: int, user_id: int):
        self.amount = amount
        self.year_id = year_id
        self.category_id = category_id
        self.subcategory_id = subcategory_id
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'amount': str(self.amount),
            'year_id': self.year_id,
            'category_id': self.category_id,
            'subcategory_id': self.subcategory_id,
            'user_id': self.user_id
        }

class Transaction(db.Model):
    __tablename__ = 'transactions'  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategories.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(128), nullable=True)

    def __init__(self, amount: float, date: date, category_id: int, subcategory_id: int, user_id: int, description: str):
        self.amount = amount
        self.date = date
        self.category_id = category_id
        self.subcategory_id = subcategory_id
        self.user_id = user_id
        self.description = description

    def serialize(self):
        return {
            'id': self.id,
            'amount': str(self.amount),
            'date': self.date,
            'category_id': self.category_id,
            'subcategory_id': self.subcategory_id,
            'user_id': self.user_id,
            'description': self.description
        }
