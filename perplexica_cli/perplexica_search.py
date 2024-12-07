#!/usr/bin/env python3
import argparse
import json
import sys
import requests
from typing import Optional, Dict, List, Tuple

def get_available_models() -> Tuple[Dict, Dict]:
    """Get available chat and embedding models from the API"""
    chat_models = {
        "custom_openai": {
            "qwen/qwen-2.5-72b-instruct": {
                "provider": "custom_openai",
                "model": "qwen/qwen-2.5-72b-instruct",
                "customOpenAIKey": "your_api_key",
                "customOpenAIBaseURL": "http://your-custom-endpoint.com"
            }
        }
    }
    embedding_models = {
        "openai": {
            "text-embedding-3-small": {
                "provider": "openai",
                "model": "text-embedding-3-small",
                "api_key": "your_api_key"
            }
        }
    }
    return chat_models, embedding_models

def search(
    prompt: str,
    focus_mode: str = "webSearch",
    optimization_mode: str = "speed",
    chat_provider: Optional[str] = None,
    chat_model: Optional[str] = None,
    embedding_provider: Optional[str] = None,
    embedding_model: Optional[str] = None,
    timeout: int = 30
) -> None:
    """
    Send a search request to the Perplexica API and print the results
    """
    base_url = "http://100.71.229.63:3001/api"
    url = f"{base_url}/search"
    
    # Increase connection timeout and read timeout
    timeout = (10, 60)  # (connection timeout, read timeout)

    payload = {
        "query": prompt,
        "focusMode": focus_mode,
        "optimizationMode": optimization_mode,
        "chatModel": {
            "provider": "custom_openai",
            "model": "qwen/qwen-2.5-72b-instruct",
            "customOpenAIKey": "sk-FiIu6b1Hyq7TDX-C9phogQ",
            "customOpenAIBaseURL": "https://litellm.2damoon.xyz"
        },
        "embeddingModel": {
            "provider": "openai",
            "model": "text-embedding-3-small"
        },
        "history": []
    }

    print("Sending payload:", json.dumps(payload, indent=2, ensure_ascii=False))  # Debug print

    try:
        response = requests.post(url, json=payload, timeout=timeout, headers={'Connection': 'close'})
        print("Response status:", response.status_code)  # Debug print
        print("Response headers:", dict(response.headers))  # Debug print
        
        response.raise_for_status()
        
        result = response.json()
        print("Response body:", json.dumps(result, indent=2, ensure_ascii=False))  # Debug print
        
        # Print the main message
        print("\nResult:")
        print(result["message"])
        
        # Print the sources
        if result.get("sources"):
            print("\nSources:")
            for source in result["sources"]:
                print(f"- {source['metadata']['title']}: {source['metadata']['url']}")
                
    except requests.RequestException as e:
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_data = e.response.json()
                print("Error response:", json.dumps(error_data, indent=2, ensure_ascii=False))  # Debug print
                print(f"Error: {error_data.get('message', str(e))}")
            except ValueError:
                print(f"Error: {str(e)}")
        else:
            print(f"Error: {str(e)}")

def list_models() -> None:
    """List all available models"""
    chat_models, embedding_models = get_available_models()
    
    print("Available Chat Models:")
    for provider, models in chat_models.items():
        print(f"\n{provider}:")
        for model_key, model_info in models.items():
            print(f"  - {model_key}")
    
    print("\nAvailable Embedding Models:")
    for provider, models in embedding_models.items():
        print(f"\n{provider}:")
        for model_key, model_info in models.items():
            print(f"  - {model_key}")

def main():
    parser = argparse.ArgumentParser(description='Perplexica Search CLI')
    parser.add_argument('-p', '--prompt', help='Search prompt')
    parser.add_argument('-t', '--timeout', type=int, default=30, help='Timeout in seconds (default: 30)')
    parser.add_argument('-f', '--focus', default='webSearch', 
                      choices=['webSearch', 'academicSearch', 'writingAssistant', 
                              'wolframAlphaSearch', 'youtubeSearch', 'redditSearch'],
                      help='Focus mode for the search (default: webSearch)')
    parser.add_argument('-o', '--optimization', default='speed',
                      choices=['speed', 'balanced'],
                      help='Optimization mode (default: speed)')
    parser.add_argument('--chat-provider', help='Chat model provider')
    parser.add_argument('--chat-model', help='Chat model name')
    parser.add_argument('--embedding-provider', help='Embedding model provider')
    parser.add_argument('--embedding-model', help='Embedding model name')
    parser.add_argument('-l', '--list-models', action='store_true',
                      help='List available models and exit')
    
    args = parser.parse_args()

    try:
        if args.list_models:
            list_models()
            return

        if not args.prompt:
            parser.error("the following arguments are required: -p/--prompt")
            
        search(
            prompt=args.prompt,
            focus_mode=args.focus,
            optimization_mode=args.optimization,
            chat_provider=args.chat_provider,
            chat_model=args.chat_model,
            embedding_provider=args.embedding_provider,
            embedding_model=args.embedding_model,
            timeout=args.timeout
        )
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
