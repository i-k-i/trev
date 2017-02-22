import requests
import logging
from . import config


class LinguaLeo:
    # [Full request URI: http://api.lingualeo.com/gettranslates?port=1001]
    # [Full request URI: http://api.lingualeo.com/translate.php?q=%D0%BA%D0%BE%D1%82&source=ru&target=en&port=1001]
    urls = {
        'login': 'https://api.lingualeo.com/api/login',
        'add_word': 'https://api.lingualeo.com/addword',
        'translates': 'http://api.lingualeo.com/gettranslates',
        'translate.php': ' http://api.lingualeo.com/translate.php'
    }
    session = requests.Session()

    def __check_resp__(self, resp):
        if resp.status_code != 200:
            logging.error('Status code: %s', resp.status_code)
            # resp.raise_for_status()
            return False
        if not hasattr(resp, 'json'):
            logging.error('Response from {} has no json data. Status code: {}'.format(resp.url, resp.status_code))
            return False
        if 'error_msg' in resp.json():
            if resp.json()['error_msg']:
                logging.error('Response contains error message: {}'.format(resp.json()['error_msg']))
                return False
        return True

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        params = {
            "email": self.email,
            "password": self.password
        }
        resp = self.session.get(url = self.urls['login'], params=params)
        if self.__check_resp__(resp):
            return resp

    def add_word(self, word, tword, source='en', target='ru'):
        '''"word must be in english" - LinguaLeo '''
        cor_word, cor_tword = self.prepare_to_adding(word, tword, source, target)
        data = {
            "word": cor_word,
            "tword": cor_tword,
            "context": "",
            "context_url": "null",
            "context_title": "",
            "port": "1001"
        }

        resp = self.session.post(self.urls['add_word'], data=data)
        if self.__check_resp__(resp):
            return resp

    def prepare_to_adding(self, word, tword, source, target):
        if (source, target) == ('en', 'ru'):
            return word, tword
        elif (source,target) == ('ru', 'en'):
            return tword, word
        else:
            logging.error('Oy vey. Source: {}, target: {}'. format(source, target))
            return ('None','нет')

    def translate(self, word, source='ru', target='en'):
        '''translates from any language'''
        params = {
            'q':word,
            'source':source,
            'target':target
        }
        resp = self.session.get(url=self.urls['translate.php'], params=params)
        if self.__check_resp__(resp):
            return resp

    def post_translate(self, word, source='ru', target='en'):
        '''TODO: check data in original response.
        translates only enlish'''
        data = {
            'word':word,
            'source':source,
            'target':target
        }
        resp = self.session.post(url=self.urls['translates'], data=data)
        if self.__check_resp__(resp):
            return resp


def main():
    # import ipdb; ipdb.set_trace()
    ll = LinguaLeo(config.ll_login, config.ll_passwd)
    ll.login()
    # resp = ll.add_word('offset', 'смещение')
    resp = ll.add_word('sunrise', 'восход солнца')

if __name__ == '__main__':
    main()
