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

    context_chunks = [context[i:i + max_chunk_size] for i in range(0, len(context), max_chunk_size)]

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([query] + context_chunks)

    similarities = np.dot(tfidf_matrix[0], tfidf_matrix[1:].T).toarray().flatten()

    best_chunk_idx = np.argmax(similarities)
    best_chunk = context_chunks[best_chunk_idx]

    answer = qa_pipeline(question=query, context=best_chunk)

    return answer['answer']
