import requests
from bs4 import BeautifulSoup

from secret_config import EMAIL, CWPW, FORM_ID, AB_KEY
  
URL = "https://www.commonwealmagazine.org/"
login_url = URL + 'front?destination=front'
issues_url = URL + 'issues'

payload = {
    'name':   EMAIL,
    'pass':   CWPW,
    'form_build_id': FORM_ID,
    'form_id':    'user_login_block',
    'antibot_key': AB_KEY,
    'op':	'Log+in'
}


with requests.session() as s:
    r = s.post(login_url, data=payload)
    r2 = s.get(issues_url)

    soup = BeautifulSoup(r2.content, 'html5lib')
    print(soup.prettify())