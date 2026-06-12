from transformers import pipeline

print("=" * 60)
print("HUGGING FACE MODEL EXPLORATION")
print("=" * 60)

print("\n1. TEXT CLASSIFICATION")
print("-" * 40)

classification_model = "distilbert-base-uncased-finetuned-sst-2-english"

classifier = pipeline(
    "text-classification",
    model=classification_model
)

text = "I love learning Artificial Intelligence."

result = classifier(text)

print("Model Name:", classification_model)
print("Input:", text)
print("Output:", result[0]["label"])
print("Confidence Score:", round(result[0]["score"], 4))

print("\n2. NAMED ENTITY RECOGNITION (NER)")
print("-" * 40)

ner_model = "dbmdz/bert-large-cased-finetuned-conll03-english"

ner = pipeline(
    "ner",
    model=ner_model,
    aggregation_strategy="simple"
)

sentence = "Elon Musk founded SpaceX in California."

entities = ner(sentence)

print("Model Name:", ner_model)
print("Input:", sentence)

print("\nDetected Entities:")
for entity in entities:
    print(
        f"Entity: {entity['word']}, "
        f"Type: {entity['entity_group']}, "
        f"Confidence: {entity['score']:.4f}"
    )

print("\n3. TEXT GENERATION")
print("-" * 40)

generation_model = "gpt2"

generator = pipeline(
    "text-generation",
    model=generation_model
)

prompt = "The future of AI is"

generated_text = generator(
    prompt,
    max_length=50,
    num_return_sequences=1
)

print("Model Name:", generation_model)
print("Input:", prompt)
print("Output:")
print(generated_text[0]["generated_text"])

print("\nDone!")