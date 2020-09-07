import time
import cv2
import mss
import numpy as np
import pytesseract
from PIL import Image
from ppadb.client import Client as AdbClient

# Connect to ADB
adb = AdbClient(host='localhost', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('No attached device found!')
    quit()

device = devices[0]

# Set Variables
try:
    top = int(input('Price Area (Top): '))
    left = int(input('Price Area (Left): '))
    width = int(input('Price Area (Width): '))
    height = int(input('Price Area (Height): '))

    price_area = {"top": top, "left": left, "width": width, "height": height}

    top_item_x = int(input('Top Item X: '))
    top_item_y = int(input('Top Item Y: '))

    buy_btn_x = int(input('Buy Button X: '))
    buy_btn_y = int(input('Buy Button Y: '))

    cfm_btn_x = int(input('Buy Confirm Button X: '))
    cfm_btn_y = int(input('Buy Confirm Button Y: '))

    refresh_x = int(input('Refresh X: '))
    refresh_y = int(input('Refresh Y: '))
    refresh_rate_seconds = float(input('Refresh Rate: '))

    max_price = int(input("Threshold: "))
except ValueError:
    print("Invalid input!")

t0 = time.time()  # Start time
bought = False
sct = mss.mss()


def snipe():
    # Item Type
    device.shell('input touchscreen tap {} {}'.format(top_item_x, top_item_y))
    time.sleep(0.1)
    # First Listing (Lowest Price)
    device.shell('input touchscreen tap {} {}'.format(top_item_x, top_item_y))
    time.sleep(0.8)
    # Buy
    device.shell('input touchscreen tap {} {}'.format(buy_btn_x, buy_btn_y))
    time.sleep(0.6)
    # Confirm
    device.shell('input touchscreen tap {} {}'.format(cfm_btn_x, cfm_btn_y))
    global bought
    bought = True
    t1 = time.time() - t0
    timestr = time.strftime("%H:%M:%S", time.gmtime(t1))
    print('Time Elapsed:', timestr)


while not bought:
    # Refresh
    device.shell('input touchscreen tap {} {}'.format(refresh_x, refresh_y))
    time.sleep(refresh_rate_seconds)

    # Check price
    scr = sct.grab(price_area)
    price_ss = np.array(scr)
    price_raw = pytesseract.image_to_string(price_ss)

    # Check if max_price
    if price_raw != '':
        lowest_str = price_raw.split()[0]
        lowest = int(lowest_str.replace(',', ''))
        dt = time.time() - t0
        dt_str = time.strftime("%H:%M:%S", time.gmtime(dt))
        print('[{}] {}'.format(dt_str, lowest))
        if (lowest < max_price):
            snipe()
            print('Price:', lowest)
