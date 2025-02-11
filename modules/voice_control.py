import speech_recognition as sr
import time
import RPi.GPIO as GPIO
from .hardware import control_relay, set_motor
from .audio import speak

SWITCH_PIN = 26  # 스위치 핀 번호

def process_voice_command(command):
    try:
        if "불 켜" in command:
            control_relay('on')
        elif "불 꺼" in command:
            control_relay('off')
        elif "에어컨 켜" in command:
            set_motor(MOTOR_B, 20, 'forward')
            speak("에어컨을 켭니다.")
        elif "에어컨 꺼" in command:
            set_motor(MOTOR_B, 0, 'stop')
            speak("에어컨을 끕니다.")
        else:
            speak("알 수 없는 명령입니다.")
    except Exception as e:
        print(f"명령 처리 오류: {e}")

def recognize_voice_commands():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        if GPIO.input(SWITCH_PIN) == GPIO.LOW:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                try:
                    audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(audio, language='ko-KR')
                    process_voice_command(command)
                except Exception as e:
                    print(f"음성 인식 오류: {e}")
