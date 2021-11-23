from bs4 import BeautifulSoup as bs
import requests
import mechanize
import re
import pandas as pd
session = requests.session()
url = "https://drt.gov.in/front/page1_advocate.php"
r = session.get(url)
soup = bs(r.text, 'html.parser')
# without using selenuim  mechanize has been used for the search button
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.set_handle_refresh(False)
br.addheaders=[('User-agent', 'Mozilla/5.0')]
items = soup.select('option[value]')
values = [item.get('value') for item in items]
textValues = [item.text for item in items]
# drop down slection list
def get_form_details(form):
    for input_tag in form.find("input"):
        # get type of input form control
        input_type = input_tag.attrs.get("type", "text")
        # get name attribute
        input_name = input_tag.attrs.get("name")
        # get the default value of that input tag
# Captch details entering
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
data = br.submit()
#table
table = soup.find("table")
rx = re.compile(r"\n {1,}")
cleanSoup = bs(re.sub(rx, "", str(soup)))
table = cleanSoup.find_all('table')[0]
for row in table.findAll('td'):
    #print(row)
     row = row.text
     print(row)

#finding table details
urls = {}   # Use a dictionary to create unique, ordered URLs (Assuming Python >=3.6)

for script in soup.find_all('script'):
    for m in re.findall(r"var urlstr = '(.*?)';", script.text):
        urls[m] = None

urls = list(urls.keys())
print(urls)
table = pd.read_html(url)