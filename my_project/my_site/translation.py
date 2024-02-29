from googletrans import Translator


def translate(text, lang):
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    return translation.text
