import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))

# example_sent = "This is a sample sentence, showing off the stop words filtration."

example_sent = "Natural Language Processing enables computers to understand human language."

word_tokens = word_tokenize(example_sent)
print(f"Original: {word_tokens}")

filtered_sent = [w for w in word_tokens if not w in stop_words]
print("Filtered sentence - Approach 1: ", filtered_sent)

filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
        
print("Filtered sentence - Approach 2: ", filtered_sentence)