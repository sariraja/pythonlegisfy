from  bs4 import BeautifulSoup as bs
import requests


session = requests.session()
url = "https://drt.gov.in/front/page1_advocate.php"
r = session.get(url)
soup = bs(r.text, 'html.parser')
img = soup.find('img', id='captchatext')
img_SRC = "https://drt.gov.in/front/captcha.php"

with open('captcha.php', 'wb') as handle:
    response = requests.get(img_SRC, stream=True)
    if not response.ok:
        print("ok")
    for block in response.iter_content(1024):
        if not block:
            break
        handle.write(block)
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pic = Image.open('captcha.php')
pytesseract.pytesseract.tesseract_cmd = r'Enter the installation path of the \tesseract.exe'
captchaText = pytesseract.image_to_string(pic)

