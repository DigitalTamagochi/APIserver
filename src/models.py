from mongoengine import *
# from .config import DB_HOST
DB_HOST = "mongodb+srv://admin:GvCajyHU4BdLcAuB@cluster0.3vpqs.mongodb.net/total_records?retryWrites=true&w=majority"
connect(host=DB_HOST)


class user(Document):
    my_id = IntField(primary_key=True)
    login = StringField(max_length=100)
    email = StringField(max_length=100)
    first_name = StringField(max_length=100)
    second_name = StringField(max_length=100)
    not_hashed_password = StringField()

    valid_token = StringField()

    list_id = IntField()

class jest(Document):
    my_id = IntField(primary_key=True)
    name = StringField()
    description = StringField()
    # iterations = ListField(IntField())
    # progress_type = IntField()

class jest_list(Document):
    my_id = IntField()
    login = StringField()

    jest_info = DictField()
    data = ListField(IntField())
