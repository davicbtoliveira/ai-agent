import os
import argparse
import sys
from prompts import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions, call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("API Key not found in .env")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true",
                        help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(
        role="user", parts=[types.Part(text=args.user_prompt)])]

    def response():
        return client.models.generate_content(model='gemini-2.5-flash', contents=messages, config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt))

    for _ in range(20):
        func = response()

        if func.usage_metadata is None:
            raise RuntimeError("Failed API request")

        if func.function_calls is None:
            print("Final response:")
            print(func.text)
            return

        if args.verbose is True:
            print("User prompt: " + args.user_prompt)
            print(f"Prompt tokens: {func.usage_metadata.prompt_token_count}\nResponse tokens: {
                  func.usage_metadata.candidates_token_count}")

        if func.candidates is not None:
            for candidate in func.candidates:
                messages.append(candidate.content)

        function_responses = []

        for function in func.function_calls:

            if args.verbose:
                print(f"Model requested tool: {function.name}")

            function_call_result = call_function(
                function, verbose=args.verbose)

            if function_call_result.parts[0].function_response is None:
                raise Exception

            if function_call_result.parts[0].function_response.response is None:
                raise Exception

            function_responses.append(function_call_result.parts[0])

            if args.verbose is True:
                print(
                    f"-> {function_call_result.parts[0].function_response.response}")

        messages.append(types.Content(role="user", parts=function_responses))


if __name__ == "__main__":
    main()
