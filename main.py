import os
import argparse
import sys
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
    for _ in range(20):
        smth = False
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
        
        for candidates in (response.candidates or []):
            messages.append(candidates.content)
        
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {metadata.prompt_token_count}")
            print(f"Response tokens: {metadata.candidates_token_count}")

        function_calls = response.function_calls or []

        if not function_calls:
            if response.text:
                print(response.text)
            return

        function_result = []
        for item in response.function_calls :
            function_call_result = call_function(item)
            part0 = function_call_result.parts[0]

            function_response = part0.function_response

            if function_response == None:
                raise Exception("Function call returned an invalid function_response")
            
            if "result" in function_response.response:
                print(function_response.response["result"])

            if args.verbose: 
                print(f"Verbose: -> {function_response.response}")

            function_result.append(part0)

            
            messages.append(types.Content(role="user", parts=function_result))

    print("The ai couldn't answer your prompt, try again...")
    sys.exit(1)
    

if __name__ == "__main__":
    main()
