from enum import Enum

class States(Enum):
    """
    Мы используем словарь, в которой храним всегда строковые данные,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_LINK = "1"
    S_ENTER_CAMPAIGN_NAME = "2"
    S_START_TRACKING_CAMPAIGN = "3"
    S_STOP_TRACKING_CAMPAIGN = "4"
    S_SEND_STICKER = "5"

token = '1246015474:AAE_NKdBl8yzf89zjoJfaxOhd3rYnsn-llQ'
stickers = {1:'CAACAgIAAxkBAAEBMexfNULi1BQeYvq1mTqL5VYP_LG9AgAC2AAD_OXdAAHG5O5jdHdpTxoE',
            2:'CAACAgIAAxkBAAEBJMdfKSbcR4hiQgRsQ9HivZ9oK6qhzAACFwEAAtLdaQXeYl54aAbKphoE',
            3:'CAACAgIAAxkBAAEBMe5fNUL7SgY6FjuU84-2Ge6ILySIDAACGAADkSHBEbMy_hUnfIW_GgQ',
            4:'CAACAgIAAxkBAAEBMfBfNUMeJk5U_Pkq0I885s9BwUpUUwACYQADU_hiCe0fcIJ2FiRDGgQ',
            5:'CAACAgIAAxkBAAEBJM9fKSdNWiG4mJiiJfhoPyoOGdlIYwACEgADdVCBE26opWd1F-9VGgQ',
            6:'CAACAgIAAxkBAAEBJNFfKSdZHkaYKoMPQ1eAFkTOoC9SRgACLgAD4djSAAH6uc0pGAABXwkaBA',
            7:'CAACAgIAAxkBAAEBJNNfKSd24KT1fJVkn2zrRLkwJZMJ2QACFQADg0cqOFMI5b7VynSqGgQ',
            8:'CAACAgIAAxkBAAEBMfJfNUMqsh4gJwaD8Vv2mXLinWByogACJQMAAubOVgwGCV3gX0iNNBoE',
            9:'CAACAgIAAxkBAAEBJNdfKSfONquRlqHmwwtrhzwyofI3tgACIAADFvHqEqDWa0lrY0FgGgQ',
            10:'CAACAgIAAxkBAAEBJNlfKSfdCFp9yCiCrdMxKRI9yDSlxwAC2gAD_OXdAAEiZoo4l1XxNhoE',
            11:'CAACAgIAAxkBAAEBJRhfKUUbwt4YJCPdnjy3VbuHCLjJ1gACSwAD3B1fMs8xSfx3nsMwGgQ'}

header = {'User-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:79.0)'+ \
                           ' Gecko/20100101 Firefox/79.0', # Создаем заголовок, чтобы сайты не воспринимали нас как бота
              'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'}
cookies = dict(cookies_are='session=4b082e00-074c-75f7-4761-4fb12bbb343b; __utma=12798129.510440631.1596800516.'
                               '1596800516.1596800516.1; __utmc=12798129;' + \
                               ' __utmz=12798129.1596800516.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|' + \
                               'utmctr=(not%20provided); __gads=ID=19506182921d16b7:T=1596800516:S=ALNI' + \
                               '_MY-XwLcuZvDvxMnb7lEx3kAG7ideQ; __qca=P0-23977826-1596800516655;' + \
                               ' _ga=GA1.2.1387315142.1596800524; _gid=GA1.2.525403005.1596800524')
soup_type = 'lxml'
auth = {'user':'b60d1e2a8f35c3', 'password':'480afd1d','host':'us-cdbr-east-02.cleardb.com'}
