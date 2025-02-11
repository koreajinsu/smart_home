from gtts import gTTS
import pygame
import os
import tempfile

def speak(text):
    try:
        tts = gTTS(text=text, lang='ko')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as mp3_file:
            tts.save(mp3_file.name)

        pygame.mixer.init()
        pygame.mixer.music.load(mp3_file.name)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        os.remove(mp3_file.name)
    except Exception as e:
        print(f"음성 출력 오류: {e}")
