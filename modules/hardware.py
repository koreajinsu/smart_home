import RPi.GPIO as GPIO
import time
import busio
from adafruit_pca9685 import PCA9685

# GPIO 핀 설정
LED_PINS = {'red': 23, 'green': 24, 'blue': 25}
RELAY_PIN = 17
SWITCH_PIN = 26

# I2C 및 모터 드라이버 설정
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 60

MOTOR_A = {'ena': 8, 'in1': 9, 'in2': 10}
MOTOR_B = {'ena': 13, 'in1': 11, 'in2': 12}

GPIO.setmode(GPIO.BCM)
GPIO.setup(list(LED_PINS.values()) + [RELAY_PIN, SWITCH_PIN], GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def set_motor(motor, speed_percent, direction=None):
    try:
        speed = min(max(speed_percent, 0), 100)
        duty_cycle = int(speed / 100.0 * 0xFFFF)
        pca.channels[motor['ena']].duty_cycle = duty_cycle

        if direction == 'forward':
            pca.channels[motor['in1']].duty_cycle = 0xFFFF
            pca.channels[motor['in2']].duty_cycle = 0x0000
        elif direction == 'backward':
            pca.channels[motor['in1']].duty_cycle = 0x0000
            pca.channels[motor['in2']].duty_cycle = 0xFFFF
        else:
            pca.channels[motor['in1']].duty_cycle = 0x0000
            pca.channels[motor['in2']].duty_cycle = 0x0000
    except Exception as e:
        print(f"모터 제어 오류: {e}")

def control_relay(state):
    GPIO.output(RELAY_PIN, GPIO.HIGH if state == 'on' else GPIO.LOW)

def cleanup():
    GPIO.cleanup()
    pca.deinit()
    print("하드웨어 정리 완료")
