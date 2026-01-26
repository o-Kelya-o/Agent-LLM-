import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None: 
        raise RuntimeError("API key wasn't found in .env.\nPlease set it up this way -> GEMINI_API_KEY='{your api key}'")
    
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chat Bot")
    parser.add_argument("user_prompt", type=str, help="The message the ai will read")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


    response = client.models.generate_content(model = "gemini-2.5-flash", contents = messages)
    metadata = response.usage_metadata

    if metadata == None:
        raise RuntimeError("The metadata if None, there's likely an issue with Google api... retry in a moment")
    

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")
        
    print(response.text)

if __name__ == "__main__":
    main()
