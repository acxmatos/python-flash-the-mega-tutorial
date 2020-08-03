import json
import requests
from flask_babel import _

from app import app

def translate(text, source_language, dest_language):
    # Code based on: https://www.labnol.org/code/19909-google-translate-api
    r = requests.get('https://translate.googleapis.com/translate_a'
                     '/single?client=gtx&sl={}&tl={}&dt=t&q={}'.format(
                         source_language, dest_language, text))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    response = json.loads(r.content.decode('utf-8-sig'))

    # Response json has a series of arrays. The translated text is three arrays deep
    return response[0][0][0]