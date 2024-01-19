import time

import requests

ADMINS = [5908702613]
def pulling():
   update_id = 0
   while True:
       time.sleep(0.5)
       r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
       update_id_new = r['result'][-1]['update_id']
       if update_id != update_id_new:
           count_message = len(r['result'])
           message = r['result'][-1]
           print(message)
           file_id = message['message']['photo'][-1]['file_id']
           if 'caption' in message['message']:
               caption = message['message']['caption']
           else:
               caption = 'Нет описания'
           user_id = message['message']['from']['id']
           user_name = message['message']['from']['username']
           requests.get(f'{BASE_URL}{TOKEN}/sendPhoto?chat_id={user_id}&photo={file_id}&caption={caption}')
       update_id = update_id_new

pulling()

