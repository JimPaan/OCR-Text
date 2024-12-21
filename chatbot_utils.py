from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Initialize the Hugging Face model pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")


def generate_response(context, query, max_chunk_size=512):
    """
    This function takes a large context and a query, chunks the context for optimization,
    and returns the answer by querying a Hugging Face model.

    :param context: The large text context
    :param query: The question/query
    :param max_chunk_size: Maximum chunk size for context (in tokens)
    :return: The response from the model
    """

    # Step 1: Chunk the context to fit within the model's input size
    context_chunks = [context[i:i + max_chunk_size] for i in range(0, len(context), max_chunk_size)]

    # Step 2: Use TF-IDF to find the chunk most relevant to the query
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([query] + context_chunks)

    # Compute the similarity between the query and context chunks
    similarities = np.dot(tfidf_matrix[0], tfidf_matrix[1:].T).toarray().flatten()

    # Step 3: Get the chunk with the highest similarity to the query
    best_chunk_idx = np.argmax(similarities)
    best_chunk = context_chunks[best_chunk_idx]

    # Step 4: Query the model with the best chunk
    answer = qa_pipeline(question=query, context=best_chunk)

    return answer['answer']
