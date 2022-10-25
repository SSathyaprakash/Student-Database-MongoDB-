#1)Find the student name who scored maximum scores in all (exam, quiz and homework)?


import pymongo

myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=myclient["student_DB"]
mycol=mydb["students_record"]

data= mycol.aggregate([
    {"$unwind":"$scores"},
    {"$group":{"_id":"$_id","name":{"$first":"$name"},"Total":{"$sum":"$scores.score"}}},
    {"$sort":{"Total":-1}},
    {"$limit":1}
    ])
    
for i in data:
    print(i)