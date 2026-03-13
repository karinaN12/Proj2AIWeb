import google.generativeai as genai

# Put your Gemini API key here
GEMINI_API_KEY = ""

def print_header():
    print("=" * 60)
    print("SMART RESEARCH BOT")
    print("=" * 60)
    print("Ask a question and the bot will generate a concise answer.")
    print("Type 'exit' to quit.")
    print()


def print_separator():
    print("-" * 60)


def main():
    if not GEMINI_API_KEY:
        print("Error: Missing Gemini API key.")
        return

    genai.configure(api_key=GEMINI_API_KEY)

    try:
        model = genai.GenerativeModel(
            MODEL_NAME,
            tools="google_search_retrieval"
        )
    except Exception as e:
        print(f"Error initializing Gemini model: {e}")
        return

    print_header()

    while True:
        user_question = input("Enter your research question: ").strip()

        if not user_question:
            print("Please enter a question.\n")
            continue

        if user_question.lower() == "exit":
            print("\nGoodbye.")
            break

        print()
        print_separator()
        print("Searching and generating answer...")
        print_separator()

        try:
            response = model.generate_content(user_question)

            print("\nANSWER:")
            print(response.text)
            print()
            print_separator()
            print()

        except Exception as e:
            print(f"\nError: {e}")
            print_separator()
            print()


if __name__ == "__main__":
    main()
