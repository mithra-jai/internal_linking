import anthropic
import os
from dotenv import load_dotenv
load_dotenv()


def get_claude_llm_connection(prompt):
    try:
        # Claude 3.5 API client setup
        claude_api_key = os.getenv('CLAUDE_API_KEY')
        claude_model = os.getenv('CLAUDE_MODEL')
        claude_client = anthropic.Anthropic(api_key=claude_api_key)
        message = claude_client.messages.create(
        model=claude_model,
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}])   
        return message
        
        
    except Exception as e:
        print(f"An error occurred in connecting with claude: {e}")
        return {"status_code":500,"error": "An error occurred in Claude connection"}
        
        
        