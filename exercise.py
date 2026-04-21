from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["gym"]

customers = db["customers"]
memberships = db["memberships"]
visitlogs = db["visitlogs"]


# Customer CRUD MongoDB calls
def create_customer(customer):
    return db.customers.insert_one(customer)

def update_customer(customer_id, data):
    return db.customers.update_one(
        {"_id": ObjectId(customer_id)},
        {"$set": data}
    )

def delete_customer_by_id(customer_id):
    return db.customers.delete_one({"_id": ObjectId(customer_id)})

def get_customer_by_id(customer_id):
    return db.customers.find_one({"_id": ObjectId(customer_id)})

def get_customers():
     return db.customers.find()


# Membership CRUD MongoDB calls
def create_membership(membership):
    return db.memberships.insert_one(membership)

def update_membership(membership_id, data):
    return db.memberships.update_one(
        {"_id": ObjectId(membership_id)},
        {"$set": data}
    )

def delete_membership_by_id(membership_id):
    return db.memberships.delete_one({"_id": ObjectId(membership_id)})

def get_membership_by_id(membership_id):
    return db.memberships.find_one({"membershipID": int(membership_id)})

def get_memberships():
    return db.memberships.find()


# Visitlog CRUD MongoDB calls

def get_visitlog_by_membership_id(membership_id):
     return db.visitlogs.find({"membershipID": int(membership_id)})
