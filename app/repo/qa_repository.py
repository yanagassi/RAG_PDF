from pymongo import MongoClient
from app.settings.config import settings

cliente = MongoClient(settings.MONGO_URI)
db = cliente["rag"]
colecao = db["perguntas_respostas"]


def salvar_qa(pergunta: str, resposta: str):
    colecao.insert_one({"pergunta": pergunta, "resposta": resposta})
