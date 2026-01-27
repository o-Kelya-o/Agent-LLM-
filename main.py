import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from modules.prompts import system_prompt
from modules.call_function import available_functions, call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    model_name = "gemini-2.5-flash"

    if api_key == None: 
        raise RuntimeError("API key wasn't found in .env.\nPlease set it up this way -> GEMINI_API_KEY='{your api key}'")
    
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chat Bot")
    parser.add_argument("user_prompt", type=str, help="The message the ai will read")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt,
            )
    )
    metadata = response.usage_metadata

    if metadata == None:
        raise RuntimeError("The metadata if None, there's likely an issue with Google api... retry in a moment")
    
    function_result = []
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")
        
    for item in response.function_calls :
        function_call_result = call_function(item)
        if function_call_result.parts[0].function_response == None:
            raise Exception("Function call .function_response returned None")
        if function_call_result.parts[0].function_response.response == None:
            raise Exception("Function call .function_response.response returned None")
        print(function_call_result.parts[0].function_response.response["result"])
        function_result.append(function_call_result.parts[0])
        if args.verbose: 
            print(f"Verbose: -> {function_call_result.parts[0].function_response.response}")


if __name__ == "__main__":
    main()
