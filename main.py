import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("API key is not found")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
    print("Hello from bootdev-ai-agent!")

    #print("Ask the magic answers machine:")
    #args.prompt = input()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )

    if response.usage_metadata == None:
        raise RuntimeError("usage_metadata is empty, likely due to a failed API response")
    
    

    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    

    if not response.function_calls:
        print(response.text)
        return
    
    call_responses = []
    for call in response.function_calls:
        call_args = {"name" : call.name, **call.args}
        #print(f"Combined call_args: {call_args}")

        function_call_response = call_function(call_args, args.verbose)
        if not function_call_response.parts[0].function_response.response:
            raise Exception(f"Invalid function call response from: {call.name}")
        call_responses.append(function_call_response.parts[0])

        if args.verbose:
            print(f"-> {function_call_response.parts[0].function_response.response}")
        
        #print(f"Calling function: {call.name}({call.args})")



if __name__ == "__main__":
    main()
