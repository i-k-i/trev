import requests
ex_url = 'https://translate.google.com/translate_a/single?client=t&sl=en&tl=ru&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&rom=1&ssel=3&tsel=4&kc=1&tk=60357.434328&q=dark'

def get_gtranslate(url, source_string, source_lang, result_lang):
    resp = requests.get(url)
    import ipdb; ipdb.set_trace()

def main():
    get_gtranslate(ex_url, 1,1,1)

if __name__ == '__main__':
    main()
