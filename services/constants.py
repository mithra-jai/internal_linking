

def get_suitable_link_prompt(query,data,example_format):
    try:
        
        prompt = f"""You are an advanced AI system designed to filter and rank search results based on a given query. Your task is to analyze the query, evaluate the search results, and return all relevant and suitable links in a JSON format.

    Here is the search query you need to analyze:
    query - {query}

    Here are the search results you need to evaluate:
    search_results - {data}

    Instructions:
    1. Analyze the query intent:
    - Determine the query type (informational, navigational, transactional, etc.).
    - Identify the core subject, key requirements, and nuances of the query.

    2. Evaluate the search results:
    - Review each result's relevance to the query.
    - Consider factors such as content quality, source reliability, recency, and alignment with the query intent.
    - Exclude only those results that are completely irrelevant or untrustworthy. All other results should be included as they are likely relevant.
    - Do not exclude anything that is somewhat relevant.

    3. Filter and rank the results:
    - Include **every relevant link** in the results.
    - Exclude only those results that are **completely irrelevant** or **untrustworthy**. If a result has any relevance at all, include it.
    - Rank the links based on their relevance, reliability, and quality.

    4. Output a JSON object containing only the suitable links:
    - For each relevant link, include the URL, its title and description from the given data.
    - Do not include any analysis or explanation outside the JSON structure.
    - Ensure the JSON object is formatted as a single line with no line breaks or additional text.



    Output Format:
    Provide a JSON object with an array of relevant links. For example:

    {
    example_format
    }

    Important:
    - **Return all relevant links**. Only omit those that are completely irrelevant.
    - If a link is even slightly relevant, **do not exclude it**.
    - Do not include any text or explanation outside the JSON structure.
    """
        return prompt
        
        
    except Exception as e:
        print(f"An error occurred while returning prompt: {e}")
        return {"status_code":500,"error": "An error occurred while returning prompt"}
        
           