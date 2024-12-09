import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongo:27017/cadastro')  
DATABASE_NAME = os.getenv('DATABASE_NAME')

cliente = MongoClient(MONGO_URI)
db = cliente[DATABASE_NAME]

def obter_colecao(nome_da_colecao):
    return db[nome_da_colecao]
