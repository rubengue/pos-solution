import json
import boto
import uuid
from products.tenant import Tenant

class Ingredients:
    def __init__(self, id, title, tenantid):
        self.id = str(uuid.uuid1())
        self.title = title
        self.tenantid = Tenant.id
        