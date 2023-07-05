'''Module for Translating English to French & French to English using MyMemoryTranslator'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''Translates English text to French'''
    english_translator = MyMemoryTranslator(source="en-US", target="fr-FR").translate(english_text)
    return english_translator

def french_to_english(french_text):
    '''Translates French text to English'''
    french_translator = MyMemoryTranslator(source="fr-FR", target="en-US").translate(french_text)
    return french_translator

french_translation = english_to_french(input('English: '))
print('French: ', french_translation)

english_translation = french_to_english(input('French: '))
print('English: ', english_translation)
