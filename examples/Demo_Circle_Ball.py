from machine import Pin, SPI
import random
import st7789  # library of TFT display controller uses SPI interface
from time import sleep

# Set up the SPI and TFT displays
spi0 = SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19))
spi1 = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))

# Define TFT displays with different CS pins
tft0 = st7789.ST7789(spi0, 240, 240, reset=Pin(16, Pin.OUT), cs=Pin(17, Pin.OUT), dc=Pin(6, Pin.OUT), backlight=Pin(7, Pin.OUT), rotation=0)
tft1 = st7789.ST7789(spi1, 240, 240, reset=Pin(12, Pin.OUT), cs=Pin(13, Pin.OUT), dc=Pin(14, Pin.OUT), backlight=Pin(15, Pin.OUT), rotation=0)

tft0.init()
tft1.init()

# Initialize the displays with a black background
tft0.fill(0)
tft1.fill(0)

# Define ball properties
ball_radius = 10
ball_color = st7789.color565(255, 0, 0)  # Red color for the ball
bg_color = st7789.color565(0, 0, 0)      # Black background
ball_speed_x = 2
ball_speed_y = 2

# Initial position of the balls
ball_x0 = 50
ball_y0 = 50
ball_x1 = 100
ball_y1 = 100

# Animation loop
while True:
    # Clear the previous position of the balls
    tft0.fill_circle(ball_x0, ball_y0, ball_radius, bg_color)
    tft1.fill_circle(ball_x1, ball_y1, ball_radius, bg_color)
    
    # Update ball positions
    ball_x0 += ball_speed_x
    ball_y0 += ball_speed_y
    ball_x1 += ball_speed_x
    ball_y1 += ball_speed_y

    # Check for collision with screen boundaries and reverse direction if needed
    if ball_x0 - ball_radius < 0 or ball_x0 + ball_radius > 240:
        ball_speed_x = -ball_speed_x
    if ball_y0 - ball_radius < 0 or ball_y0 + ball_radius > 240:
        ball_speed_y = -ball_speed_y

    if ball_x1 - ball_radius < 0 or ball_x1 + ball_radius > 240:
        ball_speed_x = -ball_speed_x
    if ball_y1 - ball_radius < 0 or ball_y1 + ball_radius > 240:
        ball_speed_y = -ball_speed_y

    # Draw the balls at the new positions
    tft0.fill_circle(ball_x0, ball_y0, ball_radius, ball_color)
    tft1.fill_circle(ball_x1, ball_y1, ball_radius, ball_color)

    # Add a small delay to control the animation speed
    sleep(0.01)
