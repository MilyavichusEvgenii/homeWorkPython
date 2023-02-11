from deep_translator import GoogleTranslator

def TranslateLang(text):
    marker = 0
    for i in text.lower():
        if ord(i) >= 97 and ord(i) <= 122:
            marker = 1

    if marker == 1:
        translated = GoogleTranslator(source='en', target='ru').translate(text=text)
        return translated
    else:
        translated = GoogleTranslator(source='ru', target='en').translate(text=text)
        return translated
