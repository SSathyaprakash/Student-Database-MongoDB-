'''Find students who scored below pass mark and assigned them as fail, 
and above pass mark as pass in all the categories'''


import pymongo

myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=myclient["student_DB"]
mycol=mydb["students_record"]

data=mycol.aggregate(
[ {"$set": 
   {"scores": 
     {"$arrayToObject": 
       [{"$map": 
           {"input": "$scores",
            "as": "s",
            "in": {"k": "$$s.type", "v": "$$s.score"}}}]}}},
 {"$project":
  {
     "_id":1,
     "name":1,
     "result":{
            "$cond":
                    {"if": {"$and" : [{"$gte": ["$scores.exam", 40]}, {"$gte": ["$scores.quiz", 40]}, {"$gte": [ "$scores.homework", 40]}]
                            },
                    "then" :"pass",
                    "else":"fail"
                    }
               }
  }
}
  ])
    
for i in data:
    print(i)