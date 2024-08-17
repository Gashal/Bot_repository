import requests
import time


API_URL = 'https://api.telegram.org/bot'
API_DOGS_URL = 'https://random.dog/woof.json'
BOT_TOKEN = ''
ERROR_TEXT = 'Здесь должна была быть картинка с собачкой :('
MAX_COUNTER = 100

offset = -2
counter = 0
dog_response: requests.Response
dog_link: str
chat_id: int

while counter < MAX_COUNTER:
    print('attempt =', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            dog_response = requests.get(API_DOGS_URL)
            if dog_response.status_code == 200:
                dog_link = dog_response.json()['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={dog_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1