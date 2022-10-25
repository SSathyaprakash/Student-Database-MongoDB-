'''Create a new collection which consists of students
 who scored below average and above 40% in all the categories'''
 
 
import pymongo 

myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=myclient["student_DB"]
mycol=mydb["students_record"]
Avgrage_Candidates=mydb.Avgrage_Candidates

data=mycol.aggregate(
[{"$match": 
   {"$expr": 
     {"$and": 
       [{"$gt": [{"$min": "$scores.score"}, 40]},
         {"$lt": [{"$max": "$scores.score"}, 70]}
        ]
      }
    }
  }])

Data1= []
for i in data:
  Data1.append(i)
  print(i)
  
Avgrage_Candidates.insert_many(Data1)