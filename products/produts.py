import json
import boto3
import uuid
from products.category import Category
from products.flavors import Flavors
from products.ingredients import Ingredients

from products.tenant import Tenant

class Product:
    def __init__(self, id, title, description, price, ingredients, flavor, belong_to, category ):
        self.id = str(uuid.uuid1())
        self.title = title
        self.belong_to = Tenant.id
        self.description = description
        self.price = price
        self.ingredients = Ingredients.tenantid.title
        self.flavor = Flavors.title
        self.category = Category.tenantid.title
    