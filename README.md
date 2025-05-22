# Projeto RAG com FastAPI, Langchain e MongoDB

Este projeto implementa uma solução RAG (Retrieval Augmented Generation) com as seguintes funcionalidades principais:

- Processamento de arquivos PDF
- Armazenamento em base vetorial
- Endpoint para realização de perguntas
- Persistência das perguntas com suas respectivas respostas

## Tecnologias Utilizadas

- Langchain
- FastAPI
- Base vetorial (Chroma ou Pinecone)
- LLM Gemini 2 Flash (gratuito)
- Ambiente com Docker e Docker Compose
- Banco NoSQL para armazenamento de perguntas e respostas

## Como Rodar

1. Clone o repositório:

```bash
git clone https://github.com/yanagassi/RAG_PDF.git
cd RAG_PDF
```

2. Crie um arquivo `.env` baseado no arquivo `.env.example` e configure a chave de API do Google:

```env
GOOGLE_API_KEY=sua-chave-google
```

> **Importante:** Não esqueça de habilitar o serviço _Generative Language_ para a sua chave na Google Cloud.

3. Suba os containers usando Docker Compose:

```bash
docker-compose up --build
```

4. Acesse a documentação da API em: [http://localhost:8000/docs](http://localhost:8000/docs)

> Adicionei também uma collection do Postman além do Swagger para facilitar os testes.

## Evidências de Teste

##### Utilizei o mesmo exemplo mencionado na reunião, que é o meu currículo, considerando que a IA não sabe o tipo do arquivo.

### Envio do arquivo PDF para a API

![Evidência de Envio do PDF](evidencia/Evidencia%20de%20request%20de%20envio%20de%20PDF.png)

### Envio de pergunta e resposta gerada

![Evidência de Resposta](evidencia/Evidencia%20de%20resposta%20gerada.png)
