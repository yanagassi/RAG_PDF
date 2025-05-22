from fastapi import FastAPI, UploadFile, File
from app.service.rag import responder_pergunta
from app.service.pdf_processor import processar_pdf
from app.repo.vector_store import armazenar_documento
from app.repo.qa_repository import salvar_qa
from app.repo.schemas import PerguntaRequest

app = FastAPI()


@app.post("/enviar-pdf/")
async def enviar_pdf(file: UploadFile = File(...)):
    texto = await processar_pdf(file)
    armazenar_documento(texto)
    return {"mensagem": "PDF processado e armazenado com sucesso."}


@app.post("/perguntar/")
async def perguntar(payload: PerguntaRequest):
    resposta = responder_pergunta(payload.pergunta)
    salvar_qa(payload.pergunta, resposta)
    return {"resposta": resposta}
