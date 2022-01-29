
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import pyautogui

# Remember that './secret_key.txt' is encrypted until it's needed, and only read by a non-root user
with open('./secret.txt') as f:
    SECRET_KEY = f.read().strip() 

def send_capture_screen(message='default message'):
    url = 'https://notify-api.line.me/api/notify'
    # change your token
    token = SECRET_KEY
    headers = {'Authorization':'Bearer '+token}
    capture_file = "capture.png"
    pyautogui.screenshot(capture_file)
    files = {'imageFile': open(capture_file, 'rb')}
    print(files)
    r = requests.post(url, headers=headers , data = {'message': message}, files=files)
    print(r.content)

