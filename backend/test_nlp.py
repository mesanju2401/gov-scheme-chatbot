from nlp_utils import extract_intent_entities

queries = [
    "Tell me about loan schemes",
    "I want farmer related schemes",
    "Education support for students",
    "What schemes are available?"
]

for q in queries:
    intent, entities = extract_intent_entities(q)
    print(f"Query: {q}")
    print(f"Intent: {intent}")
    print(f"Entities: {entities}")
    print("-" * 20)
