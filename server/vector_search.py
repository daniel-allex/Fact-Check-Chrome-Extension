from annoy import AnnoyIndex
import numpy as np
import os

class VectorSearcher:
    def __init__(self, dimensionality, num_trees, file_name, vector_data):
        self.dimensionality = dimensionality
        self.num_trees = num_trees
        self.file_name = file_name
        self.vector_data = vector_data
        self.build_index()

    def build_index(self):
        if os.path.exists(self.file_name):
            # Load the index file if it exists
            self.index = AnnoyIndex(self.dimensionality, 'euclidean')
            self.index.load(self.file_name)
        else:
            # Create and save the index file if it does not exist
            self.index = AnnoyIndex(self.file_name, 'euclidean')

            # Store the vectors in the index
            for i, (id, vector) in enumerate(self.vector_data.items()):
                self.index.add_item(i, vector)

            # Build the index!
            self.index.build(self.num_trees)
            self.index.save(self.file_name)

    def search_vector(self, embedding_vector, k):
        return self.index.get_nns_by_vector(embedding_vector, k)
