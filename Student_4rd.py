''' Find the total and average of the exam, quiz and homework and
 store them in a separate collection.'''
 
import pymongo 

myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=myclient["student_DB"]
mycol=mydb["students_record"]
total_avg=mydb.total_avg

data=mycol.aggregate([
    {"$unwind":"$scores"},
    {"$group":
     {
         "_id":"$_id",
        "name":{"$first":"$name"}
      ,
     "Total":{"$sum":"$scores.score"},
      "Average":{"$avg":"$scores.score"}
      }
     },
     {"$sort":{"_id":1}}
     
     ])

data1=[]
for i in data:
  data1.append(i)
  print(i)

total_avg.insert_many(data1)
