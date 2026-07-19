# requirements.txt file is responsible to have all the libraries mentioned or required
# for your application run.

# We would be using FastAPI server, which is a Python framework to develop and run Python applications.

# Swagger would be our API testing tool.

#Library -> calculator (add, sub, div, mul) 
#fastapi : Framework to run your python application
#uvicorn: Helps you to run your application at desired port and also pops up swagger to test your api's
#Application -> calculator (go and use the library developed by Pranav)

#pip install -r requirements.txt (used to install all the libraries in one go)

#In order to setup MongoDB dB 
Steps to follow

1. Install Docker (ChatGPT) -> use CLI to install Docker
2. docker pull mongo
3. docker run -d --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password mongo