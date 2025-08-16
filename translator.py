from googletrans import Translator

def main():
    translator = Translator()
    print("🌍 Simple Language Translator")
    print("Type text → choose target language → get instant translation.\n")

    while True:
        text = input("Enter text (or type 'exit' to quit): ")
        if text.lower() == "exit":
            print("Goodbye 👋")
            break

        target_lang = input("Translate to (ex: 'en' for English, 'bn' for Bangla, 'fr' for French): ")
        try:
            translated = translator.translate(text, dest=target_lang)
            print(f"Translation → {translated.text}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    main()
