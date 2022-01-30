from calendar import c
from math import remainder
import re
import pyautogui
import time
import line

pyautogui.FAILSAFE= 2.5


def is_loading():
    loading_img = pyautogui.locateOnScreen('images/loading.png', grayscale=True, confidence=0.7)
    if loading_img is None:
        return False
    print('loading is appear...')
    return True

def is_connected_metamask():
    # connect meta mask wallet when it's expire something
    result_connect_wallet_button = pyautogui.locateOnScreen('images/btn-connect-wallet.png', confidence=0.8)
    if result_connect_wallet_button is not None:
        x, y = pyautogui.center(result_connect_wallet_button)
        print("Click connect wallet")
        time.sleep(0.5)
        pyautogui.click(x, y)
        time.sleep(10)
        result_sign_button = pyautogui.locateOnScreen('images/btn-sign.png', confidence=0.8)
        if result_sign_button is not None:
            x, y = pyautogui.center(result_sign_button)
            print("Click sign wallet")
            time.sleep(0.5)
            pyautogui.click(x, y)
            time.sleep(15)

def click_treasure_box(cature_screen=True):
    print("click_treasure_box")
    treasure_box_button = pyautogui.locateOnScreen('images/treasure-box.jpg', confidence=0.8)
    if treasure_box_button is not None:
        x, y = pyautogui.center(treasure_box_button)
        time.sleep(0.5)
        pyautogui.click(x, y)
        time.sleep(1)
        line.send_capture_screen('thresure value') if cature_screen else 0
        time.sleep(1)
        click_close_button()


def time_with_click_refresh(cycle_time, refresh_min=10):
    '''
        cycle_time int minutes
        refresh_min int refresh_min
    '''
    round_ = cycle_time // refresh_min
    remainder = cycle_time % refresh_min
    print('round {} remainder {} ', (round_, remainder))
    for j in range(round_):
        print('accumulate sleep for ', 60*j*refresh_min, ' second')
        time.sleep(60*refresh_min)
    click_treasure_box()
    time.sleep(60*remainder)

def click_back_button():
    print("Process find green button back. Please wait...")
    result_find_back_button = pyautogui.locateOnScreen('images/btn-back.jpg', confidence=0.8)
    time.sleep(1)
    if result_find_back_button is not None:    
        print("Found green back button")
        x, y = pyautogui.center(result_find_back_button)
        print("Save position green back button")
        print(x,y)
        pyautogui.click(x, y)
        print("Click green back button")

def click_close_button():
    result_find_close_button = pyautogui.locateOnScreen('images/btn-close.jpg', confidence=0.8)
    if result_find_close_button is not None:
        x, y = pyautogui.center(result_find_close_button)
        print("Click close button")
        time.sleep(0.5)
        pyautogui.click(x, y)
        time.sleep(1)
        pyautogui.click(x, y)

def click_start_button():
    result_find_start_button = pyautogui.locateOnScreen('images/btn-start.jpg', confidence=0.8)
    if result_find_start_button is not None:
        x, y = pyautogui.center(result_find_start_button)
        print("Click start button")
        time.sleep(0.5)
        pyautogui.click(x, y)
        time.sleep(1)
        pyautogui.click(x, y)

def click_list_hero():
    result_find_list_hero = pyautogui.locateOnScreen('images/list-hero.jpg', grayscale=True, confidence=0.7)
    print("Find button list hero. Please wait...")
    #  Find hero image 
    if result_find_list_hero is not None:
        print("Find hero resting. Please wait...")
        x, y = pyautogui.center(result_find_list_hero)
        print(x,y)
        time.sleep(1)
        pyautogui.click(x, y, clicks=2, interval=0.25)
        time.sleep(1)

def main():
    i = 0
    count_hero_start = 0
    j = 0
    print("Program bot for bormcrypto start")
    print("Open browser for program one by one")
    print("Keep all hero to rest")
    print("After open 'Treasure Hunt' page and wait for end process")
    cycle_time = input("Input cycle time (Min.): \n")
    cycle_time = int(cycle_time)

    while j < 999:
        # Back Button function 
        click_back_button()

        # cature is loading
        while True:
            loading_img = pyautogui.locateOnScreen('images/loading.png', grayscale=True, confidence=0.7)
            if loading_img is None:
                break
            print('loading is appear...')
            time.sleep(1)

        # is connected meta mask
        is_connected_metamask()
        #find Hero function
        time.sleep(1)
        click_list_hero()
        # In the charecters dialog box
        while i <= 2:
            result_click_btn_work = pyautogui.locateOnScreen('images/btn-all.jpg', confidence=0.9)
            print('result_click_btn_work', result_click_btn_work)
            if result_click_btn_work is not None:
                time.sleep(1)
                x, y = pyautogui.center(result_click_btn_work)
                pyautogui.click(x, y)
                count_hero_start += 1
                print("Click work hero: ",count_hero_start)
            i += 1
            time.sleep(0.5)
        i=0
        print("Ready to start...")
        print("Find close button")
        time.sleep(0.5)
        click_close_button()
        print("Find start button")
        time.sleep(1)
        # find start button
        click_start_button()
        print("Program ready running re process in (Min)",cycle_time)
        line.send_capture_screen('current screen')
        # time.sleep(60*cycle_time)
        time_with_click_refresh(cycle_time)

main()
# time_with_click_refresh(2, 1)
# click_treasure_box()