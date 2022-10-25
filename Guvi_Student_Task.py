import pymongo   # Importing Mongo Module
import json      # Importing json Module


#Connection to Mongo Server
myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/")

# Creating the Database
mydb=myclient.student_DB
# Creating the Collection
mycol = mydb.students_record

#Extracting Data from Json 
with open("students.json") as students:
  Data = [json.loads(i) for i in students]

# Inserting Data in to Collection
mycol.insert_many(Data)

