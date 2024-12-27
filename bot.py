import pyautogui
import time
import keyboard
import random
import win32api
import win32con

battle_button = 'battle.png'
ok_button = 'ok.png'
target_card = 'target.png'
elixir_x2 = 'x2.png'
cards_positions = [ (2020,1277),(2177,1271),(2323,1273),(2440,1277)]
cycle_units_x = (2200,2300)
cycle_units_y = (800,850)
target_x = (2200,2260)
target_y = (1075,1100)
time_sleep = 4
time_sleep_when_elixir_2 = 2

while True:
    while True:
        try:
            location = pyautogui.locateOnScreen(battle_button, confidence=0.8)  # Use confidence for partial matching
            if location:
                print(f'Battle button found at {location}')
                point_location = pyautogui.center(location)
                x, y = point_location
                pyautogui.click(x = x, y = y)
                time.sleep(10)
                break
        except pyautogui.ImageNotFoundException:
            print('Battle button not found')
    is_elixir_x2 = False

    while True:
        try:
            location = pyautogui.locateOnScreen(ok_button, confidence=0.8)  # Use confidence for partial matching
            if location:
                print(f'Ok button found at {location}')
                point_location = pyautogui.center(location)
                x, y = point_location
                pyautogui.click(x = x, y = y)
                time.sleep(10)
                break
        except pyautogui.ImageNotFoundException:
            print('Still fighting')
            if not is_elixir_x2:
                try:
                    elixir_location = pyautogui.locateOnScreen(elixir_x2,confidence=0.8)
                    if elixir_location:
                        is_elixir_x2 = True
                        print('elixir_x2 time')
                except pyautogui.ImageNotFoundException:
                    print('Not elixir_x2')
            try:
                target_location = pyautogui.locateOnScreen(target_card,confidence=0.8) 
                if target_location:
                    print(f'Target found at {location}')
                    target_point = pyautogui.center(target_location)
                    x, y = target_point
                    x = x + random.randint(1,10)
                    y = y + random.randint(1,10)
                    pyautogui.click(x = x, y = y)
                    print(f'Clicked target at x={x} y={y}')
                    time.sleep(0.25)
                    random_x = random.randint(target_x[0],target_x[1])
                    random_y = random.randint(target_y[0],target_y[1])
                    pyautogui.click(x = random_x, y = random_y)
                    if is_elixir_x2:
                        time.sleep(time_sleep_when_elixir_2)
                    else:
                        time.sleep(time_sleep)
            except pyautogui.ImageNotFoundException:
                print('Target not found')
                position = random.randint(0,3)
                x,y = cards_positions[position]
                x = x + random.randint(1,10)
                y = y + random.randint(1,10)
                pyautogui.click(x = x, y = y)
                print(f'Clicked cycle unit x={x} y={y}')
                time.sleep(0.25)
                random_x = random.randint(cycle_units_x[0],cycle_units_x[1])
                random_y = random.randint(cycle_units_y[0],cycle_units_y[1])
                pyautogui.click(x = random_x, y = random_y)
                if is_elixir_x2:
                    time.sleep(time_sleep_when_elixir_2)
                else:
                    time.sleep(time_sleep)
