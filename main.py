import time
import threading
from modules.lcd_display import initialize_lcd, update_lcd_static
from modules.dht_sensor import read_dht22
from modules.voice_control import recognize_voice_commands
from modules.utility import listen_for_key_input
from modules.hardware import cleanup

initialize_lcd()

# 스레드 실행
dht_thread = threading.Thread(target=read_dht22, daemon=True)
dht_thread.start()

voice_thread = threading.Thread(target=recognize_voice_commands, daemon=True)
voice_thread.start()

key_thread = threading.Thread(target=listen_for_key_input, daemon=True)
key_thread.start()

try:
    while True:
        update_lcd_static("Idle", "Off")
        time.sleep(1)
except KeyboardInterrupt:
    cleanup()
