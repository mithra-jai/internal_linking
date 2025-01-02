import anthropic
import requests
import json
import ast
import os
from dotenv import load_dotenv
from controller.claude_process import get_relevant_links



load_dotenv()


# Claude 3.5 API client setup
claude_api_key = os.getenv('CLAUDE_API_KEY')
claude_client = anthropic.Anthropic(api_key=claude_api_key)

# Google Search setup

google_api_key = os.getenv('GOOGLE_API_KEY')
google_se_id = os.getenv('GOOGLE_SE_ID')


# Function to get search results from Google Custom Search API
def get_google_search_results(domain: str, query: str) :
    try:
        results = []
        
        # Construct the search query by appending the site:domain filter
        search_query = f"{query} site:{domain} "
        
        print(search_query,"search")
        
        # First request to get the top 10 results
        url = os.getenv('GOOGLE_API_URL')
        params = {
            "key": google_api_key,
            "cx": google_se_id,
            "q": search_query,
            "num": 10  # First 10 results
        }

        response = requests.get(url, params=params)

        search_results = response.json()

        if "items" in search_results:
            for item in search_results["items"]:
                results.append({
                    "link": item["link"],
                    "title": item["title"],
                    "description": item.get("snippet", "No description available"),
                })
        

            # Second request to get the next 10 results (start at 11)
        params["start"] = 11
        response = requests.get(url, params=params)
        search_results = response.json()

        if "items" in search_results:
            for item in search_results["items"]:
                results.append({
                    "link": item["link"],
                    "title": item["title"],
                    "description": item.get("snippet", "No description available"),
                })
        response =   get_relevant_links(results, query)     
        return response
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"status_code":500,"error": "An unexpected error occurred while getting search results from google"}
        
# FastAPI route to handle search requests


