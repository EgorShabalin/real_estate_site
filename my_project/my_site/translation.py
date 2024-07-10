from googletrans import Translator
import re


def translate(text, lang):
    # translator = Translator()
    # translation = translator.translate(text, dest=lang)
    # return translation.text

    # Split the text into lines
    lines = text.split("\n")

    translator = Translator()
    translated_lines = []

    for line in lines:
        # Preserve empty lines and lines with only whitespace
        if not line.strip():
            translated_lines.append(line)
            continue

        # Extract leading whitespace
        leading_whitespace = re.match(r"\s*", line).group()

        # Extract content (non-whitespace)
        content = line.strip()

        # Translate content if it's not just punctuation or symbols
        if re.search(r"[a-zA-Zа-яА-Я]", content):
            translated_content = translator.translate(content, dest=lang).text
        else:
            translated_content = content

        # Reconstruct the line
        translated_line = leading_whitespace + translated_content
        translated_lines.append(translated_line)

    # Join the translated lines back together
    return "\n".join(translated_lines)
