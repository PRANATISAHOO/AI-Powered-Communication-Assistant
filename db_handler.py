# db_handler.py
from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority")
db = client["support_assistant"]
emails_collection = db["emails"]

def save_email(email_data):
    emails_collection.insert_one(email_data)

def get_all_emails():
    return list(emails_collection.find({}, {"_id": 0}))
