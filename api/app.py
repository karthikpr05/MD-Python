from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI(
    title="Student CRUD operation",
    description="Simple CRUD API using fast API and MongoDB",
    version="1.0"
)

#Establish connection with your DB
client = MongoClient("mongodb://admin:password@localhost:27017/")
db = client["training_db"]
collection = db["students"]

@app.get("/students")
def get_students():

    students=[]
    for student in collection.find():
      student["_id"] = str(student["_id"])
      students.append(student)

    return students

@app.post("/students")
def create_student(student: dict):
    result = collection.insert_one(student)

    return{
        "message":"Student created",
        "id": str(result.inserted_id)
    }