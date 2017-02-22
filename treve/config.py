#logging
import logging
filename = 'treve.log'
formatter = '[%(levelname)s]%(asctime)s - %(pathname)s:%(lineno)d - %(message)s'
logging.basicConfig(filename = filename, level=logging.DEBUG, format=formatter)

## ll
#  lingualeo aut
ll_login = 'w5540554@gmail.com'
ll_passwd = '327mZ0'

## ya
# yandex translate API key
# get key:  https://tech.yandex.com/keys/get/?service=trnsl
yatapi_key = 'trnsl.1.1.20170121T223424Z.b39a6fd533062e94.d1247c847a9bd695cc1d8c6dc89863eb842e82ee'
