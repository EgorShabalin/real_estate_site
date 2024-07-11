from googletrans import Translator
import re


def translate(text, lang):
    translator = Translator()
    try:
        # Split the text into segments based on newlines and tabs
        segments = re.split(r"(\n|\t)", text)
        translated_segments = []

        for segment in segments:
            if segment.strip():  # Only translate non-whitespace segments
                translation = translator.translate(segment, dest=lang)
                translated_segments.append(translation.text)
            else:
                translated_segments.append(segment)  # Preserve whitespace segments

        # Reassemble the translated text
        translated_text = "".join(translated_segments)
        return translated_text
    except Exception as e:
        return f"Error: {e}"
