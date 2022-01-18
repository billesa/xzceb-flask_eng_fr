"""Module cretaes an instance of LanguageTranslatorV3 and defines methods for access
"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """Translates from english to french
    """
    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr'
    )
    return frenchText

def frenchToEnglish(frenchText):
    """Translates from french to english
    """
    englishText = language_translator.translate(
        text=frenchText,
        model_id='fr-en'
    )
    return frenchText