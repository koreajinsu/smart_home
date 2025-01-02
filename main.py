from modules.hardware import initialize_gpio, cleanup
from modules.lcd_display import initialize_lcd, update_lcd_static
from modules.voice_control import recognize_voice_commands
from modules.utility import listen_for_key_input
import threading
import time

# 초기화
initialize_gpio()
initialize_lcd()

# 스레드 시작
dht_thread = threading.Thread(target=read_dht22, daemon=True)
dht_thread.start()

voice_thread = threading.Thread(target=recognize_voice_commands, daemon=True)
voice_thread.start()

key_thread = threading.Thread(target=listen_for_key_input, daemon=True)
key_thread.start()

# 메인 루프
try:
    while True:
        update_lcd_static()
        time.sleep(1)
except KeyboardInterrupt:
    cleanup()
