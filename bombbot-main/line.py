
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import pyautogui

def send_capture_screen():
    url = 'https://notify-api.line.me/api/notify'
    # change your token
    token = '{your token}'
    headers = {'Authorization':'Bearer '+token}
    capture_file = "capture.png"
    pyautogui.screenshot(capture_file)
    files = {'imageFile': open(capture_file, 'rb')}
    print(files)
    r = requests.post(url, headers=headers , data = {'message': 'message'}, files=files)
    print(r.content)

