import requests
import time

while True:
    r = requests.get('http://111.230.224.190/get_set_motion/')

    ch = r.json()['set_mode']
    payload = {'bot_mode': ch}
    print(ch)
    r = requests.post('http://111.230.224.190/update_bot_motion/', json=payload)
    print(r.text)
    time.sleep(1)
