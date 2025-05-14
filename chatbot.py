from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer

# Sentiment analysis pipeline (for detecting emotions)
sentiment_pipeline = pipeline("sentiment-analysis")

# Load GPT-2 model for chatbot replies
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Function to detect sentiment (positive/negative)
def get_sentiment(text):
    result = sentiment_pipeline(text)
    return result[0]['label']

# Function to generate chatbot reply using GPT-2 model
def generate_chatbot_reply(user_input):
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    reply_ids = model.generate(inputs, max_length=150, num_return_sequences=1)
    reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return reply
