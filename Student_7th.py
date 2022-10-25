''' Create a new collection which consists of students
 who scored above pass mark in all the categories'''
 

import pymongo 

myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=myclient["student_DB"]
mycol=mydb["students_record"]
passed=mydb.passed


query={}
data=mycol.aggregate(
[{"$match": 
   {"$expr": 
     
       {"$gt": [{"$max": "$scores.score"}, 40]}
      
    }
  }])

passed1 = []
for i in data:
  passed1.append(i)
  print(i)
  
passed.insert_many(passed1)