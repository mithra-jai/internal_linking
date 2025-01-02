
from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from controller.web_results import get_google_search_results
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()


app = FastAPI()

# Define the query parameters model
class QueryRequest(BaseModel):
    query: str
    domain: str

origins = ["*"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Route to accept domain and query, then fetch links and process with Claude
@app.post("/search_web_links")

async def process_query(request: QueryRequest,api_key: str = Header(...), ):
    
    try:

        domain = request.domain
        query = request.query
        
        valid = check_api_key(api_key)
        
        if not valid:
            return {"status_code":403,"message":"The user is unauthorized"}

        # Perform Google search
        search_data = get_google_search_results(domain, query)

        return search_data
    
    except Exception as e:
        print(f"An error occurred while processing the request: {e}")
        return {"status_code":500,"error": "An error occurred while processing the request"}
        
           

def check_api_key(api_key):
    try:
        actual_api_key=os.getenv('API_KEY')
        if api_key and api_key!= actual_api_key:
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred while checking for API key: {e}")
        return {"status_code":500,"error": "An error occurred while checking for API key"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)    
            
        
    



