"""
This is a translator
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate english to french
    """
    #write the code here
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate french to english
    """
    #write the code here
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
