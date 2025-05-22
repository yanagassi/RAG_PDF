from PyPDF2 import PdfReader
import io


async def processar_pdf(file) -> str:
    conteudo = await file.read()
    leitor = PdfReader(io.BytesIO(conteudo))
    texto = "".join([pagina.extract_text() or "" for pagina in leitor.pages])
    return texto
