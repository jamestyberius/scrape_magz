import requests
from bs4 import BeautifulSoup

from secret_config import EMAIL, CWPW, FORM_ID, AB_KEY
  
URL = "https://www.commonwealmagazine.org"
login_url = URL + '/front?destination=front'

issues_urls = []
for x in range(7):
    issues_urls.append(URL + '/issues?page=' + str(x))

'''
payload = {
    'name':   EMAIL,
    'pass':   CWPW,
    'form_build_id': FORM_ID,
    'form_id':    'user_login_block',
    'antibot_key': AB_KEY,
    'op':	'Log+in'
}
'''

with requests.session() as s:

    # Login
    # r = s.post(login_url, data=payload)

    # Go to each issues page
    i = 0
    for x in issues_urls:
        print('Page:' + str(i))
        r2 = s.get(x)
        soup = BeautifulSoup(r2.content, 'html5lib')

        # Get list of issues on each page
        table = soup.select('div.field-content a')
        issue_links = []
        for row in table:
            issue = row['href']
            issue_links.append(issue)
            print(issue)
        i += 1