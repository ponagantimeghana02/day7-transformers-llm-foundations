from transformers import AutoTokenizer

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Sample texts
short_sentence = "Artificial Intelligence is amazing."

long_paragraph = """
Artificial Intelligence is transforming industries worldwide.
Machine learning and deep learning models can analyze large
amounts of data, identify patterns, and make predictions.
Many companies use AI for automation, recommendation systems,
and natural language processing applications.
"""

programming_code = """
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
"""

texts = {
    "Short Sentence": short_sentence,
    "Long Paragraph": long_paragraph,
    "Programming Code": programming_code
}

print("=" * 60)
print("TOKENIZATION EXPERIMENT")
print("=" * 60)

for name, text in texts.items():
    print(f"\n{name}")
    print("-" * 60)

    # Tokenization
    tokens = tokenizer.tokenize(text)

    # Token IDs
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    # Decode back
    decoded_text = tokenizer.decode(token_ids)

    print("Original Text:")
    print(text)

    print("\nTokens:")
    print(tokens)

    print("\nToken IDs:")
    print(token_ids)

    print("\nDecoded Text:")
    print(decoded_text)

    print("\nToken Count:", len(tokens))

print("\nExperiment Completed Successfully!")