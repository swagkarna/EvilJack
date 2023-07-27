from flask import Flask, render_template, send_file, abort, jsonify
import os
import glob
import time
import base64

app = Flask(__name__)

def get_latest_qr_code():
    qr_code_dir = "evil_qr_codes"
    qr_code_files = glob.glob(os.path.join(qr_code_dir, "*.png"))
    if qr_code_files:
        latest_qr_code = max(qr_code_files, key=os.path.getctime)
        return latest_qr_code
    return None

@app.route('/')
def index():
    latest_qr_code = get_latest_qr_code()
    latest_qr_code_filename = os.path.basename(latest_qr_code) if latest_qr_code else None

    return render_template('index.html', latest_qr_code_filename=latest_qr_code_filename)

@app.route('/latest_qr_code')
def latest_qr_code():
    latest_qr_code = get_latest_qr_code()
    if latest_qr_code:
        with open(latest_qr_code, "rb") as file:
            qr_image = base64.b64encode(file.read()).decode('utf-8')
            return jsonify({"qr_image": qr_image})
    else:
        return jsonify({"qr_image": None})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
