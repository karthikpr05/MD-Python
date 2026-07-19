#if the incoming data is invalid, the request never reaches your function, Pydantic helps you to validate that the data you are receiving from the client is in the expected format or no!


without pydantic

@app.post("/students")
def create_student(student: dict):
    collection.insert_one(student)
    return {"message": "created"}

{
    "name": "Pranav",
    "age": "Twenty Four",
    "city": 12345
}

so with the help of pydantic we create a schema defining how the data should flow from frontend