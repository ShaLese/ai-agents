import ollama

# Define each agent as a separate function
def english_to_french_agent(text):
    prompt = f"Translate the following English text to French: {text}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def english_to_spanish_agent(text):
    prompt = f"Translate the following English text to Spanish: {text}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def english_to_german_agent(text):
    prompt = f"Translate the following English text to German: {text}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()

def localization_agent(text, language):
    prompt = f"Adapt the following text for cultural relevance in {language}: {text}"
    response = ollama.generate(model="tinyllama", prompt=prompt)
    return response["response"].strip()



def translate_and_localize():
    text = input("Enter the text to translate and localize: ")
    
    # Translate to French
    french_translation = english_to_french_agent(text)
    print(f"\nFrench Translation:\n{french_translation}\n")

    # Localize for French
    french_localized = localization_agent(french_translation, "French")
    print(f"Localized for French:\n{french_localized}\n")

    # Translate to Spanish
    spanish_translation = english_to_spanish_agent(text)
    print(f"Spanish Translation:\n{spanish_translation}\n")

    # Localize for Spanish
    spanish_localized = localization_agent(spanish_translation, "Spanish")
    print(f"Localized for Spanish:\n{spanish_localized}\n")

    # Translate to German
    german_translation = english_to_german_agent(text)
    print(f"German Translation:\n{german_translation}\n")

    # Localize for German
    german_localized = localization_agent(german_translation, "German")
    print(f"Localized for German:\n{german_localized}\n")

# Start the translation and localization process
translate_and_localize()