#pip install googletrans
#pip install langdetect

from googletrans import Translator
from langdetect import detect
# init
translator = Translator()
while (1):
# Get user input
    try: 
        text_to_translate = input("input text: ")
    except KeyboardInterrupt:
        print(end = '\r')
        exit(1)    
# auto detect language
    try:
        detected_lang = detect(text_to_translate)
        if detected_lang in ['zh-cn','zh-tw','ja','ko']:
            detected_lang = 'zh-cn'
        else: detected_lang = 'en'    
    except Exception as e:
        print(f"fail to detect: {str(e)}")
        exit()
# confirm target language
    if detected_lang == 'zh-cn':
        dest_lang = 'en'
    else:
        dest_lang = 'zh-cn'
# running
    try:
        translated = translator.translate(text_to_translate, src=detected_lang, dest=dest_lang)
        print(f"source language: {detected_lang}")
        print(f"target language: {dest_lang}")
        print(f"\nraw: {text_to_translate}")
        print(f"translation: {translated.text}\n")
    except Exception as e:
        print(f"fail to translate: {str(e)}")