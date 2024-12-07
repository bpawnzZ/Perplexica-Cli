#!/usr/bin/env python3
import argparse
import json
import sys
import requests
from typing import Optional

def search(prompt: str, show_sources: bool = False, timeout: int = 30) -> None:
    """
    Send a search request to the Perplexica API and print the results
    """
    base_url = "http://100.71.229.63:3001/api"
    url = f"{base_url}/search"
    
    # Increase connection timeout and read timeout
    timeout = (10, 60)  # (connection timeout, read timeout)

    payload = {
        "query": prompt,
        "focusMode": "webSearch",
        "optimizationMode": "speed",
        "chatModel": {
            "provider": "custom_openai",
            "model": "qwen/qwen-2.5-72b-instruct",
            "customOpenAIKey": "your_api_key",
            "customOpenAIBaseURL": "http://your-custom-endpoint.com"
        },
        "embeddingModel": {
            "provider": "openai",
            "model": "text-embedding-3-small"
        },
        "history": []
    }

    try:
        response = requests.post(url, json=payload, timeout=timeout, headers={'Connection': 'close'})
        response.raise_for_status()
        
        result = response.json()
        
        # Print the main message
        print(result["message"])
        
        # Print the sources only if requested
        if show_sources and result.get("sources"):
            print("\nSources:")
            for source in result["sources"]:
                print(f"- {source['metadata']['title']}: {source['metadata']['url']}")
                
    except requests.RequestException as e:
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_data = e.response.json()
                print(f"Error: {error_data.get('message', str(e))}")
            except ValueError:
                print(f"Error: {str(e)}")
        else:
            print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Simple Perplexica Search CLI')
    parser.add_argument('-p', '--prompt', required=True, help='Search prompt')
    parser.add_argument('-s', '--sources', action='store_true', help='Show sources')
    parser.add_argument('-t', '--timeout', type=int, default=30, help='Timeout in seconds (default: 30)')
    
    args = parser.parse_args()

    try:
        search(
            prompt=args.prompt,
            show_sources=args.sources,
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
