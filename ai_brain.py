import os
from google import genai

API_KEY = "AIzaSyCzJUyVAQkxYkc-z_WcqK-6tXy7NzBV4V0"

def main():
    if not API_KEY:
        print("Error: API key missing.")
        return

    client = genai.Client(api_key=API_KEY)

    question = input("Ask a question: ").strip()

    if not question:
        print("No question entered.")
        return

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=question
        )

        print("\nLLM Response:")
        print(response.text)

    except Exception as e:
        print("Error calling Gemini API:", e)


if __name__ == "__main__":
    main()
