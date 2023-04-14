# import libraries
from machine import Pin, I2C
import ssd1306
from time import sleep
import dht

# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# LCD Display Parameters
lcd_width = 128
lcd_height = 64
oled = ssd1306.SSD1306_I2C(lcd_width, lcd_height, i2c)

# DHT11 Sensor Parameters
sensor = dht.DHT22(Pin(13))

while True:
  try:
    # Read temperature and humidity from sensor
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    
    # Clear LCD display 
    oled.fill(0)
    # Display temperature and humidity on LCD 
    oled.text('TEMP: ' + str(temp) + ' C', 0, 0)
    oled.text('HUM: ' + str(hum) + ' %', 0, 10)

    # Update LCD display 
    oled.show()

    # Wait for 2 seconds before next reading 
    sleep(2)

  except OSError as e:
    print('Failed to read sensor.')