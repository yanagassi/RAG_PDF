from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from app.settings.config import settings
import logging

logger = logging.getLogger(__name__)


# Adicione o splitter para dividir o texto em partes menores, tentando seguir o exemplo do bate-papo que tivemos na entrevista tecnica.
def armazenar_documento(texto: str, chunk_size: int = 1000, chunk_overlap: int = 200):

    texto_limpo = " ".join(
        texto.split()
    )  # Adicionei esse trecho para limpar espaços extras e quebras desnecessárias

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len
    )

    docs = splitter.create_documents([texto_limpo])

    logger.info(f"Documento dividido em {len(docs)} chunks")
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001", google_api_key=settings.GOOGLE_API_KEY
    )

    Chroma.from_documents(
        docs, embeddings, persist_directory=settings.VECTOR_DIR
    ).persist()


def carregar_vectorstore():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001", google_api_key=settings.GOOGLE_API_KEY
    )
    return Chroma(persist_directory=settings.VECTOR_DIR, embedding_function=embeddings)
