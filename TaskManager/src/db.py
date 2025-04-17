from pymongo import MongoClient

# Substitua a string abaixo se estiver usando o MongoDB Atlas
client = MongoClient("mongodb://localhost:27017/")
db = client["task_manager_db"]
tarefas_collection = db["tarefas"]
