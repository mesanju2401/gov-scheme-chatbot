from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend import nlp_utils, db
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load schemes from JSON
with open("data/schemes.json", "r", encoding="utf-8") as f:
    schemes_data = json.load(f)

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Government Scheme Chatbot API!"}

@app.post("/query")
async def handle_query(request: QueryRequest):
    user_input = request.query
    
    lang = nlp_utils.detect_language(user_input)
    translated_text = nlp_utils.translate_to_english(user_input, lang)
    
    intent, entities = nlp_utils.extract_intent_entities(translated_text)
    matched_schemes = db.find_matching_schemes(schemes_data, intent, entities)
    
    return {
        "language": lang,
        "intent": intent,
        "entities": entities,
        "schemes": matched_schemes
    }
