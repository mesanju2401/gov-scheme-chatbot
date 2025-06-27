from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect

# Mapping from language code to MarianMT model name
model_name_map = {
    'hi': 'Helsinki-NLP/opus-mt-hi-en',
    # 'ta': 'Helsinki-NLP/opus-mt-ta-en',  # Add back if access becomes available
    # Add more Indian languages as needed
}

# Cache for loaded models and tokenizers
translation_models = {}

def detect_language(text: str) -> str:
    try:
        return detect(text)
    except Exception:
        return "en"  # fallback if detection fails

def translate_to_english(text: str, src_lang: str) -> str:
    if src_lang == 'en' or src_lang not in model_name_map:
        return text  # No translation needed or unsupported language

    if src_lang not in translation_models:
        model_name = model_name_map[src_lang]
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        translation_models[src_lang] = (tokenizer, model)

    tokenizer, model = translation_models[src_lang]
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated_tokens = model.generate(**inputs)
    return tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

def extract_intent_entities(text):
    text = text.lower()
    if "loan" in text:
        return "get_loan_schemes", ["loan"]
    elif "farmer" in text or "kisan" in text:
        return "get_farmer_schemes", ["farmer"]
    elif "education" in text or "student" in text:
        return "get_education_schemes", ["education"]
    elif "scheme" in text or "योजना" in text:
        return "get_general_info", ["scheme"]
    else:
        return "get_general_info", []
