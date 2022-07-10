import json
import boto
import uuid

class Tenant:
    def __init__(self, id, name, description, address):
        self.id = str(uuid.uuid1())
        self.name = name
        self.description = description
        self.address = address