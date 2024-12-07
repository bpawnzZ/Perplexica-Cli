# Perplexica CLI

## Note: You will need to modify the perplexica_simple.py and perplexica_search.py with values that match your setup.  Once you do that install as described below

## Description

Perplexica CLI provides command-line interfaces for interacting with the Perplexica Search API. It allows you to perform searches, list available models, and more.

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Steps to Install

1. **Clone the Repository**

   ```bash
   git clone https://github.com/bpawnzZ/Perplexica-Cli.git
   cd Perplexica-Cli
   ```

2. **Install the Package**

   ```bash
   pip install -e .
   ```

   This command installs the package in editable mode, ensuring that any changes you make to the source code are immediately reflected.

## Usage

### Commands

- **Simple Search**

  ```bash
  perplexica-simple -p "your search prompt"
  ```

  **Options:**
  - `-p, --prompt`: The search prompt (required).
  - `-s, --sources`: Show sources.
  - `-t, --timeout`: Timeout in seconds (default: 30).

- **Search**

  ```bash
  perplexica-search -p "your search prompt" -f webSearch -o speed
  ```

  **Options:**
  - `-p, --prompt`: The search prompt (required).
  - `-t, --timeout`: Timeout in seconds (default: 30).
  - `-f, --focus`: Focus mode for the search (default: webSearch).
  - `-o, --optimization`: Optimization mode (default: speed).
  - `--chat-provider`: Chat model provider.
  - `--chat-model`: Chat model name.
  - `--embedding-provider`: Embedding model provider.
  - `--embedding-model`: Embedding model name.
  - `-l, --list-models`: List available models and exit exit.

### Examples

1. **Perform a Search**

   ```bash
   perplexica-search -p "What is the capital of France?"
   ```

2. **List Available Models**

   ```bash
   perplexica-search -l
   ```

3. **Perform a Simple Search with Sources**

   ```bash
  (base) [~]$ perplexica-simple -p "give me a overview of sentiment regarding the crypto market" -s

Certainly! Here’s an overview of the sentiment regarding the crypto market:

- **Definition and Importance**: Crypto market sentiment refers to the overall attitude or emotion that investors and traders have toward the cryptocurrency market. It is a collective sentiment—either bullish or bearish—based on factors such as market trends, news events, and social media discussions. This sentiment is crucial because it can significantly influence market behavior and price movements [1][7].

- **Current Sentiment**: As of the latest data, the sentiment score for the cryptocurrency market is currently 100, indicating a strongly bullish sentiment. This suggests that the market is currently optimistic about the future of cryptocurrencies [11].

- **Sources of Sentiment Data**:
  - **Community Votes**: Platforms like CoinMarketCap measure community sentiment by tallying bullish and bearish votes from users. This provides a direct gauge of how retail investors feel about the market [2].
  - **Technical Indicators**: Tools and platforms use technical indicators such as moving averages and oscillators to estimate market sentiment. These indicators help in identifying trends and potential turning points [11].
  - **Sentiment Analysis Tools**: Services like StockGeist.ai provide real-time sentiment monitoring of hundreds of cryptocurrencies. By analyzing social media, news articles, and other data sources, these tools can predict price movements [10].

- **Factors Influencing Sentiment**:
  - **Market Trends**: The overall direction of the market, whether it is rising or falling, significantly impacts sentiment. For example, a prolonged bull run can boost investor confidence, while a bear market can lead to pessimism [1][4].
  - **News Events**: Major news events, such as regulatory changes, technological advancements, and macroeconomic factors, can sway market sentiment. Positive news can drive prices up, while negative news can cause prices to drop [1][5].
  - **Social Media and Forums**: Discussions on social media platforms and forums can amplify or dampen market sentiment. Positive or negative sentiment expressed by influential figures or large communities can have a significant impact [6][12].

- **Behavioral Indicators**:
  - **Profit-Taking Patterns**: Analyzing profit-taking behavior can help identify market tops. A decline in profit-taking is often a sign of market "greed" and can indicate that the market is overbought [4].
  - **Transaction Flows**: Experts use data such as the "age" of Bitcoins held at addresses to categorize traders and predict their behavior. For instance, long-term holders might be less likely to sell during price drops, while short-term traders might be more reactive [5].

- **Impact on Investment Decisions**:
  - **Tax Efficiency**: While sentiment is a powerful indicator, tax efficiency is also crucial for portfolio management. Crypto tax software can help investors maximize deductions and find tax-loss harvesting opportunities, ensuring they do not overpay or underpay their tax obligations [3].
  - **Predictive Power**: Understanding market sentiment can help investors make more informed decisions. For example, a positive sentiment can signal a good time to buy, while a negative sentiment might suggest a more cautious approach [13].

- **Challenges and Considerations**:
  - **Volatility**: The crypto market is known for its high volatility, which can make sentiment analysis more challenging. Rapid price movements can quickly shift sentiment from bullish to bearish or vice versa [8].
  - **Speculation**: The market is often driven by speculation, especially in the early stages of new projects. This can lead to significant price fluctuations that may not always align with fundamental value [9].

In summary, the current sentiment in the crypto market is bullish, driven by positive market trends, favorable news, and optimistic community sentiment. However, it is important to consider multiple factors and use a combination of tools to make well-informed investment decisions [1][7][11].

Sources:
- Crypto Market Sentiment Analysis Explained: https://academy.wirexapp.com/post/crypto-market-sentiment-guide
- Crypto Community Sentiment - CoinMarketCap: https://coinmarketcap.com/sentiment/
- How to Find & Analyze Crypto Market Sentiment - zenledger.io: https://zenledger.io/blog/what-is-crypto-market-sentiment/
- Understanding the Current Sentiment in the Crypto Market: https://insights.santiment.net/read/understanding-the-current-sentiment-in-the-crypto-market-8255
- Understanding Market Sentiment: How Crypto Sentiment Affects Prices: https://simpleswap.io/blog/how-crypto-sentiment-affects-prices
- Crypto Sentiment Analysis Guide - Bitsgap: https://bitsgap.com/blog/understanding-and-using-sentiment-analytics-in-crypto-trading
- What Is Crypto Market Sentiment? A Barometer for Investor ... - RoboFi: https://robofi.io/blog/what-is-crypto-market-sentiment/
- Crypto Market Sentiment: Get to Know The Impact! - Quant Matter: https://quantmatter.com/crypto-market-sentiment-get-to-know-the-impact/
- Understanding Crypto Market Trends - One Trading: https://onetrading.com/blogs/understanding-crypto-market-trends
- Crypto Market Sentiment Analysis: https://www.stockgeist.ai/crypto-sentiment-analysis/
- Bitcoin & Crypto Sentiment Today - CoinCodex: https://coincodex.com/sentiment/
- Sentiment Analysis in Crypto Trading: A Beginners' Guide: https://www.kucoin.com/learn/trading/sentiment-analysis-in-crypto-trading-a-beginners-guide
- Role of Sentiment Analysis in Crypto Trading: https://www.blockchain-council.org/blogs/sentiment-analysis-in-crypto-trading/
- Crypto Fear & Greed Index - Bitcoin Sentiment - Alternative.me: https://alternative.me/crypto/fear-and-greed-index/
- Not all words are equal: Sentiment and jumps in the ...: https://www.sciencedirect.com/science/article/pii/S1042443123001889
   ```

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
