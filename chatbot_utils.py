from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Initialize the Hugging Face model pipeline
qa_pipeline = pipeline("text-generation", model="gpt2")


def generate_response(context, query, max_chunk_size=150, max_length=150):
    """
    This function takes a large context and a query, chunks the context for optimization,
    and returns the answer by querying a Hugging Face model.

    :param max_length:
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

    input_text = f"Context: {best_chunk}\nQuestion: {query}\nAnswer:"
    output = qa_pipeline(input_text, max_length=max_length, num_return_sequences=1)
    response = output[0]['generated_text']
    answer = response.split("Answer:")[1].strip() if "Answer:" in response else response

    return answer
