
import os
import time
import pyautogui
from pyzbar import pyzbar
from PIL import Image, ImageOps

def capture_and_save_qr_codes():
    if not os.path.exists("evil_qr_codes"):
        os.mkdir("evil_qr_codes")
    
    while True:
        try:
            screenshot = pyautogui.screenshot()
        except Exception as e:
            print(f"An error occurred while taking a screenshot: {str(e)}")
            continue

        qr_codes = pyzbar.decode(screenshot)
        if qr_codes:
            for idx, qr_code in enumerate(qr_codes, start=1):
                qr_data = qr_code.data.decode('utf-8')
                print(f"Detected QR code ({idx}): {qr_data}")
                qr_box = qr_code.rect
                qr_area = screenshot.crop((qr_box.left, qr_box.top, qr_box.left + qr_box.width, qr_box.top + qr_box.height))

                # Resize and compress the QR code image
                qr_area.thumbnail((300, 300))  # Resize to 300x300 pixels

                # Save the compressed QR code image
                qr_area.save(f"evil_qr_codes/qr_code.png")

        time.sleep(1)

if __name__ == "__main__":
    try:
        print("QR code detection and screenshot initiation.... 😈")
        capture_and_save_qr_codes()
    except KeyboardInterrupt:
        print("\nStopping the evil operation. Bye! 😈")
