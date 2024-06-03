# Finance-Chatbot

This project is an interactive chatbot designed to answer general questions and provide information on finance-related topics, including stock prices. The chatbot utilizes Hugging Face's DialoGPT for conversational abilities and Yahoo Finance (yfinance) for real-time stock data.

## Features

- Responds to general conversational prompts
- Provides explanations of finance-related terms
- Retrieves current stock prices for valid ticker symbols

## Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/abirarsalane/finance-bot.git
    cd finance-bot
    ```

2. Install the required libraries:

    ```sh
    pip install -r requirements.txt
    ```

### Required Libraries

- transformers
- yfinance

You can install the required libraries using the following command:

```sh
pip install transformers yfinance
```

## Usage

To start the chatbot, simply run the script:

```sh
python finance-chatbot.py
```

### Example Interaction

```
You: hello
Bot: Hello! :D
You: explain finance to me
Bot: Finance involves managing money, including investments, budgeting, banking, and loans.
You: what is the stock market
Bot: The stock market is where shares of publicly traded companies are bought and sold.
You: tell me about cryptocurrency
Bot: Cryptocurrency is a digital or virtual currency that uses cryptography for security.
You: price of AAPL
Bot: The current price of AAPL is $X.XX.
```

### How It Works

1. **General Responses**: For general conversation, the chatbot uses the DialoGPT model from Hugging Face.
2. **Finance Queries**: For finance-related questions, the chatbot provides predefined responses or fetches real-time stock data using Yahoo Finance.

### Custom Responses

The chatbot includes predefined responses for common finance terms. These can be found in the `finance_responses` dictionary in `finance-chatbot.py`. You can easily add or modify these responses to suit your needs.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the coding guidelines and document your code.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or suggestions, feel free to contact [Abir Arsalane](mailto:abir.arsalane@outlook.com).

---

### Acknowledgements

- [Hugging Face](https://huggingface.co/) for providing the DialoGPT model
- [Yahoo Finance](https://finance.yahoo.com/) for real-time stock data

## File Structure

- `finance-chatbot.py`: Main script for the chatbot
- `requirements.txt`: List of dependencies
