from app.repo.vector_store import carregar_vectorstore
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from app.settings.config import settings


def responder_pergunta(pergunta: str) -> str:
    retriever = carregar_vectorstore().as_retriever()
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-flash", google_api_key=settings.GOOGLE_API_KEY
    )
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain.run(pergunta)
