import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.nlp_utils import detect_language, translate_to_english, extract_intent_entities, match_schemes

app = FastAPI()

# CORS settings — allow React dev server origins and all methods including OPTIONS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # <--- very important to allow OPTIONS/preflight
    allow_headers=["*"],
)

# Load schemes data at startup
with open("data/schemes.json", "r", encoding="utf-8") as f:
    schemes_data = json.load(f)

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Welcome to the Government Scheme Chatbot API!"}

@app.post("/query")
async def query_handler(request: QueryRequest):
    query = request.query

    lang = detect_language(query)
    query_en = translate_to_english(query, lang)
    intent, entities = extract_intent_entities(query_en)
    matched = match_schemes(query_en, schemes_data)

    return {
        "language": lang,
        "intent": intent,
        "entities": entities,
        "schemes": matched
    }
