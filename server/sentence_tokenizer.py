import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer

nltk.download('punkt')

class sentence_tokenizer:
    def __init__(self):
        self.tokenizer = PunktSentenceTokenizer()

    def tokenize_raw(self, text):
        return self.tokenizer.tokenize(text)
