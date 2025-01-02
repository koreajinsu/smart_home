import speech_recognition as sr
from modules.motor_control import set_motor, run_motor_for_seconds
from modules.utility import speak

def recognize_voice_commands():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio, language='ko-KR')
                process_voice_command(command)
            except sr.UnknownValueError:
                print("명령을 이해하지 못했습니다.")
            except sr.RequestError as e:
                print(f"음성 인식 오류: {e}")

def process_voice_command(command):
    if "커튼 올려" in command:
        run_motor_for_seconds(MOTOR_A, 'forward', 25, 1)
        speak("커튼을 올립니다.")
    elif "불 켜" in command:
        speak("불을 켭니다.")
    else:
        speak("알 수 없는 명령입니다.")
