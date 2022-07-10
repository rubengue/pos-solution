import json
import boto3
import uuid
from products.tenant import Tenant

class Category:
    def __init__(self, id, title, tenantid):
        self.id = str(uuid.uuid1())
        self.title = title
        self.tenantid = Tenant.id