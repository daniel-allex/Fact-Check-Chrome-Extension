import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
import spacy

nltk.download('punkt')


class SentenceTokenizer:
    def __init__(self):
        self.tokenizer = PunktSentenceTokenizer()
        self.nlp = spacy.load('en_core_web_sm')
        self.nlp.add_pipe('coreferee')

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
    
    def replace_references(self, context, sentence):
        # Concatenate the context and the sentence with a space
        text = context + " " + sentence

        doc = self.nlp(text)

        # Find out how many tokens are in the context. We'll use this to only return the main sentence later.
        context_tokens = len(self.nlp(context))

        resolved_text_list = list(token.text for token in doc)

        for token in doc:
            if token._.coref_chains:
                chain = token._.coref_chains[0] # Get the first coreference chain
                referent_idx = chain[0][0] # Get the index of the first mention in the chain
                referent = doc[referent_idx].text # Get the text of the referent
                resolved_text_list[token.i] = referent # Replace the pronoun with the referent

        # Return only the main sentence, skipping the number of tokens in the context
        return " ".join(resolved_text_list[context_tokens:])


