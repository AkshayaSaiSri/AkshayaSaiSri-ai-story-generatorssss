from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

def generate_story(prompt):
    output = generator(prompt, max_length=150, num_return_sequences=1)
    return output[0]['generated_text']

