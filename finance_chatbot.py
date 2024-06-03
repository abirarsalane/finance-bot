# -*- coding: utf-8 -*-
"""Finance Chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/172S0hvui9lwYRbn0A8RocZ-LSNSZFF7r
"""

pip install transformers yfinance

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import yfinance as yf

# Load the model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Custom responses for finance-related queries
finance_responses = {
    "finance": "Finance involves managing money, including investments, budgeting, banking, and loans.",
    "stock market": "The stock market is where shares of publicly traded companies are bought and sold.",
    "investment": "Investment involves putting money into assets like stocks, bonds, or real estate to earn a return.",
    "cryptocurrency": "Cryptocurrency is a digital or virtual currency that uses cryptography for security."
}

def generate_response(prompt, history=None):
    if history is None:
        history = []

    # Encode the new user input and add the eos_token
    new_user_input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')

    # Concatenate the new user input with the chat history
    bot_input_ids = torch.cat([history, new_user_input_ids], dim=-1) if len(history) > 0 else new_user_input_ids

    # Generate a response
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Convert the tokens to text
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    # Update the history
    history = chat_history_ids

    return response, history

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    if hist.empty:
        return None
    price = hist['Close'].iloc[-1]
    return price

def handle_finance_query(query):
    tokens = query.lower().split()
    for token in tokens:
        if token in finance_responses:
            return finance_responses[token]
        elif token.upper().isalpha() and len(token) <= 5:  # Tickers are usually alphabetic and 1-5 characters long
            if is_valid_ticker(token.upper()):
                price = get_stock_price(token.upper())
                if price is not None:
                    return f"The current price of {token.upper()} is ${price:.2f}."
                else:
                    return f"Could not retrieve the price for {token.upper()}. It might be an invalid ticker or there is no data available."
    return "I'm not sure about that stock or finance topic. Please check the ticker symbol or clarify your question."

def is_valid_ticker(ticker):
    try:
        yf.Ticker(ticker).info
        return True
    except:
        return False

history = None

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit"]:
        print("Bot: Goodbye! Have a great day!")
        break
    if any(keyword in user_input.lower() for keyword in ["price of", "finance", "stock", "investment", "cryptocurrency"]):
        finance_response = handle_finance_query(user_input)
        print(f'Bot: {finance_response}')
    else:
        response, history = generate_response(user_input, history)
        print(f'Bot: {response}')

