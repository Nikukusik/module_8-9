from mongoengine import *


class Author(Document):
    _id = ObjectIdField()
    fullname = StringField(max_length=100)
    born_date = StringField(max_length=100)
    born_location = StringField(max_length=100)
    description = StringField(max_length=10000)
class Quote(Document):
    tags = ListField()
    author = ReferenceField(Author)
    quote = StringField(max_length=10000)
