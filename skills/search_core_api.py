import requests
import json
import os
import hashlib

# Replace with your CORE API key from https://core.ac.uk/services/api
CORE_API_KEY = "CORE_API_KEY"

# Set the base URL for the CORE API
api_endpoint = "https://api.core.ac.uk/v3/"

def find_papers_core(query, max_results=10):
    """
    Searches the CORE API for the given query. Instead of returning the search results,
    it prints the abstract, DOI, and URLs for each result.

    Args:
        query (str): The search query.
        max_results (int, optional): The maximum number of search results to process. Defaults to 10.
    
    Example:
        >>> query_core_api("COVID AND yearPublished>=2010 AND yearPublished<=2021")
        # This will print the abstract, DOI, and URL for each of the top results based on the query.
    """

    # Generate a unique cache key based on the query and max_results
    key = hashlib.md5(("query_core_api(" + str(max_results) + ")" + query).encode("utf-8")).hexdigest()

    # Prepare the header with the authorization token
    headers = {"Authorization": f"Bearer {CORE_API_KEY}"}

    # Construct the query payload and make the POST request to the CORE API
    payload = {"q": query, "limit": max_results}
    response = requests.post(f"{api_endpoint}search/works", data=json.dumps(payload), headers=headers)

    # Check for a successful response
    if response.status_code == 200:
        results = response.json()["results"]
        # Print the required details for each result
        for result in results:
            print(f"Abstract: {result['abstract']}")
            print(f"DOI: {result['doi']}")
            print(f"URL: {result.get('sourceFulltextUrls', 'No URL available')}")
    else:
        print(f"Error code {response.status_code}, {response.content}")
        
        
#Helper function

def pretty_json(json_object):
    """
    Utility function to print JSON objects in a formatted manner.
    Args:
        json_object (dict): The JSON object to format and print.
    """
    print(json.dumps(json_object, indent=2))