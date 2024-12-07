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
   perplexica-simple -p "What is the capital of France?" -s
   ```

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
