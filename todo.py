import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://amankhanathani:<PASSWORD>12@cluster0.9gp2f.mongodb.net/<DB>?retryWrites=true&w=majority")
db = client["mydata"]

collection = db["mydata"]


post = {"_id":1,"task":"lunch","when":"noon"}

collection.insert_one(post)


