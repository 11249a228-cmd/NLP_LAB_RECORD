import re
from collections import Counter, defaultdict
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    sentence = sentence.lower()
    return ["<s>"] + re.findall(r"[a-z']+", sentence) + ["</s>"]
sentences = [tokenize(s) for s in corpus.strip().split("\n")]
unigram_counts = Counter()
bigram_counts = Counter()
vocab = set()
for sent in sentences:
    unigram_counts.update(sent[:-1])
    vocab.update(sent)
    for i in range(len(sent) - 1):
        bigram_counts[(sent[i], sent[i + 1])] += 1
V = len(vocab)
# Create probability matrix
prob_matrix = defaultdict(dict)
words = ["the", "quick", "brown", "fox", "dog"]
for w1 in words:
    for w2 in words:
        prob_matrix[w1][w2] = (
            bigram_counts[(w1, w2)] + 1
        ) / (unigram_counts[w1] + V)
# Print small probability matrix
print("\nBIGRAM PROBABILITY MATRIX")
print("-" * 50)
print(f"{'Word':<10}", end="")
for word in words:
    print(f"{word:<8}", end="")
print()
for w1 in words:
    print(f"{w1:<10}", end="")

    for w2 in words:
        print(f"{prob_matrix[w1][w2]:<8.3f}", end="")
    print()