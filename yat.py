import click
from yandex_translate import YandexTranslate
import notify2
import subprocess
import requests
from config import yatapi_key


ya_tr= YandexTranslate(yatapi_key)
directions = {'ru':'ru-en', 'en':'en-ru'}


def auto_translate_ya(source_string):
    try:
        source_lang = ya_tr.detect(source_string)
        trans_dir = directions[source_lang]
    except :
        trans_dir = directions['en']
    result = ya_tr.translate(source_string, trans_dir)
    return result


def main():
    print('Translate:', ya.translate('Привет, мир!', 'ru-en'))
    # import ipdb; ipdb.set_trace()
    # auto_translate('')

if __name__ == '__main__':
    main()
