<p align="center">
<img src='https://github.com/swagkarna/EvilJack/blob/3c370b6c0aa3cbc0e094f0f04c0d838b2703fb4b/screenshots/evil.gif'></img>
</p>
<p align=center>  
<a href=https://github.com/swagkarna><img src="https://img.shields.io/badge/Author-Swagkarna-red.svg?style=for-the-badge&label=Author" /></a>

<img src="https://img.shields.io/badge/Version-1.0-brightgreen?style=for-the-badge" > 
<img src="https://img.shields.io/github/followers/swagkarna?label=Followers&style=for-the-badge">
</p> 

 ---
 * **If you like the tool and for my personal motivation so as to develop other tools please  leave a +1 star** 
  ---
## What is QRLJacking?
---  

QRLJacking, also known as Quick Response Code Login Jacking, is a straightforward yet highly malicious attack method that targets applications utilizing the "Login with QR code" feature as a supposedly secure means of account access. The primary objective of this attack is to hijack users' sessions, enabling attackers to gain unauthorized access to their accounts

---
## Installation ☑️

```
python -m venv venv
venv\Scripts\activate
pip install pyautogui pyzbar Pillow Flask pyocr pytesseract
```
If you get dll error in pyzbar module visit this site:
https://stackoverflow.com/questions/64570443/q-how-to-fix-the-missing-dependancies-in-pyzbar
## Requirements 🧾
<p>
To install Tesseract OCR on Windows, follow these steps:

- Download the Tesseract OCR Installer:
- Visit the Tesseract OCR GitHub page: https://github.com/tesseract-ocr/tesseract

- Scroll down to the "Downloads" section and click on "tesseract-ocr-w64-setup-v5.x.x.exe" (where "x.x" represents the version number) to download the Windows installer for Tesseract OCR.

## Run the Tesseract Installer
- Double-click on the downloaded "tesseract-ocr-w64-setup-v5.x.x.exe" file to run the installer.

- Choose Components (Optional)
During the installation, you will be asked to select the components to install. You can keep the default options or customize them based on your needs. At a minimum, make sure the "Tesseract OCR" component is selected.

- Set Installation Path (Optional)
The installer will prompt you to choose an installation directory. You can keep the default or specify a different one. If you change the path, make sure to remember it for later steps.
## Add Tesseract to path 
### Just add the folder to the Path under Windows (not sure with Win7)
- Control Panel > System and Security > System >
- Advanced system settings > Advanced > Environment variables > PATH > New
#### Add this to path 

```
C:\Program Files\Tesseract-OCR
```
<img src='https://github.com/swagkarna/EvilJack/blob/d32641a8c476c703dad6a6095bccbf5e5ca8e086/screenshots/Screenshot%20(108)_LI.jpg'></img>
</p>

### Note : After adding Tesseract-OCR to path make sure to restart your pc
---
## EvilJack in Action 
---
- Run evil_jack.py and server.py 
- Open web.whatsapp.com in a separate window in your browser. Note: Do not close or minimize the window because EvilJack will continuously take screenshots of the QR code on web.whatsapp.com and send them to our phishing page. 
- Now send the phishing link `127.0.0.1:5000` to victim . Note the link `127.0.0.1:5000` only work if victim connected to same network .To perform the attack outside the wan use ngrok or portmap.io 
- After the victim scans the code, you will gain access to his WhatsApp session. Additionally, after the victim has scanned the QR code, he will be automatically redirected to a fake verification page
---
### <a href='https://www.youtube.com/watch?v=7CE79X5tOi8'>PortForwarding with portmap.io</a>

### Note : Make sure you forward Port:5000 in portmap.io
---
## Screenshots 
<p align="left">
   <img src="https://github.com/swagkarna/EvilJack/blob/ce4d74ca266a4c4cee69c39021665e8a400e1537/screenshots/1.png" width=750px height=500px>
   </p>
   <p align="left">
   <img src="https://github.com/swagkarna/EvilJack/blob/ce4d74ca266a4c4cee69c39021665e8a400e1537/screenshots/2.png" width=750px height=500px>
   </p>
   <p align="left">
   <img src="https://github.com/swagkarna/EvilJack/blob/ce4d74ca266a4c4cee69c39021665e8a400e1537/screenshots/3.png" width=750px height=500px>
   </p>
--- 

## EvilJack Demo   

https://github.com/swagkarna/EvilJack/assets/46685308/77fd0f85-8f85-47f3-a4fd-a6ffca758cde

---
###  script  to auto click the QR code reload element on whatsappweb

Open chrome/firefox and navigate to `console tab` from developer option and paste the following code
```
function checkAndClickButton() {
  const button = document.querySelector('.Jht5u');
  if (button) {
    button.click();
  }
}

// Set an interval to periodically check and click the button (e.g., every 5 seconds)
setInterval(checkAndClickButton, 2000);
```
## EvilJack tested on following sites 

- [X] Whatsapp
- [X] Telegram
- [X] Discord
- [X] steam
- [X] AirDroid
- [X] Tiktok 
---

## Disclaimer ⚠️
<b>swagkarna Provides no warranty and will not be responsible for any direct or indirect damage caused by this tool.<br>
  EVILJACK is built for Educational and Internal use ONLY.</b>
