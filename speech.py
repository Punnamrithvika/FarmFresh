import pyttsx3
import speech_recognition as sr
from googletrans import Translator

# Initialize Text-to-Speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to convert speech to text in any language
def speech_to_text(language_code="en-US"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening. Please start speaking.")
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            # Recognize speech in the specified language
            text = recognizer.recognize_google(audio, language=language_code)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said. Could you please repeat?")
            return None
        except sr.RequestError:
            speak("There was an issue with the speech recognition service.")
            return None
        except Exception as e:
            speak("An error occurred.")
            print(f"Error: {e}")
            return None

# Function to translate text to English
def translate_to_english(text, source_language="auto"):
    translator = Translator()
    try:
        translation = translator.translate(text, src=source_language, dest="en")
        return translation.text
    except Exception as e:
        speak("An error occurred while translating.")
        print(f"Translation Error: {e}")
        return None

# Main function
def main():
    speak("Welcome to the multi-language translator. Please specify the language you will speak.")
    speak("For example, say 'Spanish', 'French', or 'Hindi'.")
    
    # Language selection
    language_selection = speech_to_text("en-US")  # Default language is English
    language_code = "en-US"  # Default language code

    # Map language names to Google API language codes
    language_map = {
        "english": "en-US",
        "spanish": "es-ES",
        "french": "fr-FR",
        "german": "de-DE",
        "hindi": "hi-IN",
        "japanese": "ja-JP",
        "chinese": "zh-CN",
        "arabic": "ar-SA",
        "korean": "ko-KR",
        "italian": "it-IT",
        "telugu": "te-IN",
    }

    if language_selection:
        for key, value in language_map.items():
            if key in language_selection.lower():
                language_code = value
                speak(f"You selected {key}.")
                break
        else:
            speak("I did not recognize the language. Defaulting to English.")

    # Perform speech-to-text in the selected language
    speak("Please start speaking in your selected language.")
    recognized_text = speech_to_text(language_code)
    if recognized_text:
        print(f"Recognized Text: {recognized_text}")

        # Translate recognized text to English
        translated_text = translate_to_english(recognized_text, source_language=language_code[:2])
        if translated_text:
            print(f"Translated Text (to English): {translated_text}")
            speak(f"The translation is: {translated_text}")
    else:
        speak("No speech was recognized.")

if __name__ == "__main__":
    main()