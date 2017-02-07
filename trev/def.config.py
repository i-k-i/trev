#logging
import logging
formatter = '[%(levelname)s]%(asctime)s - %(pathname)s:%(lineno)d - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=formatter)

# ***ll***
# lingualeo auth
# register
ll_login = 'email'
ll_passwd = 'passwd'
# ***end ll***

# ***ya***
# yandex translate API key
# get key:  https://tech.yandex.com/keys/get/?service=trnsl
yatapi_key = 'yandex_api_key'
# ***end ya***
