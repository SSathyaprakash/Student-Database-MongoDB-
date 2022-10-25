''' Create a new collection which consists of students 
who scored below the fail mark in all the categories'''

import pymongo 

myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=myclient["student_DB"]
mycol=mydb["students_record"]
fail=mydb.fail


query={}
data=mycol.aggregate(
[{"$match": 
   {"$expr": 
     
       {"$lt": [{"$max": "$scores.score"}, 40]}
      
    }
  }])

faila = []
for i in data:
  faila.append(i)
  print(i)
  
fail.insert_many(faila)