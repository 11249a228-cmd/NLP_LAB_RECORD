import re
from collections import Counter
corpus = """
Natural language processing is a field of artificial intelligence.
It helps computers understand human language.
Language models are used in many natural language processing applications.
They can predict words and generate text.
N gram models are simple language models that use word sequences.
Unigram models use one word, bigram models use two words,
and trigram models use three words.
"""
def tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)
tokens = tokenize(corpus)
# Unigram
unigram_counts = Counter(tokens)
# Bigram
bigram_counts = Counter()
for i in range(len(tokens) - 1):
    bigram_counts[(tokens[i], tokens[i + 1])] += 1
# Trigram
trigram_counts = Counter()
for i in range(len(tokens) - 2):
    trigram_counts[
        (tokens[i], tokens[i + 1], tokens[i + 2])
    ] += 1
print("LARGER CORPUS N-GRAM MODEL")
print("-" * 40)
print("\nTotal Tokens:", len(tokens))
print("\nTop 10 Unigrams:")
for word, count in unigram_counts.most_common(10):
    print(f"{word:<15} {count}")
print("\nTop 10 Bigrams:")
for bigram, count in bigram_counts.most_common(10):
    print(f"{bigram!s:<35} {count}")
print("\nTop 10 Trigrams:")
for trigram, count in trigram_counts.most_common(10):
    print(f"{trigram!s:<45} {count}")