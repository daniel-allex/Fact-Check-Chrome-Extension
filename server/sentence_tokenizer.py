import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer

nltk.download('punkt')

class SentenceTokenizer:
    def __init__(self):
        self.tokenizer = PunktSentenceTokenizer()

    def tokenize_paragraph(self, text):
        return self.tokenizer.tokenize(text)
    
    def tokenize_raw(self, text):
        paragraphs = text.split('\n')
        paragraphs_tokenized = [self.tokenize_paragraph(paragraph) for paragraph in paragraphs]
        
        sentences = []
        for paragraph in paragraphs_tokenized:
            for sentence in paragraph:
                sentences.append(sentence)

        return sentences
