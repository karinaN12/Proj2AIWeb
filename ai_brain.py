import google.generativeai as genai

API_KEY = ""

def main():
    if not API_KEY:
        print("Error: API key missing.")
        return

    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel("gemini-pro")

    user_question = input("Ask a question: ").strip()
    if not user_question:
        print("No question entered.")
        return

    try:
        response = model.generate_content(user_question)

        print("\nLLM Response:")
        print(response.text)

    except Exception as e:
        print(f"Error calling Gemini API: {e}")


if __name__ == "__main__":
    main()
