from sentence_transformers import SentenceTransformer, util
import numpy as np

class sentenceEmbeddingTransformer:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def transformSentence(self, sentence):
        return self.model.encode(sentence, convert_to_tensor=True)
    
    def transformSentences(self, sentences):
        return np.array(list(map(self.transformSentence, sentences)))