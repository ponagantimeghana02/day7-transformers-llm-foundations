# Tokenization Experiment Report

## Objective

The objective of this experiment is to understand how Hugging Face tokenizers convert text into tokens, map tokens to numerical IDs, and reconstruct text from those IDs.

---

## Tokenizer Used

Model:
`bert-base-uncased`

Tokenizer Type:
WordPiece Tokenizer

---

## Tasks Performed

1. Converted text into tokens.
2. Converted tokens into token IDs.
3. Decoded token IDs back into text.
4. Compared token counts for different input types.

---

## Input Types

### 1. Short Sentence

Text:

Artificial Intelligence is amazing.

Observation:

* Produced a small number of tokens.
* Most words remained intact.
* Easy for the model to process.

Example Tokens:

['artificial', 'intelligence', 'is', 'amazing', '.']

---

### 2. Long Paragraph

Observation:

* Generated significantly more tokens.
* Longer inputs require more memory and computation.
* Context is spread across many tokens.

Example:

A paragraph of 50 words may generate around 60–80 tokens depending on punctuation and word splitting.

---

### 3. Programming Code

Observation:

* Code is tokenized differently from natural language.
* Symbols such as parentheses, operators, commas, and colons become separate tokens.
* Variable names may be split into multiple subwords.

Example Tokens:

['def', 'add', '(', 'a', ',', 'b', ')', ':']

---

## Why Tokenization Is Important

Large Language Models cannot directly understand raw text.

Tokenization:

* Breaks text into smaller units.
* Converts words into numerical representations.
* Enables neural networks to process language efficiently.

---

## Comparison of Token Counts

| Input Type       | Expected Token Count                      |
| ---------------- | ----------------------------------------- |
| Short Sentence   | Low (5–10)                                |
| Long Paragraph   | Medium to High (50+)                      |
| Programming Code | Varies depending on symbols and variables |

---

## Conclusion

The experiment demonstrates that different types of input produce different tokenization patterns. Natural language generally results in meaningful word tokens, while programming code generates many additional symbol tokens. Understanding tokenization is important because token count directly affects model performance, memory usage, and processing cost.