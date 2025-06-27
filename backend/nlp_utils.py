from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect
import torch

# Language to MarianMT model map
model_name_map = {
    'hi': 'Helsinki-NLP/opus-mt-hi-en',
    # Add more languages as needed
}

# Cache translation models
translation_models = {}

def detect_language(text: str) -> str:
    try:
        return detect(text)
    except Exception:
        return "en"

def translate_to_english(text: str, src_lang: str) -> str:
    if src_lang == 'en' or src_lang not in model_name_map:
        return text

    if src_lang not in translation_models:
        model_name = model_name_map[src_lang]
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        translation_models[src_lang] = (tokenizer, model)

    tokenizer, model = translation_models[src_lang]
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        translated_tokens = model.generate(**inputs)
    return tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

# Intent and entity mapping
intent_entity_map = {
    "loan": ("get_loan_schemes", "loan"),
    "farmer": ("get_farmer_schemes", "farmer"),
    "kisan": ("get_farmer_schemes", "farmer"),
    "education": ("get_education_schemes", "education"),
    "student": ("get_education_schemes", "education"),
    "scheme": ("get_general_info", "scheme"),
    "yojana": ("get_general_info", "scheme"),
    "योजना": ("get_general_info", "scheme"),
    "health": ("get_health_schemes", "health"),
    "gas": ("get_gas_schemes", "gas"),
    "ujjwala": ("get_gas_schemes", "gas")
}

def extract_intent_entities(text: str):
    text = text.lower()
    found_intents = set()
    found_entities = []

    for keyword, (intent, entity) in intent_entity_map.items():
        if keyword in text:
            found_intents.add(intent)
            found_entities.append(entity)

    if not found_intents:
        return "get_general_info", []

    return list(found_intents)[0], list(set(found_entities))

def match_schemes(user_query, schemes):
    user_query = user_query.lower()
    matched = []
    for scheme in schemes:
        for keyword in scheme.get("keywords", []):
            if keyword.lower() in user_query:
                matched.append(scheme)
                break
    return matched
