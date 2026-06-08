from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL


# =========================================
# LOAD MODEL ONLY WHEN NEEDED
# =========================================

embedding_model = None


def get_embedding_model():

    global embedding_model

    if embedding_model is None:

        embedding_model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    return embedding_model


# =========================================
# GENERATE EMBEDDINGS
# =========================================

def generate_embeddings(chunks):

    model = get_embedding_model()

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True
    )

    return embeddings