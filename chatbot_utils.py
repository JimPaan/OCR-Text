import torch
from transformers import pipeline


def load_model():
    model_id = "meta-llama/Llama-3.2-1B"
    return pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )


# Generate response using the model
def generate_response(user_query, context):
    model = load_model()
    max_context_tokens = 400
    truncated_context = context[:max_context_tokens]
    input_text = f"Context: {truncated_context}\nQuestion: {user_query}\nAnswer:"

    response = model(input_text, max_new_tokens=150, num_return_sequences=1)
    return response[0]["generated_text"].split("Answer:")[-1].strip()

