from textblob import TextBlob

'''
text = TextBlob('she is a bad cook')
print(text.sentiment)
print(text.word_counts)
print("\n============================================================================\n")
text = TextBlob('she is a baad singer ')
print(text.sentiment)
print(text.word_counts)
text = text.correct()
print(text)
print(text.sentiment)
print("\n============================================================================\n")

text = TextBlob('I am a good teacher')
print(text.sentiment)
print("\n============================================================================\n")

text = TextBlob('covid pandemic is really horrifying')
print(text.sentiment)
print("\n============================================================================\n")

text = TextBlob('Kevin said - thank god its friday')
print(text.sentiment)
print(text.noun_phrases)
print("\n============================================================================\n")

text = TextBlob('this isn\'t ging to be graet jobb')
for word in text.words:
    print(word.spellcheck())
print("\n============================================================================\n")
'''

speech = """
Good evening everyone! My name is Aman Dwivedi. It’s a pleasure to be here today. I want to talk about the importance of innovation in technology.
Innovation is key to our future, and we all need to push ourselves to think creatively. It’s not always easy, but it’s necessary.
Let’s embrace the challenges ahead and make the future a better place for everyone.
"""

text = TextBlob(speech)

print(f"Sentiment of the speech: {text.sentiment}")
print(f"Word counts: {text.word_counts}")
print(f"Nouns: {text.noun_phrases}")

