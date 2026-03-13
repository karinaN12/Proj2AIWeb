import os
from google import genai

MODEL_NAME = "gemini-3-flash-preview"


def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is not set.")
        return

    client = genai.Client(api_key=api_key)

    user_question = input("Ask a question: ").strip()
    if not user_question:
        print("No question entered.")
        return

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=user_question,
        )

        print("\nLLM Response:")
        print(response.text)

    except Exception as e:
        print(f"Error calling Gemini API: {e}")


if __name__ == "__main__":
    main()
