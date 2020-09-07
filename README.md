# Help Me Buy 🤖

Tired of camping and refreshing the TS to buy your item?

HMB automates the process of buying items off the Trade Station in the mobile game MSM.

1. Search for the item you are waiting to buy such that it is in the first row
2. Start HMB\* with a set threshold price
3. When an item is listed below threshold price, HMB helps you buy the first (lowest price) listing of the item.

\*Read on, don't be fooled, this is one loaded step...

## Disclaimer

- In its current state, HMB is very unrefined (probably an understatement, just look at the amount of setup to get it to work 🤮) GUI app version that is more user-friendly may come someday...

- Following from above, use and experiment HMB at your own risk! I'm not responsible for bans/losses from the use of HMB.

- The codes are all in the script for you to tinker if you know what you are doing. Do share what worked for you, or suggestions for improvement, I **MAY** just update it but I'm also lazy af ✌

- HMB is not intended for you if you are looking to profit from botting, I can only trust your integrity 😇

- Inspired by [Engineer Man](https://www.youtube.com/channel/UCrUL8K81R4VBzm-KOYwrcxQ) from YouTube (automating Android games series)

## Guide

This guide is limited to Windows + BlueStacks users for now.

### Things To Install

1. Install [tesseract](https://digi.bib.uni-mannheim.de/tesseract/) (tested with v5.0.0-alpha.20200328) and add its directory to PATH

2. Install Python and pip, add to PATH (Google how to do this on Windows)

3. Clone this project, navigate into the folder from **Command Prompt** and install requirements with `pip install -r requirements.txt`

4. Download Android Debug Bridge (ADB) for Windows. [Here](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) is the official download link.

5. Install BlueStacks and of course the game itself.

### Setup

Currently, HMB requires the BlueStacks window to be open and "on top", so that it can read the price of the items. The _pin to top_ option in BlueStacks is recommended.

1. Finding the **Price Area**

   - Pick a permanent spot on your monitor where your BlueStacks window will remain open.
   - Open MSM TS and search for the item to buy.
   - Run `python price_area.py` from HMB folder.
   - Make guesses (yes guesses lmao) for the location (pixels) of the price of the item on your monitor.
   - Check the output screenshot `sct.png` to see what area is being captured.
   - Keep repeating this till the area only captures the lowest price of the item. Take note of the pixel values.

2. Start ADB

   - Extract the ADB zip, navigate into the folder from **Command Prompt** and run `adb start-server`
   - From BlueStacks, go to Settings > Preferences > Platform settings > Enable ADB (take note of the port number after the `:` in the IP address).
   - Run `adb devices` and see if an emulator with that port number is in the list
     - If not in the list, you have to run `adb connect localhost:XXXX` replacing XXXX with the port number.

3. First time running HMB

   - From BlueStacks, enable [show pointer location](https://support.bluestacks.com/hc/en-us/articles/360048200932-How-to-view-tap-points-in-BlueStacks-4)
   - Run `python hmb.py` from HMB folder.
   - Fill in the **Price Area** values you found in Step 1
   - Now HMB needs to know where to click to purchase the item, it will ask for some X & Y values. Basically try clicking (and holding) in BlueStacks, then look at the bar on top for the X & Y values for that position.
     - **Top Item** - position to click for the first listing
     - **Buy Button** - position of the buy button
     - **Buy Confirm Button** - position of the next buy button
     - **Refresh** - position to click that will refresh listings (the item category names e.g. Hat/Outfit/Gloves/Shoes)
     - **Refresh Rate** - interval between refresh (in seconds)
     - **Threshold** - HMB will buy the lowest priced item if it is below this threshold you set
   - Take note of all the X & Y values you used, you can now disable the pointer location.

4. Running HMB
   - Create a .txt file (e.g. `input.txt`) inside HMB folder
   - Write the values used in Step 3 (in the same order that you entered them) into this file, each value on a new line, save.
   - Now you can run HMB with just `python hmb.py < input.txt` from the HMB folder.
