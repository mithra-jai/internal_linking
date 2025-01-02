import ast
import anthropic
import os
from dotenv import load_dotenv

from services.constants import get_suitable_link_prompt
from services.llm import get_claude_llm_connection
load_dotenv()


# Claude 3.5 API client setup
claude_api_key = os.getenv('CLAUDE_API_KEY')
claude_client = anthropic.Anthropic(api_key=claude_api_key)


# Function to interact with Claude 3.5 Sonnet
def get_relevant_links(data: list, query: str):
    
    try:
    
        # Format the message with the link, description, and topic for Claude
        example_format = {"filtered_results": [{"link": "https://example.com/page1", "title": "Example Page 1", "description": "This is a description of Example Page 1."}, {"link": "https://example.com/page2", "title": "Example Page 2", "description": "This is a description of Example Page 2."}, {"link": "https://example.com/page3", "title": "Example Page 3", "description": "This is a description of Example Page 3."}]}

        prompt = get_suitable_link_prompt(query,data,example_format)
        
        message = get_claude_llm_connection(prompt)
        
              
        # Access the tokens using dot notation
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens

    
        message_content=message.content[0].text
        
        print("message_content",message_content)
        parsed_content = ast.literal_eval(message_content)

    # Access the filtered_results
        filtered_results = parsed_content.get("filtered_results", [])
        print(filtered_results,"filtered_results")
        
        # Assuming Claude returns the most relevant links
        return {"relevant_links":filtered_results,"status_code":200,"input_token":input_tokens,"output_token":output_tokens}
    except Exception as e:
        print(f"An error occurred in the Claude processing: {e}")
        return {"status_code":500,"error": "An error occurred in Claude response processing"}