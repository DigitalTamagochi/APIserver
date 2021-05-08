from mongoengine import *
# from .config import DB_HOST
DB_HOST = "mongodb+srv://admin:<password>@cluster0.3vpqs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

connect(host=DB_HOST)


class user(Document):
    my_id = IntField(primary_key=True)
    login = StringField(max_length=100)
    email = StringField(max_length=100)
    first_name = StringField(max_length=100)
    second_name = StringField(max_length=100)
    not_hashed_password = StringField()


class pet(Document):
    my_id = IntField(primary_key=True, required=True)
    name = StringField(required=True)
    description = StringField()
    iterations = ListField(IntField(), required=True)
