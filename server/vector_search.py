from annoy import AnnoyIndex
import numpy as np
import os

class VectorSearcher:
    def __init__(self, dimensionality, num_trees, file_name, database):
        self.dimensionality = dimensionality
        self.num_trees = num_trees
        self.file_name = file_name
        self.database = database
        self.build_index()

    def build_index(self):
        self.index = AnnoyIndex(self.dimensionality, 'euclidean')
        if os.path.exists(self.file_name):
            # Load the index file if it exists
            self.index.load(self.file_name)
        else:
            vector_data = {}
            for row in self.database.get_all():
                vector_data[row['Index']] = row['Embedding'] 

            # Store the vectors in the index
            for i, (id, vector) in enumerate(vector_data.items()):
                self.index.add_item(id, vector)

            # Build the index!
            self.index.build(self.num_trees)
            self.index.save(self.file_name)

    def search_vector(self, embedding_vector, k):
        return self.index.get_nns_by_vector(embedding_vector, k, include_distances=True)
