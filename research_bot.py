import google.generativeai as genai

# Put your Gemini API key here
GEMINI_API_KEY = "AIzaSyCzJUyVAQkxYkc-z_WcqK-6tXy7NzBV4V0"

def main():

    if not GEMINI_API_KEY:
        print("Missing Gemini API key.")
        return

    genai.configure(api_key=GEMINI_API_KEY)

    user_question = input("Ask a research question: ").strip()

    if not user_question:
        print("No question entered.")
        return

    try:
        model = genai.GenerativeModel(
            "gemini-1.5-pro",
            tools="google_search_retrieval"
        )

        response = model.generate_content(user_question)

        print("\nResearch Bot Answer:\n")
        print(response.text)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
