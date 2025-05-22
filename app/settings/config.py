import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017")
    VECTOR_DIR = os.getenv("VECTOR_DIR", "vector_data")


settings = Settings()
