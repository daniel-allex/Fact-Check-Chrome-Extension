from sentence_transformers import SentenceTransformer, util
import numpy as np

class sentenceEmbeddingTransformer:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def transformSentence(self, sentence):
        return self.model.encode(sentence, convert_to_tensor=True)
    
    def transformSentences(self, sentences):
        return np.array(self.model.encode(sentences))
    
    def compareSentences(self, embedding_1, embedding_2):
        return util.pytorch_cos_sim(embedding_1, embedding_2)