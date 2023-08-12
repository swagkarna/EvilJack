
import os
import time
import pyautogui
from pyzbar import pyzbar
from PIL import Image

def capture_and_save_qr_codes():
    if not os.path.exists("evil_qr_codes"):
        os.mkdir("evil_qr_codes")
    
    while True:
        screenshot = pyautogui.screenshot()
        qr_codes = pyzbar.decode(screenshot)
        if qr_codes:
            for idx, qr_code in enumerate(qr_codes, start=1):
                qr_data = qr_code.data.decode('utf-8')
                print(f"Detected QR code ({idx}): {qr_data}")
                qr_box = qr_code.rect
                qr_area = screenshot.crop((qr_box.left, qr_box.top, qr_box.left + qr_box.width, qr_box.top + qr_box.height))
                qr_area.save(f"evil_qr_codes/qr_code.png")

        time.sleep(0.5)

if __name__ == "__main__":
    try:
        print("QR code detection and screenshot initiation... 😈")
        capture_and_save_qr_codes()
    except KeyboardInterrupt:
        print("\nStopping the evil operation. Bye! 😈")
