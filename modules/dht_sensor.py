import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D4)

def read_dht22():
    while True:
        try:
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity
            return temperature, humidity
        except RuntimeError as e:
            print(f"DHT22 오류: {e}")
        time.sleep(2)
