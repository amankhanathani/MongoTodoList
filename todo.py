import pymongo
import time
import datetime
from datetime import date
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://amankhanathani:<PASSWORD>@cluster0.9gp2f.mongodb.net/mydata?retryWrites=true&w=majority")
db = client["mydata"]


collection = db["mydata"]

now = (datetime.datetime.now(),0)
future = (datetime.datetime(2021, 7, 22, 17, 17, 36),0)



'''post = {"_id":6,"task":"breakfast","set on":now[0],"set for":future[0],"status":"incomplete"}
collection.insert_one(post)'''

'''collection.delete_one({"_id":1})'''

'''collection.replaceOne({"_id":3},{"set for":now[0]})'''

'''collection.find_one_and_update({"_id":3},{"set for":now[0]})'''


print(collection.find_one({"_id": 3}))
