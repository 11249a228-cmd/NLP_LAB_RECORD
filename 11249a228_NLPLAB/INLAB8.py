import re
from collections import Counter
import matplotlib.pyplot as plt
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z']+", text)
tokens = tokenize(corpus)
# Count unigrams
unigram_counts = Counter(tokens)
# Get top 10 unigrams
top10 = unigram_counts.most_common(10)
words = [item[0] for item in top10]
counts = [item[1] for item in top10]
# Create bar chart
plt.figure(figsize=(10, 5))
plt.bar(words, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Unigram Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()