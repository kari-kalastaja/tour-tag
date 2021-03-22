#!/usr/bin/env python

import time
from sys import exit
import threading

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

import unicornhathd


class Led:
    def __init__(self):
        self.on = True
        self.thread = None
    
    def show(self, lines, text_colour, back_colour, arrival_time=-1):
        if self.thread != None:
            self.on = False
            self.thread.join()
            self.on = True
            self.thread = threading.Thread(target=self.led_on, args=(lines, text_colour, back_colour, arrival_time))
            self.thread.start()
        else:
            self.thread = threading.Thread(target=self.led_on, args=(lines, text_colour, back_colour, arrival_time))
            self.thread.start()
    
    def led_on(self, input_lines, text_colour, back_colour, arrival_time=-1):

        FONT = ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 12)

        unicornhathd.rotation(270)
        unicornhathd.brightness(0.6)


        width, height = unicornhathd.get_shape()

        text_x = width
        text_y = 0

        font_file, font_size = FONT

        font = ImageFont.truetype(font_file, font_size)
        
        start_time = time.time()
        
        while self.on:
            lines = input_lines.copy()
            if arrival_time != -1:
                time_passed = time.time() - start_time
                time_left = arrival_time - int(time_passed/60)
                if time_left < 0:
                    ar_t = "We have arrived"
                else:
                    ar_t = "Arrival time: " + str(time_left) + "min"
                lines.append(ar_t)
            
            text_width, text_height = width, 0

            for line in lines:
                w, h = font.getsize(line)
                text_width += w + width
                text_height = max(text_height, h)

            text_width += width + text_x + 1

            image = Image.new('RGB', (text_width, max(16, text_height)), back_colour)
            draw = ImageDraw.Draw(image)

            offset_left = 0

            for index, line in enumerate(lines):
                draw.text((text_x + offset_left, text_y), line, text_colour, font=font)

                offset_left += font.getsize(line)[0] + width
            for scroll in range(text_width - width):
                for x in range(width):
                    for y in range(height):
                        pixel = image.getpixel((x + scroll, y))
                        r, g, b = [int(n) for n in pixel]
                        unicornhathd.set_pixel(width - 1 - x, y, r, g, b)

                unicornhathd.show()
                time.sleep(0.02)
        unicornhathd.off()
    def led_off(self):
        if self.thread != None:
            self.on = False
            self.thread.join()
            self.thread = None
        
try:
    led = Led()
    led.show(["hellurei"], (0, 255, 0), (0,0,0), 50)
    time.sleep(5)
    led.show(["hellurei"], (255, 0, 0), (0,0,0), 10)
    time.sleep(5)
    led.led_off()
except KeyboardInterrupt:
    unicornhathd.off()

