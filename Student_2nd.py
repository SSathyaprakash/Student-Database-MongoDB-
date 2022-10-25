#2)Find students who scored below average in the exam and pass mark is 40%?


import pymongo

myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=myclient["student_DB"]
mycol=mydb["students_record"]

query={'scores.type':'exam','scores.score':{'$gt':40,'$lt':60}}

data= mycol.aggregate([
    {'$unwind':'$scores'},
    {"$match":query}
    ])
    
for i in data:
    print(i)