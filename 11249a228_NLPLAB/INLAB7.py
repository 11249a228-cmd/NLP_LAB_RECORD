import re
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z']+", text)
# Training vocabulary
training_words = set(tokenize(corpus))
# Test sentence
test_sentence = "the fox runs quickly"
test_words = tokenize(test_sentence)
# Find OOV words
oov_words = [word for word in test_words if word not in training_words]
# Calculate OOV rate
oov_rate = len(oov_words) / len(test_words) * 100
print("OOV RATE")
print("-" * 30)
print("Test sentence:", test_sentence)
print("Total test words:", len(test_words))
print("OOV words:", oov_words)
print("Number of OOV words:", len(oov_words))
print(f"OOV Rate: {oov_rate:.2f}%")