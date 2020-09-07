import mss

top = int(input('Price Area (Top): '))
left = int(input('Price Area (Left): '))
width = int(input('Price Area (Width): '))
height = int(input('Price Area (Height): '))

price_area = {"top": top, "left": left, "width": width, "height": height}

with mss.mss() as sct:
    output = "sct.png"
    scr = sct.grab(price_area)
    mss.tools.to_png(scr.rgb, scr.size, output=output)
    print("Check", output)
