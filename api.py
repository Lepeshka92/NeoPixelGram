from gc import collect
from ujson import dumps
from requests import post


class TelegramBot:
    
    def __init__(self, token):
        self.url = 'https://api.telegram.org/bot{}/{}'.format(token, '{}')

        self.kbd = {
            'keyboard': [[]],
            'resize_keyboard': True,
            'one_time_keyboard': True}

        self.upd = {
            'offset': 0,
            'limit': 1,
            'timeout': 5,
            'allowed_updates': ['message']}

    def send(self, chat_id, text, keyboard=None):
        data = {'chat_id': chat_id, 'text': text}
        if keyboard:
            self.kbd['keyboard'] = keyboard
            data['reply_markup'] = dumps(self.kbd)
        try:
            post(self.url.format('sendMessage'), json=data)
        except:
            pass
        finally:
            collect()

    def update(self):
        result = None
        try:
            jo = post(self.url.format('getUpdates'), json=self.upd).json()
        except:
            return result
        finally:
            collect()
        if 'result' in jo:
            if jo['result'] and 'text' in jo['result'][0]['message']:
                if 'username' not in jo['result'][0]['message']['chat']:
                    jo['result'][0]['message']['chat']['username'] = 'guest'
                result = (jo['result'][0]['message']['chat']['id'],
                               jo['result'][0]['message']['chat']['username'],
                               jo['result'][0]['message']['text'])
        if result:
            self.upd['offset'] = jo['result'][-1]['update_id'] + 1
            
        return result