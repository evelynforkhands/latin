# coding=utf8

import json
import requests
import time
import urllib


wiuyakurgskhjgfkhfgksjhfgdd = '692224945:AAH9yaX_jp7o6hskjTnMet5N6KgLt20wywM'
URL = "https://api.telegram.org/bot{}/".format(wiuyakurgskhjgfkhfgksjhfgdd)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()


# import requests
# import datetime

# class BotHandler:

#     def __init__(self, ewkhealjkwheljkheljheljkfbbfksjfkjsfbkf):
#         self.ewkhealjkwheljkheljheljkfbbfksjfkjsfbkf = ewkhealjkwheljkheljheljkfbbfksjfkjsfbkf
#         self.api_url = "https://api.telegram.org/bot{}/".format(ewkhealjkwheljkheljheljkfbbfksjfkjsfbkf)

#     def get_updates(self, offset=None, timeout=1):
#         method = 'getUpdates'
#         params = {'timeout': timeout, 'offset': offset}
#         resp = requests.get(self.api_url + method, params)
#         result_json = resp.json()['result']
#         return result_json

#     def send_message(self, chat_id, text):
#         params = {'chat_id': chat_id, 'text': text}
#         method = 'sendMessage'
#         resp = requests.post(self.api_url + method, params)
#         return resp

#     def get_last_update(self):
#         get_result = self.get_updates()
        
#         if len(get_result) > 0:
#             last_update = get_result[-1]
#         else:
#             last_update = get_result

#         return last_update



# greet_bot = BotHandler('692224945:AAH9yaX_jp7o6hskjTnMet5N6KgLt20wywM')
# greetings = ('hello', 'hi', 'greetings', 'sup', 'Привет', 'здравствуй')
# now = datetime.datetime.now()


# def main():

#     new_offset = None
#     today = now.day
#     hour = now.hour

#     while True:


#         greet_bot.get_updates(new_offset)

#         last_update = greet_bot.get_last_update()
                    
#         last_update_id = last_update['update_id']
#         last_chat_text = last_update['message']['text']
#         last_chat_id = last_update['message']['chat']['id']
#         last_chat_name = last_update['message']['chat']['first_name']

#         if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
#             greet_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
#             today += 1

#         elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
#             greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
#             today += 1

#         elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
#             greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
#             today += 1

#         new_offset=last_update_id + 1

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         exit()